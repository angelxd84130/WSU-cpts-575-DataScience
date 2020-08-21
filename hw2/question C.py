import matplotlib.pyplot as plt
import csv
import statistics
mpg = []
cylinders = []
displacement = []
horsepower = []
weight = []
acceleration = []
year = []
count = 0

with open('Auto.csv', newline='') as csvfile:
    Auto = csv.reader(csvfile, quotechar='|')
    for row in Auto:
        if (count > 0 and count < 45) or (count > 85):
            mpg.append(float(row[0]))
            cylinders.append(int(row[1]))
            displacement.append(float(row[2]))
            if row[3]!='?':
                horsepower.append(int(row[3])) #some '?'
            weight.append(int(row[4]))
            acceleration.append((float(row[5])))
            year.append(int(row[6]))
        count += 1


print("Range of mpg: ", min(mpg), '~', max(mpg), '/ mean: ',
      sum(mpg)/len(mpg), '/ standard deviation: ', statistics.stdev(mpg))
print("Range of cylinders: ", min(cylinders), '~', max(cylinders), '/ mean: ',
      sum(cylinders)/len(cylinders), '/ standard deviation: ', statistics.stdev(cylinders))
print("Range of displacement: ", min(displacement), '~', max(displacement), '/ mean: ',
      sum(displacement)/len(displacement), '/ standard deviation: ', statistics.stdev(displacement))
print("Range of horsepower: ", min(horsepower), '~', max(horsepower), '/ mean: ',
      sum(horsepower)/len(horsepower), '/ standard deviation: ', statistics.stdev(horsepower))
print("Range of weight: ", min(weight), '~', max(weight), '/ mean: ',
      sum(weight)/len(weight), '/ standard deviation: ', statistics.stdev(weight))
print("Range of acceleration: ", min(acceleration), '~', max(acceleration), '/ mean: ',
      sum(acceleration)/len(acceleration), '/ standard deviation: ', statistics.stdev(acceleration))
print("Range of year: ", min(year), '~', max(year), '/ mean: ',
      sum(year)/len(year), '/ standard deviation: ', statistics.stdev(year))

