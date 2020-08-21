import pandas as pd

data = pd.read_csv("Auto.csv")
data1 = data.drop(columns=['name'])

for i in range(len(data1)):
    a = data1['horsepower'][i]
    if a == '?':
        data1 = data1.drop([i])

data1['horsepower'] = pd.to_numeric(data1['horsepower'])
pd.set_option('display.max_columns', None)
print(data1.corr(method='pearson'))

