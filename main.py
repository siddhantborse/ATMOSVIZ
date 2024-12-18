
from Package.data_preprocessing import load_data, preprocess_data,filter_data_by_country, filter_data_by_city
from Package.models import train_linear_regression, train_random_forest, prepare_train_test_data
from Package.evaluation import evaluate_model
from Package.viz import plot_temperature_trends, plot_world_temperature_map,plot_interactive_world_map,plot_monthly_temperature_heatmap,plot_temperature_boxplot
import pandas as pd
import os


# Load the data
file_path = r'C:\Users\phbor\OneDrive\Desktop\GEOG\Atmos Viz\GlobalLandTemperaturesByCity_500000.csv'

# df = pd.read_csv(file_path)
# print(len(df))
# num_rows = 100000
# for i in range(0, len(df), num_rows):
#     new_df = df[i:i+num_rows]
#     new_df.to_csv(f"GlobalLandTemperaturesByCity_{i}.csv", index=False)  # this code is written for breaking the large dataset

'the above code is written to break the largr chunk of CSV file into small chunks using pandas'

# Load the data from the specified file path
data = load_data(file_path)

# Define the city to be analyzed
x = 'Badajoz'

# Filter the data for the specified city
bal_data = filter_data_by_city(data, x)

# Preprocess the filtered city data
data = preprocess_data(bal_data)

# Define the country to be analyzed
z = 'Spain'

# Filter the data for the specified country
india_data = filter_data_by_country(data, z)

# Prepare data for modeling
# Define the target column (dependent variable) and feature columns (independent variables)
target_col = 'AverageTemperature'
feature_cols = ['Year', 'sin_month', 'cos_month']

# Split the data into training and testing sets for modeling
X_train, X_test, y_train, y_test = prepare_train_test_data(india_data, target_col, feature_cols)

# Train a Linear Regression model on the training data
linear_model = train_linear_regression(X_train, y_train)

# Train a Random Forest model on the training data
rf_model = train_random_forest(X_train, y_train)

# Make predictions using the Linear Regression model
y_pred_linear = linear_model.predict(X_test)

# Make predictions using the Random Forest model
y_pred_rf = rf_model.predict(X_test)

# Evaluate the Linear Regression model using metrics like MAE, RMSE, and R²
linear_metrics = evaluate_model(y_test, y_pred_linear)

# Evaluate the Random Forest model using metrics like MAE, RMSE, and R²
rf_metrics = evaluate_model(y_test, y_pred_rf)

# Print the evaluation metrics for both models
print("Linear Regression Metrics:", linear_metrics)
print("Random Forest Metrics:", rf_metrics)

# Visualization: Plot the temperature trends for the specified city (Badajoz)
plot_temperature_trends(data, x)

# Visualization: Create a Seaborn heatmap showing monthly temperature trends for Spain
plot_monthly_temperature_heatmap(data, country_name=z)

# Visualization: Add a 'Continent' column to the data for boxplot analysis
data['Continent'] = 'Europe'  # Assuming the data belongs to Europe

# Visualization: Create a Seaborn boxplot showing temperature distribution by continent
plot_temperature_boxplot(data)

# Visualization: Plot a world map showing temperature data for the specified shapefile
plot_world_temperature_map(data, shapefile_path=r'C:\Users\phbor\OneDrive\Desktop\GEOG\Atmos Viz\shapefiles\ne_10m_admin_0_countries.shp')

# Check if the shapefile exists in the specified directory
print(os.path.exists('C:/Users/phbor/OneDrive/Desktop/GEOG/Atmos Viz/shapefiles/world_shapefile.shp'))
