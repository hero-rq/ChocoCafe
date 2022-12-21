import pandas as pd
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv('training_data.csv')

X = df[['open', 'high', 'low', 'volume']]
y = df['close']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)
print('Accuracy:', accuracy)

new_data = [[100, 105, 98, 1000]]
prediction = model.predict(new_data)
print('Prediction:', prediction)
