import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
from scipy import stats

data = pd.read_csv("Auto.csv")
data1 = data.drop(columns=['name'])

for i in range(len(data1)):
    a = data1['horsepower'][i]
    if a == '?':
        data1 = data1.drop([i])

data1['horsepower'] = pd.to_numeric(data1['horsepower'])

X = data1.drop(columns=['mpg'])
Y = data1['mpg']
x2 = sm.add_constant(X)
est = sm.OLS(Y, x2)
est2 = est.fit()
print(est2.summary())

