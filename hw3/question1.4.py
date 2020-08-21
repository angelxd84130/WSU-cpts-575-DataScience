import pandas as pd

data = pd.read_csv("msleep_ggplot2.csv")

print(data.groupby('order').agg({'sleep_total': ['mean', 'min', 'max']}))

