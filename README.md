# Wine Quality Prediction Project

A simple data science project that predicts wine quality using a Random Forest Classifier.

## Project Structure

- **src/wine_quality/**: Contains the Python package modules.
- **data/**: Contains the dataset.
- **notebooks/**: Jupyter notebooks for exploratory data analysis.
- **setup.py**: Package configuration.
- **README.md**: Project documentation.

## Requirements

- **Python**: 3.7 or higher
- **Dependencies**:
  - pandas>=1.0.0,<2.0.0
  - numpy>=1.18.0,<2.0.0
  - scikit-learn>=0.24.0,<0.25.0

## Installation

### Prerequisites

- **Python**: Ensure you have Python 3.7 or higher installed.
- **pip**: Python package installer.
- **Optional**: [pyenv](https://github.com/pyenv/pyenv) for managing Python versions and virtual environments.

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/wine_quality_project.git
   cd wine_quality_project
   ```

2. **Set Up a Local Python Environment (Recommended)**

   Use `pyenv` and `venv` to create an isolated environment for the project.

   ```bash
   # Install Python 3.9.0 using pyenv (if not already installed)
   pyenv install 3.9.0

   # Set the local Python version for the project
   pyenv local 3.9.0

   # Create a virtual environment
   python -m venv .venv

   # Activate the virtual environment
   source .venv/bin/activate

   # Upgrade pip
   pip install --upgrade pip
   ```

3. **Install the Package**

   Install the package in editable mode along with its dependencies.

   ```bash
   pip install -e .
   ```

## Downloading and Storing the Data

The project uses the **Wine Quality Dataset** (red wine variant) from the UCI Machine Learning Repository.

### Steps to Download the Data

1. **Download the Dataset**

   - Visit the [UCI Machine Learning Repository Wine Quality Data Set](https://archive.ics.uci.edu/ml/datasets/wine+quality).
   - Direct download link for the red wine dataset: [winequality-red.csv](https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv).

2. **Store the Data**

   - Place the `winequality-red.csv` file into the `data/` directory of the project.

     ```bash
     mv /path/to/downloaded/winequality-red.csv data/winequality-red.csv
     ```

   - Ensure the file is named exactly `winequality-red.csv` and located in the `data/` folder to match the expected file path in the code.

## Usage

Run the prediction pipeline using the console script:

```bash
wine_quality_predictor
```

This command executes the entire data science workflow:

1. **Load Data**: Reads the dataset from `data/winequality-red.csv`.
2. **Preprocess Data**: Simplifies the target variable and prepares features.
3. **Split Data**: Divides the data into training and testing sets.
4. **Train Model**: Trains a Random Forest Classifier.
5. **Evaluate Model**: Outputs a classification report.

**Sample Output:**

```
Loading data...
Preprocessing data...
Splitting data...
Training model...
Evaluating model...
Classification Report:
              precision    recall  f1-score   support

           0       0.89      0.96      0.93       273
           1       0.68      0.43      0.53        47

    accuracy                           0.87       320
   macro avg       0.78      0.70      0.73       320
weighted avg       0.86      0.87      0.86       320
```

## Project Workflow

- **Data Loading**: Implemented in `src/wine_quality/data_loader.py`.
- **Data Preprocessing**: Implemented in `src/wine_quality/preprocess.py`.
- **Model Training**: Implemented in `src/wine_quality/train.py`.
- **Model Evaluation**: Implemented in `src/wine_quality/evaluate.py`.
- **Main Execution Script**: `src/wine_quality/main.py` orchestrates the workflow.

## Dependencies

The project's dependencies are specified in `setup.py` under `install_requires`. These dependencies will be installed automatically when you install the package.

- **Runtime Dependencies**:
  - pandas>=1.0.0,<2.0.0
  - numpy>=1.18.0,<2.0.0
  - scikit-learn>=0.24.0,<0.25.0

## Development Dependencies (Optional)

If you plan to contribute to the project, you may need additional development tools:

- **Testing**: pytest
- **Code Formatting**: black
- **Linting**: flake8

Install development dependencies:

```bash
pip install -r requirements-dev.txt
```

*Note: Create a `requirements-dev.txt` file listing the development dependencies.*

## License

This project is licensed under the MIT License.

## Acknowledgments

- Dataset provided by the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/wine+quality).


