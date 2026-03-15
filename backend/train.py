import numpy as np
import json
import os
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from models import *
from utils import detect_diagnostics

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

def train_model(data, target_column, model_type, params):
    X = data.drop(columns=[target_column])
    y = data[target_column]

    X_train, X_val, y_train, y_val = train_test_split(
        X, y,
        test_size=params.get("val_split", 0.2),
        random_state=42
    )

    logs = {"train_loss": [], "val_loss": []}

    if model_type == "linear":
        model = get_linear_model()
        model.fit(X_train, y_train)
        train_pred = model.predict(X_train)
        val_pred = model.predict(X_val)

        logs["train_loss"].append(mean_squared_error(y_train, train_pred))
        logs["val_loss"].append(mean_squared_error(y_val, val_pred))

    elif model_type == "tree":
        model = get_tree_model(
            params.get("max_depth", 5),
            params.get("min_samples_leaf", 1)
        )
        model.fit(X_train, y_train)

        train_pred = model.predict(X_train)
        val_pred = model.predict(X_val)

        logs["train_loss"].append(mean_squared_error(y_train, train_pred))
        logs["val_loss"].append(mean_squared_error(y_val, val_pred))

    elif model_type == "mlp":
        model = get_mlp_model(
            X_train.shape[1],
            params.get("hidden_units", 32),
            params.get("learning_rate", 0.001)
        )

        history = model.fit(
            X_train, y_train,
            validation_data=(X_val, y_val),
            epochs=params.get("epochs", 20),
            batch_size=params.get("batch_size", 32),
            verbose=0
        )

        logs["train_loss"] = history.history["loss"]
        logs["val_loss"] = history.history["val_loss"]

    diagnostics = detect_diagnostics(
        logs["train_loss"],
        logs["val_loss"]
    )

    log_file = os.path.join(LOG_DIR, f"run_{model_type}.json")
    with open(log_file, "w") as f:
        json.dump(logs, f)

    return logs, diagnostics
