import pandas as pd 

data = {
  '이름' : ['쿠키', '판다', '펭귄', '사나', '나연', '모모'],
  '특기' : ['춤', '노래', '예능', '물고기', '헤엄', '비행'],
  '음식' : ['피자', '알파고', '문장', '아다곤예', '엘리너', '큐밥'],
  '쏘죠' : ['12', '24', '25', '15', '26', '47']
}
df = pd.DataFrame(data)
df = pd.DataFrame(data, index=['1번', '2번', '3번', '4번', '5번', '6번'])
df.index.name = 'num'
print(df)
df.to_csv('anagonye.csv')

print('\n***********************\n')
al = pd.read_csv('anagonye.csv')
print(al['쏘죠'].describe())
print('\n')
print('쏘죠 minimum = ', al['쏘죠'].min())
print('쏘죠 maximum = ', al['쏘죠'].max())
