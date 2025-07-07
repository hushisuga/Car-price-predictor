from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Load cleaned data and model
data = pd.read_csv('Cleaned_data.csv')
model = pickle.load(open('RidgeModel.pkl', 'rb'))

# Prepare dropdown options globally
options = {
    "make": sorted(data['make'].dropna().unique().astype(str)),
    "model": sorted(data['model'].dropna().unique().astype(str)),
    "year": sorted(data['year'].dropna().unique().astype(str), reverse=True),
    "fuel": sorted(data['fuel'].dropna().unique().astype(str)),
    "cylinders": sorted(data['cylinders'].dropna().unique().astype(str)),
    "transmission_type": sorted(data['transmission_type'].dropna().unique().astype(str)),
    "transmission_speed": sorted(data['transmission_speed'].dropna().unique().astype(str)),
    "trim": sorted(data['trim'].dropna().unique().astype(str)),
    "body": sorted(data['body'].dropna().unique().astype(str)),
    "doors": sorted(data['doors'].dropna().unique().astype(str)),
    "valve_type_simplified": sorted(data["valve_type_simplified"].dropna().unique().astype(str)),
    "ext_color": sorted(data['exterior_combo_interior'].apply(lambda x: x.split('_Interior_')[0] if '_Interior_' in x else 'Other').unique()),
    "int_color": sorted(data['exterior_combo_interior'].apply(lambda x: x.split('_Interior_')[-1] if '_Interior_' in x else 'Other').unique()),
    "drivetrain": sorted(data['drivetrain'].dropna().unique().astype(str)),
}

@app.route('/')
def home():
    return render_template("index.html", options=options)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get numeric inputs
        mileage = float(request.form.get('mileage', 0))
        year = int(request.form.get('year', 2023))
        cylinders = float(request.form.get('cylinders', 4.0))
        doors = float(request.form.get('doors', 4.0))
        trans_speed = float(request.form.get('transmission_speed', 6.0).split('-')[0]) if '-' in request.form.get('transmission_speed', '') else float(request.form.get('transmission_speed', 6.0))

        # Get color combo
        ext_color = request.form.get('ext_color', 'Other')
        int_color = request.form.get('int_color', 'Other')
        color_combo = f"{ext_color}_Interior_{int_color}"

        # Prepare input data
        input_data = {
            'make': request.form.get('make', 'Other'),
            'model': request.form.get('model', 'Other'),
            'year': year,
            'fuel': request.form.get('fuel', 'Gasoline'),
            'cylinders': cylinders,
            'transmission_type': request.form.get('transmission_type', 'Automatic'),
            'transmission_speed': trans_speed,
            'mileage': mileage,
            'trim': request.form.get('trim', 'Other'),
            'body': request.form.get('body', 'SUV'),
            'doors': doors,
            'drivetrain': request.form.get('drivetrain', 'All-wheel Drive'),
            'exterior_combo_interior': color_combo,
            'valve_type_simplified': request.form.get('valve_type_simplified', 'DOHC')
        }

        # Create DataFrame
        df = pd.DataFrame([input_data])

        # Make prediction
        log_price = model.predict(df)[0]
        price = round(np.exp(log_price), 2)

        return render_template('index.html', prediction=price, options=options)

    except Exception as e:
        return f"<h3 style='color:red;'>Prediction Error: {e}</h3><br><a href='/'>Go Back</a>"

if __name__ == '__main__':
    app.run(debug=True)
