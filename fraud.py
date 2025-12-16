import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

# Load dataset
df = pd.read_csv("C:\\Users\\hp\\Downloads\\archive (1)\\creditcard.csv")

# Separate normal and fraud
normal = df[df['Class'] == 0]
fraud = df[df['Class'] == 1]

# Undersample normal class
normal_sample = normal.sample(n=492, random_state=42)

# Combine and shuffle
new_data = pd.concat([normal_sample, fraud], axis=0)
new_data = new_data.sample(frac=1, random_state=42).reset_index(drop=True)

# Split features and target
X = new_data.drop(columns='Class', axis=1)
Y = new_data['Class']

# Train-test split
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, stratify=Y, random_state=3
)

# Feature scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train_scaled, Y_train)

# Accuracy on training data
X_train_prediction = model.predict(X_train_scaled)
training_data_accuracy = accuracy_score(Y_train, X_train_prediction)
print('Accuracy on Training data:', training_data_accuracy)

# Accuracy on test data
X_test_prediction = model.predict(X_test_scaled)
test_data_accuracy = accuracy_score(Y_test, X_test_prediction)
print('Accuracy on Testing data:', test_data_accuracy)
