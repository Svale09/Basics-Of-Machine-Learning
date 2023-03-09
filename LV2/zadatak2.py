import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('/Users/ivansvalina/Documents/Faks/LV2/data.csv', delimiter = ",", skiprows = 1 )
print(data)
print("Number of data inputs (people measured): " + str(data.shape))

height = data[:,1]
weight = data[:,2]

plt.scatter(height, weight, s = 1)
plt.show()
plt.scatter(data[::50,1], data[::50,2], s = 1)
plt.show()

minHeight = height.min()
maxHeight = height.max()
avgHeight = height.mean()

print("Min height recorded = ", + minHeight)
print("Max height recorded = ", + maxHeight)
print("Avg height = ", + avgHeight)

menIndex = data[:,0] == 1
menData = np.array()
print(menIndex)
for i in range (0,len(data)):
    if data[i,0] == 1:
        menData[i] = data[i]
print(menData)