from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import os
from datetime import datetime
import pandas as pd
from utils import eda_summary, handle_missing
from train import train_model

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI ML Internship Project Backend Running Successfully"}

# ✅ CORS CONFIGURATION
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development (simplest fix)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

data_store = None


@app.post("/upload")
async def upload_csv(file: UploadFile = File(...)):
    global data_store
    try:
        df = pd.read_csv(file.file)
        data_store = df
        return eda_summary(df)
    except Exception as e:
        return JSONResponse(status_code=400, content={"error": str(e)})


@app.post("/clean")
def clean_data(strategy: str):
    global data_store
    if data_store is None:
        return JSONResponse(status_code=400, content={"error": "No dataset uploaded"})
    
    data_store = handle_missing(data_store, strategy)
    return {"message": "Cleaning applied successfully"}


@app.post("/train")
def train(config: dict):
    global data_store
    if data_store is None:
        return JSONResponse(status_code=400, content={"error": "No dataset uploaded"})

    columns = list(data_store.columns)
    requested_target = config.get("target_column")

    # If the requested target column does not exist, gracefully fall back
    if requested_target in columns:
        target_column = requested_target
    else:
        # Use the last column as target if the requested one is missing
        target_column = columns[-1]

    try:
        logs, diagnostics = train_model(
            data_store,
            target_column,
            config.get("model_type"),
            config.get("params", {})
        )

        # Save the (possibly cleaned) dataset to a top-level "data" folder
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        data_dir = os.path.join(project_root, "data")
        os.makedirs(data_dir, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"cleaned_dataset_{timestamp}.csv"
        output_path = os.path.join(data_dir, filename)

        # Use the current data_store as the cleaned dataset
        data_store.to_csv(output_path, index=False)

        return {
            "logs": logs,
            "diagnostics": diagnostics,
            "used_target_column": target_column,
            "saved_cleaned_dataset": output_path,
        }

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})


import uvicorn

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=10000)