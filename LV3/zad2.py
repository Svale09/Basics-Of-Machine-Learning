import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("/Users/ivansvalina/Documents/Faks/LV3/data_C02_emission.csv")

data["CO2 Emissions (g/km)"].plot(kind= "hist", bins= 20)
plt.show()
