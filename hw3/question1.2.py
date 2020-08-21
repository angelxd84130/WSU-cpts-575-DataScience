import pandas as pd

data = pd.read_csv("msleep_ggplot2.csv")

print(data.sort_values(by=['sleep_total'], ascending=False).loc[:,
      ['name', 'order', 'sleep_total', 'bodywt']].head(5))

