import matplotlib.pyplot as plt
import csv
#from sklearn.model_selection import train_test_split
#from sklearn.linear_model import LinearRegression

mpg = []
cylinders = []
displacement = []
horsepower = []
weight = []
acceleration = []
year = []
origin = []
count = 0
countHorse = 0
with open('Auto.csv', newline='') as csvfile:
    Auto = csv.reader(csvfile, quotechar='|')
    for row in Auto:
        if count > 0:
            mpg.append(float(row[0]))
            cylinders.append(int(row[1]))
            displacement.append(float(row[2]))
            if row[3]!='?':
                horsepower.append(int(row[3])) #some ?
                countHorse += 1
            weight.append(int(row[4]))
            acceleration.append((float(row[5])))
            year.append(int(row[6]))
            origin.append(int(row[7]))
        count += 1

plt.title("cylinders v.s. weight")
plt.scatter(cylinders, weight, color="red")
#linearRegressor = LinearRegression()
#linearRegressor.fit(cylinders, weight)
#plt.plot(cylinders, linearRegressor.predict(cylinders), color="blue")
plt.xlabel("cylinders")
plt.ylabel("weight")
plt.show()
