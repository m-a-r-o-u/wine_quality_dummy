# src/wine_quality/train.py

from sklearn.ensemble import RandomForestClassifier

def train_model(X_train, y_train):
    """
    Trains a Random Forest Classifier.
    """
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    return model

