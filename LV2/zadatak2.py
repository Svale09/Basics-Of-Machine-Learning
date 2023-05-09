import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('/Users/ivansvalina/Documents/Faks/LV2/data.csv', delimiter = ",", skiprows = 1 )
print(data)
print("Number of data inputs (people measured): " + str(data.shape))

height = data[:,1]
weight = data[:,2]

# plt.scatter(height, weight, s = 1)
# plt.show()
# plt.scatter(data[::50,1], data[::50,2], s = 1)
# plt.show()

# minHeight = height.min()
# maxHeight = height.max()
# avgHeight = height.mean()

# print("Min height recorded = ", + minHeight)
# print("Max height recorded = ", + maxHeight)
# print("Avg height = ", + avgHeight)

men = (data[:,0] == 1)
female = (data[:,0] == 0)

print(men)
print(min(data[men,1])) #kako ovo radi [men,1], men je lista koja sadrži je li index polja male ili ne znaci true false polje
print(max(data[men,1]))


