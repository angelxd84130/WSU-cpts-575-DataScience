import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("TB_burden_age_sex_2019-09-19.csv")
data = data.groupby("age_group").mean()['best']
print(data)
plt.title("The relationship between age_group and best estimate")
plt.plot(data)
plt.xlabel("age_group")
plt.ylabel("best estimate")
plt.show()

