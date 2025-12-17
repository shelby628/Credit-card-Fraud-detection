

# CREDIT CARD FRAUD DETECTION USING LOGISTIC REGRESSION


## Table of Contents
1. [Overview](#overview)
2. [Data Sources](#data-sources)
3. [Tools Used](#tools-used)
4. [Process](#process)
5.  [QUESTIONS (KPI)](#QUESTIONS (KPI))
6. [Key Insights](#key-insights)
7. [Visualizations](#visualizations)
8. [Conclusion](#conclusion)
9. [Author](#author)
   




## Overview / Objectives
This project focuses on detecting fraudulent credit card transactions using Logistic Regression.
The dataset is highly imbalanced, so undersampling and proper preprocessing techniques are applied to build a reliable machine learning model.
## Data Sources
- `Dataset` — Credit Card Transactions Dataset 
-Total transactions: 284,807

Fraudulent transactions: 492

Features:

V1 to V28: PCA-transformed, anonymized features

Amount: Transaction amount

Time: Time elapsed between transactions

Class: Target variable (0 = normal, 1 = fraud)

Note: PCA was applied to protect sensitive customer information, so individual V-columns are not interpretable.
## Tools Used
- Python (Jupyter Notebook)
- Python (script-Pandas,Numpy,scikit-learn,matplotlib)

- Methodology
1️.Data Loading

The dataset is loaded using pandas and basic inspection is performed.

2️. Handling Class Imbalance

The dataset is highly imbalanced.

All fraud transactions are retained.

A random sample of normal transactions is selected to balance the classes.

3️. Data Shuffling

The balanced dataset is shuffled to remove any ordering bias.

4️. Feature and Target Separation

Features (X): All columns except Class

Target (Y): Class

5️. Train-Test Split

80% training data

20% testing data

Stratified split is used to preserve class distribution

6️.  Feature Scaling

StandardScaler is applied to standardize features

Scaling is done after splitting to prevent data leakage

7️. Model Training

Logistic Regression is used

Increased max_iter to ensure convergence

8. Model Evaluation

Accuracy is calculated on both training and testing datasets



How to Run the Project

Clone the repository or download the files

Install required dependencies:

pip install pandas numpy scikit-learn matplotlib


Run the script:

python fraud_detection.py

 
