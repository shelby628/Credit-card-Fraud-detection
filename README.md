# CREDIT CARD FRAUD DETECTION USING LOGISTIC REGRESSION

1.Overview

Data Sources

Tools Used

Methodology

Key Questions (KPIs)

Model Evaluation

Visualizations

Conclusion

How to Run the Project

Author

1.Overview

This project focuses on detecting fraudulent credit card transactions using Logistic Regression, a widely used classification algorithm.
The dataset used is highly imbalanced, with fraudulent transactions representing a very small percentage of total transactions. To address this, undersampling and proper preprocessing techniques were applied to build a more reliable and meaningful machine learning model.

The goal of this project is to demonstrate:

Handling imbalanced datasets

Applying supervised machine learning techniques

Building and evaluating a fraud detection model using Python

Data Sources

Dataset: Credit Card Transactions Dataset

Total Transactions: 284,807

Fraudulent Transactions: 492

Features

V1 – V28: PCA-transformed, anonymized features

Amount: Transaction amount

Time: Time elapsed between transactions

Class: Target variable

0 → Normal transaction

1 → Fraudulent transaction

Note: PCA was applied to protect sensitive customer information, so individual V-columns are not directly interpretable.

Tools Used

Python (Jupyter Notebook)

Python Script

Libraries:

pandas

numpy

scikit-learn

matplotlib

Methodology
1. Data Loading

The dataset is loaded using pandas, followed by initial inspection to understand structure, size, and class distribution.

2. Handling Class Imbalance

The dataset is extremely imbalanced.

All fraudulent transactions are retained.

A random sample of normal transactions is selected to balance the classes using undersampling.

3. Data Shuffling

The balanced dataset is shuffled to eliminate any ordering bias.

4. Feature and Target Separation

Features (X): All columns except Class

Target (y): Class

5. Train-Test Split

80% training data

20% testing data

Stratified split is used to preserve class distribution.

6. Feature Scaling

StandardScaler is applied to standardize numerical features.

Scaling is performed after splitting to prevent data leakage.

7. Model Training

Logistic Regression is used as the classification model.

max_iter is increased to ensure proper model convergence.

Key Questions (KPIs)

How accurately can the model detect fraudulent transactions?

How well does the model generalize to unseen data?

Does undersampling improve fraud detection performance?

Is Logistic Regression suitable for this classification task?

Model Evaluation

The model is evaluated using:

Accuracy score on training and testing data

Confusion Matrix

Precision, Recall, and F1-score
(These metrics are especially important for imbalanced datasets like fraud detection.)

Visualizations

Class distribution before and after balancing

Model performance metrics visualization

Confusion matrix plot

Conclusion

This project demonstrates an end-to-end machine learning workflow for detecting fraudulent credit card transactions.
By addressing class imbalance and applying proper preprocessing techniques, the Logistic Regression model is able to identify fraudulent transactions more effectively than a naïve baseline approach.

The project highlights the importance of:

Data preprocessing

Handling imbalanced datasets

Choosing appropriate evaluation metrics in fraud detection problems

How to Run the Project

Clone the repository or download the proj

