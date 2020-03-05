import random
import numpy as np
import csv
import matplotlib.pyplot as plt

xcoor = []
ycoor = []
with open("myData.txt", "r") as f:
	reader = csv.reader(f, delimiter=",")
	for row in reader:
		xcoor.append(row[0])
		ycoor.append(row[1])

#print("Test:\n")
for x in range(len(xcoor)):
	print (xcoor[x], ycoor[x])

xcoor = np.array(xcoor)
xcoor = xcoor.astype(np.float)

ycoor = np.array(ycoor)
ycoor = ycoor.astype(np.float)


x_mean = np.mean(xcoor)
y_mean = np.mean(ycoor)

xy_bar = np.mean(xcoor*ycoor)
x2 = np.mean(xcoor**2)


m = (y_mean - (xy_bar/x_mean))/(x_mean - (x2/x_mean))

b = y_mean - m*x_mean

#print("M and B:", m, b)

t = np.linspace(1000, 2500, 20)

plt.axis([1000,2500,195000, 410000])

plt.plot(xcoor,ycoor,"ro", t, m*t+ b, "b-")
plt.show()





