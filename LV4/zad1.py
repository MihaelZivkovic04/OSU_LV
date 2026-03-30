import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import OneHotEncoder
import sklearn.linear_model as lm
from sklearn.metrics import mean_absolute_error

dataSet = pd.read_csv('data_C02_emission.csv')

input_columns = ["Engine Size (L)", 
                 #"Cylinders", 
                 "Fuel Consumption Comb (L/100km)", 
                 "Fuel Consumption City (L/100km)", 
                 #"Fuel Consumption Hwy (L/100km)"
                 ]

output_column = "CO2 Emissions (g/km)"

dataX = dataSet[input_columns].values
dataY = dataSet[output_column].values

X_train , X_test , y_train , y_test = train_test_split (dataX, dataY, test_size = 0.2, random_state= 1)

plt.scatter(X_train[:, 1], y_train, color='blue')
plt.scatter(X_test[:, 1], y_test, color='red')

plt.figure()
plt.hist(X_train[:, 0], bins=30, color='blue')

#ohe = OneHotEncoder(handle_unknown='ignore')
#X_train = ohe.fit_transform(X_train[['Make','Model','Vehicle Class','Transmission','Fuel Type']]).toarray()
#X_test = ohe.transform(X_test[['Make','Model','Vehicle Class','Transmission','Fuel Type']]).toarray()

sc = MinMaxScaler()
X_train_n = sc.fit_transform(X_train)
X_test_n = sc.transform(X_test)

plt.figure()
plt.hist(X_train_n[:, 0], bins=30, color='red')

linearModel = lm.LinearRegression()
linearModel.fit(X_train_n, y_train)
print(linearModel.get_params())

y_test_p = linearModel.predict(X_test_n)
plt.scatter(x=y_test_p,
            y=y_test)

MAE = mean_absolute_error( y_test , y_test_p )

print(MAE)

plt.show()
