# Vehicle Price Prediction

This is a machine learning web application that predicts vehicle prices based on their specifications using Ridge Regression. The project includes a complete data preprocessing pipeline, model training workflow, and a Flask-based web interface to make predictions interactively.

## Project Overview

- Predicts the price of vehicles using features like make, model, year, mileage, engine specs, transmission, and more.
- Built using Python, Flask, and scikit-learn.
- Cleaned dataset is used to train a Ridge Regression model.
- The application runs locally and provides a simple web form for user input.

## Dataset Description

The dataset (`dataset.csv`) contains records of various vehicles with features commonly found in listings or inventory systems. After preprocessing, the cleaned dataset (`Cleaned_data.csv`) is used for model training and web form population.

### Raw Columns (Before Cleaning)
- `name`, `description`: Unstructured text fields not used in the model.
- `make`, `model`, `year`, `price`: Basic identifying fields.
- `engine`, `cylinders`, `fuel`, `mileage`, `transmission`, `trim`, `body`, `doors`, `exterior_color`, `interior_color`, `drivetrain`: Core features used or processed.

### Cleaned Columns (Used for Modeling)
- Categorical: `make`, `model`, `fuel`, `trim`, `body`, `drivetrain`, `transmission_type`, `valve_type_simplified`, `exterior_combo_interior`
- Numerical: `year`, `mileage`, `cylinders`, `doors`, `transmission_speed`
- Target: `log_price` (log-transformed version of `price`)

## Model Information

- Model: Ridge Regression (L2 regularization)
- Preprocessing: Standard scaling for numerical columns, one-hot encoding for categorical columns
- Target: `log_price`, exponentiated during prediction to return actual dollar value
- Performance:
  - R² Score: ~0.89
  - RMSE: ~0.11 (on log scale)

## How to Run the App

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/vehicle-price-predictor.git
   cd vehicle-price-predictor
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
4. Run the Flask app:
   ```bash
   python main.py
5. Open your browser and go to `http://127.0.0.1:5000` to use the predictor.

## Files Included
- `main.py`– Flask application script
  
- `RidgeModel.pkl` – Trained Ridge Regression model

- `Cleaned_data.csv` – Clean dataset used for prediction

- `dataset.csv` – Original raw dataset

- `vehicleprediction.ipynb` – Jupyter notebook for cleaning, feature engineering, and training

- `requirements.txt `– Project dependencies

- `templates/index.html` – Frontend form interface

- `README.md` – Project documentation

## Demonstration

vedio and stuff
