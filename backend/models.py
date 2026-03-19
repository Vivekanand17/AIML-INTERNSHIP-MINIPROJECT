from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.neural_network import MLPRegressor, MLPClassifier
from sklearn.metrics import accuracy_score


def get_linear_model():
    return LinearRegression()

def get_tree_model(max_depth, min_samples_leaf):
    return DecisionTreeRegressor(
        max_depth=max_depth,
        min_samples_leaf=min_samples_leaf,
        random_state=42
    )

def get_mlp_regressor(input_dim, hidden_units, learning_rate):
    return MLPRegressor(
        hidden_layer_sizes=(hidden_units,),
        learning_rate_init=learning_rate,
        max_iter=500,
        batch_size="auto",
        random_state=42,
        early_stopping=True,
        validation_fraction=0.1
    )

def get_mlp_classifier(input_dim, hidden_units, learning_rate):
    return MLPClassifier(
        hidden_layer_sizes=(hidden_units,),
        learning_rate_init=learning_rate,
        max_iter=500,
        batch_size="auto",
        random_state=42,
        early_stopping=True,
        validation_fraction=0.1
    )
