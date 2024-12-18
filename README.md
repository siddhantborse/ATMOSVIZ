Atmos Viz: Global Temperature Analysis and Prediction

Project Overview:
Atmos Viz is a comprehensive project aimed at analyzing, visualizing, and predicting global temperature trends using historical climate data. The project leverages advanced data preprocessing, machine learning models, and geospatial visualization tools to uncover patterns in temperature variations across cities and countries worldwide. By combining statistical analysis with interactive visualizations, Atmos Viz provides meaningful insights into historical trends while forecasting future climate behaviors.

Key Features:

Large-Scale Data Processing: Efficient handling of half-GB-sized datasets with Python libraries like Pandas and NumPy to manage missing values and optimize computations.
Geospatial Mapping: Integration of GeoPandas and shapefiles for GIS-based temperature mapping, enabling accurate visualization of city-wise and country-level temperature trends.
Machine Learning Models: Implementation of Linear Regression and Random Forest to predict future temperature trends based on historical data and evaluate model performance using metrics such as MAE, RMSE, and R².
Interactive Visualizations: Development of dynamic plots using Plotly and Matplotlib for city-specific and global temperature trends, including trendlines, heatmaps, and boxplots.
Cyclic Features: Addition of cyclic seasonal features for better trend identification, capturing monthly variations in temperature behavior.
Project Components:

Data Preprocessing:

Parsing and cleaning historical temperature data from CSV files.
Filling missing values using mean monthly temperature trends for cities.
Extracting relevant features, including Year, Month, and cyclic features like sin_month and cos_month.
Predictive Modeling:

Splitting data into training and testing sets.
Training Linear Regression and Random Forest models to predict temperature trends.
Evaluating predictions with robust performance metrics: MAE, RMSE, and R².
Geospatial Visualization:

Plotting world temperature maps using GeoPandas and shapefiles to showcase city-specific temperature variations.
Creating interactive scatter plots using Plotly for dynamic temperature exploration across regions.
Interactive Plots:

Generating time-series temperature trend plots for specific cities with trendlines.
Creating heatmaps of monthly temperature variations and boxplots for continental temperature distributions.
Technologies Used:

Programming Language: Python
Libraries: Pandas, NumPy, Matplotlib, Seaborn, Plotly, GeoPandas, Scikit-learn
Tools: Shapefiles for GIS mapping, Jupyter Notebooks/VSCode for development
