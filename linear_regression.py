# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OkhJnT4KrQ-t-GI5SKmgS8REAWR6I8UU
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def equation(X,theta): #theta is a vector
  y_predicted = theta[0] + theta[1]*X #theta[0] is intercept and theta[1] is intercept
  return y_predicted

def error(X,y,theta):
  n = X.shape[0]
  y_predicted = equation(X,theta)
  err = np.sum((y_predicted-y)**2)
  return err/n

def gradient(X,y,theta):
  n = X.shape[0]
  grad_desc = np.zeros(2,)
  y_predicted = equation(X,theta)
  grad_desc[0] = np.sum(y_predicted-y)
  grad_desc[1] = np.dot(X.T,y_predicted-y)#transpose of X is required for matrix multiplication
  return grad_desc/n

def gradient_descent(X,y,learning_rate=0.05,epoch=400):
  n = X.shape[0]
  theta = np.zeros(2,)#array of 2 elements viz. theta[0] and theta[1]
  for i in range(epoch):
    err = error(X,y,theta)
    grad_desc = gradient(X,y,theta)
    theta = theta - learning_rate*grad_desc
  return theta    
# Now we will access the data 
data = pd.read_csv('sample_data/mnist_test.csv')
data
X = data.iloc[:, 0] #considers the first column as X
y = data.iloc[:, 1] #considers the second column as y
X = np.array(X)
y = np.array(y)

mean_X = X.mean()    #to get a standardised value
standard_deviation_X = X.std()
X = (X-mean_X)/standard_deviation_X

plt.scatter(X,y)
theta = gradient_descent(X,y,learning_rate=0.05,epoch=100)

y_predicted = equation(X,theta)
plt.scatter(X,y)
plt.plot(X,y_predicted,c="green")
plt.show()
data
theta[0],theta[1]   #gives the value of intercept and slope

