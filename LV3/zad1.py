#Zadatak 3.4.1 Skripta zadatak_1.py ucˇitava podatkovni skup iz data_C02_emission.csv. Dodajte programski kod u skriptu pomoc ́u kojeg možete odgovoriti na sljedec ́a pitanja:
#e) Koliko je vozila s 4,6,8. . . cilindara? Kolika je prosjecˇna emisija C02 plinova s obzirom na broj cilindara?
#f) Kolika je prosjecˇna gradska potrošnja u slucˇaju vozila koja koriste dizel, a kolika za vozila koja koriste regularni benzin? Koliko iznose medijalne vrijednosti?
#g) Koje vozilo s 4 cilindra koje koristi dizelski motor ima najvec ́u gradsku potrošnju goriva?
#h) Koliko ima vozila ima rucˇni tip mjenjacˇa (bez obzira na broj brzina)?
#i) Izracˇunajte korelaciju izmed ̄u numericˇkih velicˇina. Komentirajte dobiveni rezultat.
import pandas as pd

data = pd.read_csv('/Users/ivansvalina/Documents/Faks/LV3/data_C02_emission.csv')

#Koliko mjerenja sadrži DataFrame? Kojeg je tipa svaka velicˇina? Postoje li izostale ili duplicirane vrijednosti? Obrišite ih ako postoje. Kategoricˇke velicˇine konvertirajte u tip category

print(len(data))
print(data.dtypes)
print(data.duplicated())
if data.duplicated != 0:
    data.drop_duplicates()
    data.reset_index(drop= True)

data[['Make', 'Model', 'Vehicle Class', 'Transmission', 'Fuel Type']] = data[['Make', 'Model', 'Vehicle Class', 'Transmission', 'Fuel Type']].astype('category')
print('\n')

#Koja tri automobila ima najvec ́u odnosno najmanju gradsku potrošnju? Ispišite u terminal: ime proizvod ̄acˇa, model vozila i kolika je gradska potrošnja
print(data.dtypes)

CityConsumptionData = data.sort_values(by= 'Fuel Consumption City (L/100km)', ascending= False)
print(CityConsumptionData[['Make', 'Model', 'Fuel Consumption City (L/100km)']].head(3))
print('\n')

#Koliko vozila ima velicˇinu motora izmed ̄u 2.5 i 3.5 L? Kolika je prosjecˇna C02 emisija plinova za ova vozila?


cylinderData = data[(data.Cylinders >= 2.5) & (data.Cylinders <= 3.5)]
print(len(cylinderData))
print(data['CO2 Emissions (g/km)'].mean())
print('\n')

#"Koliko mjerenja se odnosi na vozila proizvod ̄acˇa Audi? Kolika je prosjecˇna emisija C02 plinova automobila proizvod ̄acˇa Audi koji imaju 4 cilindara?")
audiData = data[data.Make == 'Audi']
print(len(audiData))

meanC02 = audiData[audiData.Cylinders == 4]['CO2 Emissions (g/km)'].mean()
print(meanC02)
print("\n")

#Koliko je vozila s 4,6,8. . . cilindara? Kolika je prosjecˇna emisija C02 plinova s obzirom na broj cilindara?")
evenCylinderData = data[(data.Cylinders % 2) == 0]
print(len(evenCylinderData))

print(evenCylinderData[evenCylinderData.Cylinders == 4]['CO2 Emissions (g/km)'].mean())
print(evenCylinderData[evenCylinderData.Cylinders == 6]['CO2 Emissions (g/km)'].mean())
print(evenCylinderData[evenCylinderData.Cylinders == 8]['CO2 Emissions (g/km)'].mean())
print("\n")

#Kolika je prosjecˇna gradska potrošnja u slucˇaju vozila koja koriste dizel, a kolika za vozila koja koriste regularni benzin? Koliko iznose medijalne vrijednosti?')
print(data[data["Fuel Type"] == "D"]["Fuel Consumption City (L/100km)"].mean())
print(data[data["Fuel Type"] == "D"]["Fuel Consumption City (L/100km)"].median())
print(data[data["Fuel Type"] == "X"]["Fuel Consumption City (L/100km)"].mean())
print(data[data["Fuel Type"] == "X"]["Fuel Consumption City (L/100km)"].median())
print("\n")

#Koje vozilo s 4 cilindra koje koristi dizelski motor ima najvec ́u gradsku potrošnju goriva?")

temp = data[(data.Cylinders == 4) & (data["Fuel Type"] == "D")]
temp.sort_values(by= "Fuel Consumption City (L/100km)", ascending= False)
print(temp[["Make", "Model", "Fuel Consumption City (L/100km)"]].head(1))
print("\n")

#Koliko ima vozila ima rucˇni tip mjenjacˇa (bez obzira na broj brzina)?')

temp = data.Transmission == "M"
print(len(temp))

#Izracˇunajte korelaciju izmed ̄u numericˇkih velicˇina. Komentirajte dobiveni rezultat.")
print(data.corr(numeric_only=True))