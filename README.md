# 🌍 **Atmos Viz: Global Temperature Analysis and Prediction**
### **Overview**
**Atmos Viz** is a Python-based project designed to analyze, visualize, and predict global temperature trends across various cities and countries. Leveraging historical climate data, this project combines **machine learning models**, **geospatial mapping**, and **interactive visualizations** to uncover meaningful insights into temperature variations over time.

---

### **Project Features**
- **Data Preprocessing**: Efficiently handles large-scale datasets, cleans missing values, and extracts features like **Year**, **Month**, and cyclic seasonal trends.
- **Geospatial Mapping**: Visualizes temperature data geographically using **shapefiles** and tools like **GeoPandas** and **Plotly**.
- **Machine Learning Prediction**: Forecasts future temperature trends using **Linear Regression** and **Random Forest** models.
- **Interactive Visualizations**: Generates engaging charts, heatmaps, and world maps for better analysis and understanding.
- **Performance Evaluation**: Measures model accuracy using metrics like **MAE**, **RMSE**, and **R²**.

---

### **Technologies Used**
- **Programming Language**: Python
- **Libraries**:
  - Data Handling: `Pandas`, `NumPy`
  - Visualization: `Matplotlib`, `Seaborn`, `Plotly`
  - Geospatial Mapping: `GeoPandas`
  - Machine Learning: `Scikit-learn`
  - GIS Tools: **Shapefiles**

---

### **Project Workflow**
1. **Data Preprocessing**
   - Load the temperature dataset (sourced from Kaggle, originally from Berkeley Earth).
   - Clean and normalize missing temperature values using **monthly means**.
   - Extract cyclic seasonal trends using sine and cosine transformations.

2. **Model Development**
   - Use **Linear Regression** and **Random Forest** for predictive modeling.
   - Train models using features like **Year**, **sin_month**, and **cos_month**.
   - Evaluate performance using **MAE**, **RMSE**, and **R²** metrics.

3. **Visualization**
   - **Geospatial Maps**: Display temperature data using **GeoPandas** and **Plotly**.
   - **Time-Series Trends**: Plot temperature trends with trendlines for specific cities.
   - **Interactive Maps**: Visualize data with **hover information** for cities on the map.
   - **Heatmaps & Boxplots**: Analyze monthly and regional temperature variations.
   
## Contributions
### Contributions are welcome! If you'd like to improve this project, please fork the repository and create a pull request.

## Contact
### For any queries or suggestions, feel free to contact me:

## Email: siddhantborse27@gmail.com
## VPortfolio: Siddhant Borse
## ⭐ If you like this project, star it on GitHub! ⭐

---

### **Project Directory Structure**
```plaintext
Atmos-Viz/
│
├── Package/
│   ├── data_preprocessing.py      # Data loading, cleaning, and feature extraction
│   ├── models.py                  # Machine learning model training
│   ├── evaluation.py              # Model evaluation metrics
│   ├── viz.py                     # Visualization functions (maps, charts, heatmaps)
│
├── shapefiles/                    # GIS shapefiles for mapping
│
├── data/                          # Raw and preprocessed temperature datasets
│
├── main.py                        # Main script for model execution and visualization
│
├── requirements.txt               # List of dependencies
│
└── README.md                      # Project documentation




