# src/wine_quality/model_factory.py
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

def get_model(model_name, **params):
    models = {
        'RandomForestClassifier': RandomForestClassifier,
        'GradientBoostingClassifier': GradientBoostingClassifier,
        'LogisticRegression': LogisticRegression,
        'SVC': SVC,
    }
    if model_name in models:
        return models[model_name](**params)
    else:
        raise ValueError(f"Unsupported model: {model_name}")

