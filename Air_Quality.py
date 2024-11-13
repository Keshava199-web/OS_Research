import Bar_chart_traffic
import pandas as pd
from pathlib import Path
from sklearn.datasets import fetch_california_housing

# Define the path to the air quality dataset CSV
file_path = 'air_quality_data.csv'

# Check if the file exists using pathlib
file_path = Path(file_path)

try:
    # If file exists, load the data
    if file_path.is_file():
        data = pd.read_csv(file_path)
        print("File loaded successfully.")
    else:
        raise FileNotFoundError  # If the file doesn't exist, trigger an error

except FileNotFoundError:
    print(f"Error: The file '{file_path}' does not exist.")
    print("Loading California housing dataset as a placeholder...")

    # Example: Using a known dataset as a fallback
    data = fetch_california_housing()

    # Convert the data to a DataFrame for easier handling
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['target'] = data.target

    print("California housing dataset loaded as a fallback.")
    print(df.head())  # Display first few rows of the dataset

# Continue with your model or further processing
# You can now proceed with the SVM model or other operations


# import pandas as pd
# from sklearn.svm import SVR
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import mean_squared_error
#
# # Example: Load an air quality dataset (replace this with actual data source)
# # For example, data might contain features like temperature, humidity, traffic, etc.
# # Let's assume a dataset that includes PM2.5 (particulate matter) concentrations as the target.
# data = pd.read_csv('air_quality_data.csv')  # Replace with your actual dataset path
#
# # Assume 'features' are columns such as temperature, humidity, traffic, etc.
# # and 'PM2.5' is the column representing the pollutant concentration (target)
# X = data[['temperature', 'humidity', 'traffic']]  # Features (example)
# y = data['PM2.5']  # Target (pollutant concentration)
#
# # Split data into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#
# # Fit SVM model for regression
# svm_model = SVR(kernel='rbf')
# svm_model.fit(X_train, y_train)
#
# # Predict on the test set
# y_pred = svm_model.predict(X_test)
#
# # Calculate Mean Squared Error (MSE)
# mse = mean_squared_error(y_test, y_pred)
# print(f"Mean Squared Error for Air Quality Prediction: {mse}")
#
# # Predict air quality for new data points (e.g., a new location)
# new_data = [[25, 60, 300]]  # Example new data: [temperature, humidity, traffic]
# predicted_pm25 = svm_model.predict(new_data)
# print(f"Predicted PM2.5 level: {predicted_pm25[0]} µg/m³")
