import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.feature_selection import SelectKBest, chi2

import os
os.listdir('/kaggle/input')

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session
# 데이터 로드
df = pd.read_csv('../input/house-prices-advanced-regression-techniques/train.csv')
df_features = ['LotArea', 'OverallQual', 'YearBuilt', 'TotalBsmtSF', 'GrLivArea']
y = df.SalePrice
X = df[df_features]

# 특성 선택
selector = SelectKBest(chi2, k=5)
X = selector.fit_transform(X, y)

# 훈련 데이터와 테스트 데이터 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# 모델 훈련
house_model = DecisionTreeRegressor(random_state=1, max_depth=5, min_samples_split=10, min_samples_leaf=5)
house_model.fit(X_train, y_train)

# 테스트 데이터 예측
y_pred = house_model.predict(X_test)

# 예측 결과 평가
from sklearn.metrics import mean_squared_error

mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
print("RMSE:", rmse)

# 새로운 데이터 예측
new_data = pd.read_csv("../input/house-prices-advanced-regression-techniques/test.csv")
new_X = new_data[df_features]
new_X = new_X.fillna(new_X.mean())

new_predictions = house_model.predict(new_X)
print(new_predictions)

# 결과를 CSV 파일로 저장
submission = pd.DataFrame({'Id': new_data['Id'], 'SalePrice': new_predictions})
submission.to_csv('submission.csv', index=False)
