import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

train = pd.read_csv('/kaggle/input/spaceship-titanic/train.csv')
test = pd.read_csv('/kaggle/input/spaceship-titanic/test.csv')

print(train.shape)
print('_'*35)
print(train.dtypes)
print('_'*35)
print(train.head())

# Drop the missing values in the train dataset
df_train = pd.DataFrame(train)
df_train = df_train.dropna(axis=0, inplace=False)

le = LabelEncoder()
# Fit and transform the "Transported" column
df_train['Transported'] = le.fit_transform(df_train['Transported'])
# Use one-hot encoding on the columns with string values
df_train = pd.get_dummies(df_train, columns=['HomePlanet', 'CryoSleep', 'Cabin', 'Destination', 'VIP', 'Name'], prefix=['HomePlanet', 'CryoSleep', 'Cabin', 'Destination', 'VIP', 'Name'])

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df_train.drop('Transported', axis=1), df_train['Transported'], test_size=0.2)

# Train the model
gnb = GaussianNB()
gnb.fit(X_train, y_train)

# Predict the target
y_pred = gnb.predict(X_test)
print(y_pred)

from sklearn.metrics import confusion_matrix

# Create a confusion matrix
cm = confusion_matrix(y_test, y_pred)
print('Confusion Matrix: \n', cm)
