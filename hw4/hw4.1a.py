import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
#import numpy as np

data = pd.read_csv("Auto.csv")
data1 = data.drop(columns=['origin', 'name'])

for i in range(len(data1)):
    a = data1['horsepower'][i]
    if a == '?':
        data1 = data1.drop([i])

data1['horsepower'] = pd.to_numeric(data1['horsepower'])

scatter_matrix(data1, alpha=0.7, figsize=(10,10))
#plt.show()

plt.savefig('a.png')
plt.close()
