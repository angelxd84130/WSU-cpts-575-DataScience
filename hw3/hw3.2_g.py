import pandas as pd
data = pd.DataFrame({'Site': ['facebook', 'myspace', 'snapchat', 'twitter'],
                     'U30.F': [32, 1, 6, 17],
                     'U30.M': [31, 5, 4, 23],
                     'O30.F': [60, 3, 3, 12],
                     'O30.M': [58, 6, 2, 17]})

data = pd.melt(data, id_vars=['Site'], value_vars=list(data.columns)[1:], var_name='type',
               value_name='value')
data = data.drop('type', axis=1).join(data['type'].str.split('.', expand=True))
data.rename(columns={0:'type', 1:'sex'}, inplace=True)
data = pd.pivot_table(data, index=['Site', 'type'], columns = 'sex', values='value')

print(data)
