# src/wine_quality/evaluate.py

from sklearn.metrics import classification_report

def evaluate_model(model, X_test, y_test):
    """
    Evaluates the model and prints a classification report.
    """
    predictions = model.predict(X_test)
    report = classification_report(y_test, predictions)
    print("Classification Report:\n", report)

