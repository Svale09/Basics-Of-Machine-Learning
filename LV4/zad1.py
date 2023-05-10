from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd
import matplotlib.pyplot as plt
import sklearn.linear_model as lm
import sklearn
import math
from sklearn.metrics import mean_absolute_error

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

# for i in range (0, 5):
#    plt.scatter(X_train[:,i], y_train, s= 1, c= "blue")
#    plt.scatter(X_test[:,i], y_test, s=1, c= "red")
#    plt.xlabel("input variable")
#    plt.ylabel("CO2 Emission (g/km)")
#    plt.show()

# plt.hist(X_train[:,0])
# plt.show()

scaler = StandardScaler()
X_train_n = scaler.fit_transform(X_train)
y_train_n = scaler.fit_transform(y_train)

# plt.hist(X_train_n[:,0])
# plt.show()

# Izgradite linearni regresijski modeli. Ispišite u terminal dobivene parametre modela i povežite ih s izrazom 4.6.
linearModel = lm.LinearRegression()
linearModel.fit(X_train_n, y_train)

print("Coeffs: ", linearModel.coef_)
print("Intercept: ", linearModel.intercept_)

#Izvršite procjenu izlazne velicˇine na temelju ulaznih velicˇina skupa za testiranje. Prikažite pomoc ́u dijagrama raspršenja odnos izmed ̄u stvarnih vrijednosti izlazne 
#velicˇine i procjene dobivene modelom.

y_test_predicted = linearModel.predict(X_test)
MAE = mean_absolute_error(y_test,y_test_predicted)
print(MAE)
# plt.scatter(x=X_test[:,0], y=y_test, c="red", s=10)
# plt.scatter(x=X_test[:,0], y=y_test_predicted, c="blue", s= 10)
# plt.show()

#Izvršite vrednovanje modela na nacˇin da izracˇunate vrijednosti regresijskih metrika na skupu podataka za testiranje.
MAE =sklearn.metrics.mean_absolute_error( y_test , y_test_predicted )
print("Vrednjovanje modela MAE:",MAE)
MSE=sklearn.metrics.mean_squared_error(y_test,y_test_predicted)
print("Vrednjovanje modela MSE:",MSE)
RMSE=math.sqrt(MSE)
print("Vrednjovanje modela RMSE:",RMSE)
MAPE=sklearn.metrics.mean_absolute_percentage_error(y_test,y_test_predicted)
print("Vrednjovanje modela MAPE:",MAPE)
R2=sklearn.metrics.r2_score(y_test,y_test_predicted)
print("Vrednjovanje modela R2:",R2)

#G. Što se dogada s vrijednostima evaluacijskih metrika na testnom skupu kada mijenjate broj ulaznih velicina?

X_train,X_test,y_train,y_test=train_test_split(x,y,test_size = 0.4,random_state=1)

ss = StandardScaler()
X_train_n=ss.fit_transform(X_train)
X_test_n=ss.transform(X_test)

linModel = lm.LinearRegression()
linModel.fit(X_train_n,y_train)
print(linModel.coef_)

y_test_p=linModel.predict(X_test_n)

MAE=sklearn.metrics.mean_absolute_error(y_test,y_test_p)
MSE=sklearn.metrics.mean_squared_error(y_test,y_test_p)
RMSE=math.sqrt(MSE)
MAPE=sklearn.metrics.mean_absolute_percentage_error(y_test,y_test_p)
R2=sklearn.metrics.r2_score(y_test,y_test_p)

print("Vrednovanje metrika nakon promjene broja ulaznih velicina")
print('MAE:',MAE)
print('MSE:',MSE)
print('RMSE:',RMSE)
print('MAPE:',MAPE)
print('R2:',R2)

plt.show()
