import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder
import sklearn.linear_model as lm
from sklearn.metrics import r2_score, mean_squared_error
import numpy as np

dataSet = pd.read_csv('data_C02_emission.csv')

input_columns = ["Engine Size (L)", 
                 "Cylinders", 
                 "Fuel Consumption Comb (L/100km)", 
                 "Fuel Consumption City (L/100km)", 
                 "Fuel Consumption Hwy (L/100km)",
                 "Fuel Type"]

output_column = "CO2 Emissions (g/km)"

ohe = OneHotEncoder(handle_unknown='ignore')
fuel_type_encoded = ohe.fit_transform(dataSet[['Fuel Type']]).toarray()

dataX_numeric = dataSet[input_columns[:-1]].values
dataX = np.hstack([dataX_numeric, fuel_type_encoded])
dataY = dataSet[output_column].values

X_train, X_test, y_train, y_test = train_test_split(dataX, dataY, test_size=0.2, random_state=1)

linearModel = lm.LinearRegression()
linearModel.fit(X_train, y_train)

y_test_p = linearModel.predict(X_test)

plt.scatter(y_test, y_test_p)

r2 = r2_score(y_test, y_test_p)
rmse = np.sqrt(mean_squared_error(y_test, y_test_p))
max_error = np.max(np.abs(y_test - y_test_p))

print(max_error)

maxErrorId = np.argmax(np.abs(y_test - y_test_p))
print(y_test[maxErrorId])

plt.show()