import pandas as pd 
import numpy as np

data = pd.read_csv('/Users/ivansvalina/Documents/Faks/LV3/data_C02_emission.csv')

print(len(data))
print(data.head(10))
print(data.info())
print(data.describe())