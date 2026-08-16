 House Price Prediction

Project Overview

This project focuses on predicting house sale prices using machine learning.

The main objective is to build a machine learning model that can predict 'SalePrice' and compare the performance of two regression algorithms:

- Linear Regression
- Random Forest Regressor

An additional experiment was also performed using Random Forest Regressor to predict `OverallQual`.

 Objectives

- Clean and preprocess the housing dataset
- Perform exploratory data analysis (EDA)
- Handle missing values
- Encode categorical features
- Build machine learning pipelines
- Train and compare regression models
- Evaluate models using R² score and MAE
- Select the best-performing model
- Deploy the final model using Streamlit

 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit


 Exploratory Data Analysis

Exploratory data analysis was performed to understand the dataset and identify relationships between different housing features and 'SalePrice'.

Some of the analysis included:

- Distribution of house prices
- Relationship between 'GrLivArea' and SalePrice
- Relationship between OverallQual and SalePrice
- Analysis of numerical and categorical features
- Missing-value analysis

 Data Preprocessing

The following preprocessing techniques were used:

- Handling missing values
- Feature selection
- Log transformation of 'SalePrice
- One-hot encoding of categorical variables
- ColumnTransformer for preprocessing
- Scikit-learn Pipeline for combining preprocessing and the model

---
 Machine Learning Models

1. Linear Regression

Linear Regression was used as the baseline model for predicting SalePrice'.

R² Score: 0.8923

 2. Random Forest Regressor

Random Forest Regressor was used to compare its performance with Linear Regression for predicting SalePrice.

R² Score: ~0.86**

---

 Model Comparison

| Model | Target | R² Score |
| Linear Regression | SalePrice | 0.8923 |
| Random Forest Regressor | SalePrice | 0.86 |

Final Model

Linear Regression was selected as the final model because it achieved a higher R² score than Random Forest Regressor on the test dataset.

This demonstrates that a more complex model does not always perform better. The final model was selected based on evaluation results.

---

Additional Experiment

Random Forest Regressor was also used to predict OverallQual as an additional experiment.

The purpose of this experiment was to explore another prediction task using the housing dataset.

Deployment

The machine learning model is deployed using Streamlit Community Cloud
[Live Application(https://saleprice-prediction.streamlit.app) to predict the saleprice
The trained Random Forest model has been deployed using Streamlit community cloud to predict overallqual
[Live Application(https://overallqual.streamlit.app)
