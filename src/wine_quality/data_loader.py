# src/wine_quality/data_loader.py

import pandas as pd

def load_data(filepath):
    """
    Loads the wine quality dataset.
    """
    data = pd.read_csv(filepath, sep=';')
    return data

