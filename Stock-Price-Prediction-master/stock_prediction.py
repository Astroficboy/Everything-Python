from sklearn.svm import SVR
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Style
plt.style.use('fivethirtyeight')

#Iterate through csv file
data  = pd.read_csv('anyfile.csv')

actual_price = data.tail(1)


#prepare data for training
#Get all the data
data = data.head(len(data)-1)


#create empty list to store the independent and dependent data
days=list()
adj_close_prices = list()


#get the date and adjusted close prices
data = data.loc[:, 'any_column']
data = data.loc[:, 'any_column']


#create the independent data set
for day in data_days:
    days.append([int(day.split('-')[1])])
#create the dependent data set
for adj_close_price in data_any_column:
    adj_close_prices.append([float(adj_close_price)])

#create the 3 support vector regression models
#create and train a support vector regression model using a linear kernel
lin_svr = SVR(kernel= 'linear', C=1000.0)
lin_svr.fit(days, adj_close_prices)

#create and train a support vector regression model using a polynomial kernel
poly = SVR(kernel= 'poly', C=1000.0, degree = 2)
poly.fit(days, adj_close_prices)

#create and train a support vector regression model using a rbf kernel
rbf = SVR(kernel= 'rbf', C=1000.0, gamma = 0.15)
rbf.fit(days, adj_close_prices)


plt.figure(figsize=(16, 8))
plt.scatter(days, adj_close_prices, color='red', label='Data')
plt.plot(days, rbf.predict(days), color = 'green', label='RBF Model')
plt.plot(days, poly.predict(days), color = 'blue', label='Polynomial Model')
plt.plot(days, lin_svr.predict(days), color = 'm', label='Linear Model')
plt.legend()


#predict
day = [[31]]
print('The RBF SVR predicted: ', rbf.predict(day))
print('The Polynomial SVR predicted: ', poly.predict(day))
print('The Linear SVR predicted: ', lin_svr.predict(day))
print('The actual price: ', actual_price['Adj Close'][21])
