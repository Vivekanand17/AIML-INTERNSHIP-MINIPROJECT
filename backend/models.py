from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor


def get_linear_model():
    return LinearRegression()

def get_tree_model(max_depth, min_samples_leaf):
    return DecisionTreeRegressor(
        max_depth=max_depth,
        min_samples_leaf=min_samples_leaf,
        random_state=42
    )

def get_mlp_model(input_dim, hidden_units, learning_rate):
    raise NotImplementedError(
        "MLP model is not available on this deployment (TensorFlow removed). "
        "Use 'linear' or 'tree' model_type instead."
    )
