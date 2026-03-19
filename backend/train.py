import numpy as np
import json
import os
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, accuracy_score
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

    is_classification = y_train.nunique() <= 10
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
        epochs = params.get("epochs", 100)
        input_dim = X_train.shape[1]
        hidden_units = params.get("hidden_units", 64)
        learning_rate = params.get("learning_rate", 0.001)
        
        if is_classification:
            model = get_mlp_classifier(input_dim, hidden_units, learning_rate)
        else:
            model = get_mlp_regressor(input_dim, hidden_units, learning_rate)
        # Set max_iter dynamically if supported, but since in model init, note: sklearn MLP max_iter is fixed but early_stopping stops early
        model.max_iter = epochs  # Override for flexibility
        
        model.fit(X_train, y_train)
        
        # Use loss_curve_ for train losses
        logs["train_loss"] = model.loss_curve_.tolist()
        
        # Simulate val_loss
        val_pred = model.predict(X_val)
        if is_classification:
            val_acc = accuracy_score(y_val, val_pred)
            val_loss_val = 1 - val_acc  # Pseudo loss (1 - accuracy)
        else:
            val_loss_val = mean_squared_error(y_val, val_pred)
        logs["val_loss"] = [val_loss_val] * len(logs["train_loss"])

    diagnostics = detect_diagnostics(
        logs["train_loss"],
        logs["val_loss"]
    )

    log_file = os.path.join(LOG_DIR, f"run_{model_type}.json")
    with open(log_file, "w") as f:
        json.dump(logs, f)

    return logs, diagnostics
