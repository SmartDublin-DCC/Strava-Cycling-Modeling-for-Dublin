# Strava Data Prediction Model

This guide will help you run a prediction model using your Strava data. The model predicts certain outcomes based on the input data and coefficients derived from a pre-trained model.

## How to Run the Prediction Model?

### 1. Download the Python Script

- Download the Python file named `Prediction.py` from the repository.

### 2. Download the Rainfall Dependency

- Download the `Rainfall(prediction dependency).csv` file, which is necessary for the prediction model. This file contains weekly rainfall data that the model uses to adjust its predictions based on weather conditions.

### 3. Prepare Your CSV File with Strava Data

- Ensure your Strava data CSV file is formatted correctly. On how to download cycling data from `Strava Metro` see [here](https://github.com/SmartDublinGit/Strava-Cycling-Modeling-for-Dublin/blob/main/Prediction%20model/How%20to%20download%20Strava%20Metro%20route%20data.pdf). The CSV file should only have the following columns:
  - `Time`: A datetime column containing the date of weekly summed record. The format should be `YYYY-MM-DD`. On how to resample the daily data to weekly, see [here](https://github.com/SmartDublinGit/Strava-Cycling-Modeling-for-Dublin/blob/main/Route%20Based%20Analysis/Weekly_resampling.ipynb)
  - `total_trip_count`: The total count of Strava trips for the given time period.

### 4. Run the Python Script
- Make sure the rainfall csv is in the same folder as `Prediction.py`
- Open a terminal or command prompt.
- Navigate to the directory where the `Prediction.py` file is located.

- Run the Python script using the following command:

  ```bash
  python path/Prediction.py

- Then the predicted file should be generated in the same folder!

Good luck
