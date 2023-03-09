import numpy as np
import matplotlib.pyplot as plt

a = np.array([1, 3, 3, 2, 1])
b = np.array([1, 1, 2, 2, 1])
plt.plot(a,b, "r", linewidth  = 0.75, markersize = 5, marker = "1")
plt.axis([0,4,0,4])
plt.xlabel("x os")
plt.ylabel("y os")
plt.show()