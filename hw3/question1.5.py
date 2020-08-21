import pandas as pd
import numpy as np

data = pd.read_csv("msleep_ggplot2.csv")

#animal's order times animal's weight
data = data.assign(wt_ratio=data['brainwt']/data['bodywt'])

countBefore = 0
countAfter = 0

for index, row in data.iterrows():
    if np.isnan(row['brainwt']):
        countBefore += 1
        row['brainwt'] = data.groupby('order').mean().loc[row['order'], 'wt_ratio'] * row['bodywt']
        print(row['order'], row['brainwt'])
        if(np.isnan(row['brainwt'])):
            countAfter += 1

#print(data['brainwt'])
print('\nBefore:', countBefore, 'nans\n', 'After:', countAfter, 'nans')

'''
#the average brainwt for animal's order
countBefore = 0
countAfter = 0
#print(data['brainwt'])
for index, row in data.iterrows():
    if np.isnan(row['brainwt']):
        #print(row['order'], row['brainwt'])
        countBefore += 1
        row['brainwt'] = data.groupby('order').mean().loc[row['order'], 'brainwt']
        print(row['order'], row['brainwt'])
        if(np.isnan(row['brainwt'])):
            countAfter += 1

#print(data['brainwt'])
print('\nBefore:', countBefore, 'nans\n', 'After:', countAfter, 'nans')
#print(data.groupby('order').mean())
#print(data.groupby('order').mean().loc['Carnivora', 'brainwt'])
'''

