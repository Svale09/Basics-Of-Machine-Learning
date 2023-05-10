import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("/Users/ivansvalina/Documents/Faks/LV3/data_C02_emission.csv")

data["CO2 Emissions (g/km)"].plot(kind= "hist", bins= 20)

data["Fuel Type"] = data["Fuel Type"].astype("category") #za c argument u scatteru mora bit 1d array numerickih vrijednosti te se tu kategoricke vrijednosti prebacuju u neumericke, svakoj kategoriji
data["Fuel Type code"] = data["Fuel Type"].cat.codes #goriva dodajemo jednu numericku vrijednost
data.plot.scatter(x= "Fuel Consumption City (L/100km)", y="CO2 Emissions (g/km)", c="Fuel Type", cmap="Paired", s= 10)

data.boxplot(column=["Fuel Consumption Hwy (L/100km)"], by="Fuel Type")
plt.show()

byFuel = data.groupby("Fuel Type")["Make"].count()
byFuel.plot.bar(color="red")
plt.show()

average_emission=data.groupby('Cylinders')['CO2 Emissions (g/km)'].mean()
average_emission.plot.bar()
plt.show()