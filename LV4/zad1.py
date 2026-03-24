import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import OneHotEncoder

dataSet = pd.read_csv('data_C02_emission.csv')

dataY = dataSet["CO2 Emissions (g/km)"]
dataX = dataSet.iloc[:, 0:-1]

X_train , X_test , y_train , y_test = train_test_split (dataX, dataY, test_size = 0.2, random_state= 1)

plt.scatter(X_train['Engine Size (L)'], y_train, color='blue')
plt.scatter(X_test['Engine Size (L)'], y_test, color='red')

plt.show()

ohe = OneHotEncoder(handle_unknown='ignore')
X_train = ohe.fit_transform(X_train[['Make','Model','Vehicle Class','Transmission','Fuel Type']]).toarray()
X_test = ohe.transform(X_test[['Make','Model','Vehicle Class','Transmission','Fuel Type']]).toarray()

sc = MinMaxScaler()
X_train_n = sc.fit_transform(X_train)
X_test_n = sc.transform(X_test)

plt.figure()
X_train['Fuel Consumption City (L/ 100km )'].plot(kind ='hist', bins = 20)
plt.show()