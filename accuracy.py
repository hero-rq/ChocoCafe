import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load the passenger data
passengers = pd.read_csv('passengers.csv')
print(passengers)

# Update sex column to numerical
# Map "female" to 1 and "male" to 0 in the Sex column
passengers['Sex'] = passengers['Sex'].map({'female': 1, 'male': 0})

# Fill the nan values in the age column
# print(passengers['Age'].values)
mean_age = passengers['Age'].mean()
passengers['Age'] = passengers['Age'].fillna(mean_age)

# Create a first class column let’s utilize the Pclass column, or the passenger class, as another feature. Create a new column named FirstClass that stores 1 for all passengers in first class and 0 for all other passengers.
passengers['FirstClass'] = (passengers['Pclass'] == 1).astype(int)

# Create a second class column
passengers['SecondClass'] = (passengers['Pclass'] == 2).astype(int)
print(passengers)

# Select the desired features
features = passengers[['Sex', 'Age', 'FirstClass', 'SecondClass']]
survival = passengers['Survived']

# Perform train, test, split
X_train, X_test, y_train, y_test = train_test_split(features, survival, test_size=0.3, random_state=42)

# Scale the feature data so it has mean = 0 and standard deviation = 1
# Create a StandardScaler object
scaler = StandardScaler()

# Fit and transform the training features
X_train_scaled = scaler.fit_transform(X_train)

# Transform the test features using the fitted scaler
X_test_scaled = scaler.transform(X_test)
model = LogisticRegression()
model.fit(X_train_scaled, y_train) 
y_pred = model.predict(X_train_scaled)

accuracy = model.score(X_test_scaled, y_test)
