# src/wine_quality/preprocess.py

def preprocess_data(data):
    """
    Preprocesses the dataset by handling missing values and encoding.
    """
    # For this dataset, there are no missing values or categorical features
    # but we can implement scaling if needed.
    features = data.drop('quality', axis=1)
    target = data['quality']
    
    # Simplify the target variable: good (7 or higher), not good (below 7)
    target = target.apply(lambda x: 1 if x >= 7 else 0)
    
    return features, target

