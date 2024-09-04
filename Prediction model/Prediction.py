import pandas as pd
import numpy as np

# Define the model coefficients
coefficients = {
    'const': -3288.106307,
    'total_trip_count': 6.021109408,
    'rain': -13.60958329,
    'Area_NE': -195.007402,
    'Area_N': 913.9910828,
    'Area_SE': -55.60656884,
    'month_2': 943.6972683,
    'month_3': 800.377454,
    'month_4': 646.7796299,
    'month_5': 963.1984018,
    'month_6': 1565.426541,
    'month_7': 1439.403119,
    'month_8': 1344.824352,
    'month_9': 2093.493887,
    'month_10': 1828.273438,
    'month_11': 1251.752054,
    'month_12': 479.7387096,
    'Bike_Lanes': 3981.443621,
    'Area_CC': 12701.56814
}

# Pre-load the rain data (assuming 'Time' is the date and rain values are in a column 'rain')
rain_data = pd.read_csv('/Users/chris/Library/Mobile Documents/com~apple~CloudDocs/工作/Data Storytelling/Strava Model_Full_Local_0831/Prediction model/Rainfall(prediction dependency).csv')
# Ensure 'Time' in rain_data is a datetime object
rain_data['Time'] = pd.to_datetime(rain_data['Time'])
rain_data.set_index('Time', inplace=True)

def prompt_yes_no(question):
    """Prompt the user with a yes/no question and return 1 for yes, 0 for no."""
    while True:
        response = input(question + " (yes/no): ").strip().lower()
        if response == "yes":
            return 1
        elif response == "no":
            return 0
        else:
            print("Please answer 'yes' or 'no'.")

def generate_month_dummies(time_series):
    """Extracts the month from a time series and generates dummies."""
    months = pd.to_datetime(time_series).dt.month
    month_dummies = pd.get_dummies(months, prefix='month', drop_first=False)
    return month_dummies

def predict(data, rain_data):
    """Predicts the outcome based on the model and data provided."""
    # Add constant
    data['const'] = 1

    # Generate month dummies
    month_dummies = generate_month_dummies(data['Time'])
    data = pd.concat([data, month_dummies], axis=1)

    # Add missing month columns (for months not present in the data)
    for month in range(2, 13):
        col_name = f'month_{month}'
        if col_name not in data.columns:
            data[col_name] = 0

    # Map rain data based on 'Time'
    data['rain'] = data['Time'].map(rain_data['rain'])

    # Prompt the user for area dummies and cycle lane dummy
    data['Area_NE'] = prompt_yes_no("Is the area Northeast (NE)?")
    data['Area_N'] = prompt_yes_no("Is the area North (N)?")
    data['Area_SE'] = prompt_yes_no("Is the area Southeast (SE)?")
    data['Area_CC'] = prompt_yes_no("Is the area Central City (CC)?")
    data['Bike_Lanes'] = prompt_yes_no("Are there bike lanes present?")

    # Calculate the predicted values by multiplying each coefficient with its corresponding variable
    data['prediction'] = (
        data['const'] * coefficients['const'] +
        data['total_trip_count'] * coefficients['total_trip_count'] +
        data['rain'] * coefficients['rain'] +
        data['Area_NE'] * coefficients['Area_NE'] +
        data['Area_N'] * coefficients['Area_N'] +
        data['Area_SE'] * coefficients['Area_SE'] +
        data['Area_CC'] * coefficients['Area_CC'] +
        data['Bike_Lanes'] * coefficients['Bike_Lanes'] +
        data['month_2'] * coefficients['month_2'] +
        data['month_3'] * coefficients['month_3'] +
        data['month_4'] * coefficients['month_4'] +
        data['month_5'] * coefficients['month_5'] +
        data['month_6'] * coefficients['month_6'] +
        data['month_7'] * coefficients['month_7'] +
        data['month_8'] * coefficients['month_8'] +
        data['month_9'] * coefficients['month_9'] +
        data['month_10'] * coefficients['month_10'] +
        data['month_11'] * coefficients['month_11'] +
        data['month_12'] * coefficients['month_12']
    )

    return data[['Time', 'prediction']]

# Prompt the user to input the file path
file_path = input("Please enter the file path for your data CSV file: ")
df = pd.read_csv(file_path)

# Ensure 'Time' in df is a datetime object
df['Time'] = pd.to_datetime(df['Time'])

# Make predictions
predicted_df = predict(df, rain_data)

# Save predictions to a CSV file
predicted_df.to_csv('predicted_values.csv', index=False)

print(predicted_df)
