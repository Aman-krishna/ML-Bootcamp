# -*- coding: utf-8 -*-
"""Logistic_Reg.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18RBv9Gzms_NZ9j4SWekyYuBFsnKJq-kk
"""

import pandas as pd
import numpy as np

def equation(X,theta):
  z = np.dot(X,theta)
  y_predicted = sigmoid(X)
  return y_predicted

def sigmoid(z):
  return 1/(1+np.exp(-z))

def error(X,theta,y):
  n = X.shape[0]
  y_predicted = equation(X,theta)
  err = np.dot(-y,np.log(y_predicted)) - np.dot((1-y),np.log(1-y_predicted))
  return err/n

def gradient(X,theta,y):
  y_predicted = equation(X,theta)
  n = X.shape[0]
  grad = np.dot(X.T,y_predicted)
  return grad/n
  
def gradient_descent(X,y,learning_rate = 0.05,epochs = 200):
  m,n = X.shape
  theta = np.zeros(n,)   # elements in theta represents number of characteristics 
  for i in range(epochs):
    grad = gradient(X,theta,y)
    theta = theta - learning_rate*grad
  return theta

data = pd.read_csv('sample_data/mnist_train_small.csv')
y = data.iloc[:,0]
X = data.iloc[:,1:]
X = np.array(X)
y = np.array(y)
theta = gradient_descent(X,y,learning_rate=0.05,epochs=200)
y_predicted = equation(X,theta)
y_predicted[y_predicted >= 0.5] = 1
y_predicted[y_predicted < 0.5] = 0

y_predicted,error(X,theta,y)



