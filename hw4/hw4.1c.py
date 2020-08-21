import pandas as pd
import matplotlib.pyplot as plt
#from pandas.plotting import scatter_matrix
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

data = pd.read_csv("Auto.csv")
data1 = data.drop(columns=['name'])

for i in range(len(data1)):
    a = data1['horsepower'][i]
    if a == '?':
        data1 = data1.drop([i])

data1['horsepower'] = pd.to_numeric(data1['horsepower'])


X = data1['year'].values.reshape(-1, 1)
#Y = data1['cylinders'].values.reshape(-1,1)
Y = data1['origin'].values.reshape(-1,1)
#X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.4, random_state=1)
regr = LinearRegression()
regr.fit(X, Y)
y_pred = regr.predict(X)
print("year_origin")
print('Coefficients:', regr.coef_)
print('Mean squared error:', mean_squared_error(Y, y_pred))
print('Variance score:', r2_score(Y, y_pred))
plt.scatter(X, Y)
plt.plot(X, y_pred, color='red')
plt.xlabel('year')
plt.ylabel('origin')

#plt.show()
plt.savefig('year_origin.png')