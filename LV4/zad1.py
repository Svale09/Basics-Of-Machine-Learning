import sklearn as sk
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
import numpy

data = pd.read_csv('/Users/ivansvalina/Documents/Faks/LV3/data_C02_emission.csv')

data = data.drop(["Make", "Model"], axis = 1)

input_variables = ["Fuel Consumption City (L/100km)",
                   "Fuel Consumption Hwy (L/100km)",
                   "Fuel Consumption Comb (L/100km)",
                   "Fuel Consumption Comb (mpg)",
                   "Engine Size (L)",
                   "Cylinders"]

output_variable = ["CO2 Emissions (g/km)"]

x = data[input_variables].to_numpy()
y = data[output_variable].to_numpy()

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 1)

for i in range (0, 5):
    plt.scatter(X_train[:,i], y_train, s= 1, c= "blue")
    plt.scatter(X_test[:,i], y_test, s=1, c= "red")
    plt.xlabel("input variable")
    plt.ylabel("CO2 Emission (g/km)")
    plt.legend()
    plt.show()
