
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
os.listdir('/kaggle/input')

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session

df = pd.read_csv('../input/house-prices-advanced-regression-techniques/train.csv')
#print(df.head())
df_features = ['LotArea', 'OverallQual', 'YearBuilt', 'TotalBsmtSF', 'GrLivArea', 'GarageCars']
y = df.SalePrice

df_features =['LotArea', 'OverallQual', 'YearBuilt', 'TotalBsmtSF', 'GrLivArea', 'GarageCars']
X = df[df_features]
X.describe()

from sklearn.tree import DecisionTreeRegressor

house_model = DecisionTreeRegressor(random_state=1)

house_model.fit(X, y)
print(X.head())
print(house_model.predict(X.head()))
print('############################')
print(y.head())
