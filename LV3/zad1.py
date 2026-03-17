import pandas as pd

dataSet = pd.read_csv("data_C02_emission.csv")

print(dataSet)

#a

#print(len(dataSet))

#print(dataSet.dtypes)

print(dataSet.isnull().sum())

dataSet.dropna(axis=0)
dataSet.dropna(axis=1)

dataSet.drop_duplicates()

dataSet = dataSet.reset_index(drop=True)

#b
dataSet = dataSet.sort_values(by=['Fuel Consumption City (L/100km)'], ascending=False)
print("Most consumption:")
print(dataSet.head(3)[['Make', 'Model', 'Fuel Consumption City (L/100km)']])
print("Least consumption:")
print(dataSet.tail(3)[['Make', 'Model', 'Fuel Consumption City (L/100km)']])

#c
motorSize = dataSet[(dataSet['Engine Size (L)'] >= 2.5) & (dataSet['Engine Size (L)'] <= 3.5)]

print(len(motorSize))
print(round(motorSize['CO2 Emissions (g/km)'].mean(), 2))

#d
audiData = dataSet[dataSet['Make'] == 'Audi']

print(len(audiData))
print(round(audiData[audiData['Cylinders'] == 4]['CO2 Emissions (g/km)'].mean(), 2))

#e
print(dataSet[dataSet['Cylinders'] % 2 == 0].groupby('Cylinders')['CO2 Emissions (g/km)'].size())
print(dataSet[dataSet['Cylinders'] % 2 == 0].groupby('Cylinders')['CO2 Emissions (g/km)'].mean())

#f
print(dataSet.groupby('Fuel Type')['Fuel Consumption City (L/100km)'].mean())
print(dataSet.groupby('Fuel Type')['Fuel Consumption City (L/100km)'].median())

#g
print("Most consuption:")
print(dataSet.iloc[dataSet[(dataSet['Cylinders'] == 4) & (dataSet['Fuel Type'] == 'D')]['Fuel Consumption City (L/100km)'].idxmax()])

#h
print(len(dataSet[dataSet['Transmission'].str[0] == 'M']))
print(dataSet.corr(numeric_only = True))