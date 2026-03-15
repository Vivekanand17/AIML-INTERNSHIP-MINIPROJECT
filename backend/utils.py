import pandas as pd
import numpy as np

def eda_summary(df):
    return {
        "shape": df.shape,
        "missing_values": df.isnull().sum().to_dict(),
        "dtypes": df.dtypes.astype(str).to_dict(),
        "head": df.head().to_dict(orient="records")
    }

def handle_missing(df, strategy):
    if strategy == "drop":
        return df.dropna()
    elif strategy == "mean":
        return df.fillna(df.mean(numeric_only=True))
    elif strategy == "median":
        return df.fillna(df.median(numeric_only=True))
    elif strategy == "mode":
        return df.fillna(df.mode().iloc[0])
    else:
        return df

def detect_diagnostics(train_loss, val_loss):
    flags = {
        "overfitting": False,
        "underfitting": False,
        "unstable": False,
        "message": ""
    }

    if any(np.isnan(train_loss)) or any(np.isnan(val_loss)):
        flags["unstable"] = True
        flags["message"] = "Training unstable (NaN detected). Reduce learning rate."

    if train_loss[-1] < train_loss[0] and val_loss[-1] > val_loss[0]:
        flags["overfitting"] = True
        flags["message"] = "Overfitting detected. Try regularization or more data."

    if train_loss[-1] > 0.5 and val_loss[-1] > 0.5:
        flags["underfitting"] = True
        flags["message"] = "Underfitting detected. Increase model complexity."

    return flags
