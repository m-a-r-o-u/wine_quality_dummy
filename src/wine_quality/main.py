# src/wine_quality/main.py

def main():
    from wine_quality.data_loader import load_data
    from wine_quality.preprocess import preprocess_data
    from wine_quality.train import train_model
    from wine_quality.evaluate import evaluate_model
    from sklearn.model_selection import train_test_split

    print("Loading data...")
    data = load_data("data/winequality-red.csv")

    print("Preprocessing data...")
    X, y = preprocess_data(data)

    print("Splitting data...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    print("Training model...")
    model = train_model(X_train, y_train)

    print("Evaluating model...")
    evaluate_model(model, X_test, y_test)

if __name__ == "__main__":
    main()

