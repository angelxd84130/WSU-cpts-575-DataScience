import pandas as pd

data = pd.read_csv("msleep_ggplot2.csv")

#print(data.assign(wt_rotio=data['brainwt']/data['bodywt']).loc[:])
print(data.assign(wt_ratio=data['brainwt']/data['bodywt'], rem_ratio=data['sleep_rem']/data['sleep_total']))

