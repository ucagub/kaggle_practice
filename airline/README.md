# Airline Passenger Satisfaction Classification

## Summary
This notebook compares four classifiers to predict airline passenger satisfaction based on various features. The classifiers evaluated include XGBoost, LightGBM (LGBM), Random Forest, and a Dense Neural Network (NN).

### Key Findings
- **Accuracy**:
  - **XGBoost**: 96%
  - **LightGBM**: 96%
  - **Random Forest**: 96%
  - **Dense Neural Network**: 77%
  - **K-means Classifier**: 50%
  
- The feature identified as the most important for predicting passenger satisfaction was **Inflight WiFi Service**.

Flask API was dockerized.

## Table of Contents
1. [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
2. [Model Training and Optimization](#model-training-and-optimization)
    - [XGBoost](#xgboost)
    - [LightGBM](#lightgbm)
    - [Random Forest](#random-forest)
    - [Neural Network in Keras](#neural-network-in-keras)
    - [K-means Classifier](#k-means-classifier)
3. [Flask API](#flask-api)

## Data Source
The dataset used for this analysis can be found at [Kaggle: Airline Passenger Satisfaction](https://www.kaggle.com/datasets/teejmahal20/airline-passenger-satisfaction).

## Tools Used
- **Classifiers**:
  - XGBoost
  - LightGBM (LGBM)
  - Random Forest
- **Metrics & Visualization**:
  - Confusion Matrix
  - Feature Importance
  - Plots (Seaborn, Matplotlib)
- **Logging & Optimization**:
  - MLflow for logging experiments
  - Optuna for hyperparameter optimization
- **Data Preparation**:
  - Pipeline, ColumnTransformer, OneHotEncoder, Simple