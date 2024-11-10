# src/wine_quality/train.py
import yaml
from src.wine_quality.model_factory import get_model

def load_config(config_path='config.yaml'):
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

def train_model(X_train, y_train, config_path='config.yaml'):
    """
    Trains a model specified in the configuration file.
    """
    config = load_config(config_path)
    model_name = config['model']['name']
    model_params = config['model'].get('params', {})

    model = get_model(model_name, **model_params)
    model.fit(X_train, y_train)
    return model

