import pandas as pd
import matplotlib.pyplot as plt

dataSet = pd.read_csv("data_C02_emission.csv")

dataSet["CO2 Emissions (g/km)"].plot(kind='hist', bins=10)

dataSet.plot.scatter(x='Fuel Consumption City (L/100km)',
                     y='CO2 Emissions (g/km)',
                     c='Fuel Type')

dataSet.boxplot(column=['Fuel Consumption Hwy (L/100km)'], by='Fuel Type')

fuel = dataSet.groupby('Fuel Type').size()
fuel.plot(kind='bar')

avgCO2 = dataSet.groupby('Cylinders')['CO2 Emissions (g/km)'].mean()
avgCO2.plot(kind='bar')

plt.show()