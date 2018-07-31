import pandas as pd

df=pd.read_csv('test.csv')
print('[non options]')
print(df)
print(df.dtypes)
print('')

df=pd.read_csv('test.csv', parse_dates=['date'])
print('[add parse_dates options]')
print(df)
print(df.dtypes)
