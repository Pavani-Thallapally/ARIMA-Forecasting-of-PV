#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pandas as pd
import numpy as np
import seaborn as sns
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import itertools


# In[3]:


import random


# In[4]:


pip install pmdarima


# In[5]:


df=pd.read_csv('D:/csv files of solar/20h.csv')


# In[6]:


df.head(10)


# In[7]:


df.tail()


# In[8]:


df.describe()


# In[9]:


df['Time'].plot()


# In[10]:


df.index = pd.to_datetime(df.index)


# In[11]:


df.set_index('Date', inplace = True)


# In[12]:


df.dropna(inplace=True)


# In[13]:


df.fillna(0)
df=df.fillna(df.bfill())


# In[14]:


from pmdarima.arima import ADFTest


# In[15]:


adf_test = ADFTest(alpha =0.05)
adf_test.should_diff(df)
df.fillna(value=0, inplace=True)


# In[16]:


from statsmodels.tsa.stattools import adfuller


# In[17]:


adf, pvalue, usedlag_, nobs_, critical_values_, icbest_ = adfuller(df)
print("pvalue=", pvalue, "if above 0.05, data is not stationary")


# In[18]:


from statsmodels.tsa.seasonal import seasonal_decompose


# In[19]:


decomposed = seasonal_decompose(df['Time'], model='additive', period=2)
trend = decomposed.trend
seasonal = decomposed.seasonal
residual = decomposed.resid


# In[20]:


plt.style.use('dark_background')


# In[21]:


plt.figure(figsize = (12,8))
plt.subplot(411)
plt.plot(df, label ='original', color= 'yellow')
plt.legend(loc='upper left')
plt.subplot(412)
plt.plot(trend, label ='trend', color= 'yellow')
plt.legend(loc='upper left')
plt.subplot(413)
plt.plot(seasonal, label ='seasonal', color= 'yellow')
plt.legend(loc='upper left')
plt.subplot(414)
plt.plot(residual, label ='residual', color= 'yellow')
plt.legend(loc='upper left')
plt.show()


# In[22]:


from pmdarima.arima import auto_arima


# In[23]:


# p,d,q represents non seasonal
#P,D,Q represents seasonal


# In[24]:


arima_model = auto_arima(df['Time'], start_p =1, d=1, start_q =1, max_q=5, max_d =5, m=6, start_P=0, D=1, start_Q=0, max_P=5, max_D=5, max_Q=5, seasonal=True, trace=True, error_action='ignore',suppress_warnings=True, stepwise=True, n_fits=50)


# In[25]:


# to print summary
print(arima_model.summary())


# In[26]:


#Model SARIMAX(0, 1, 1)x(0, 1, 1, 6)


# In[27]:


size = int(len(df)*0.66)
X_train, X_test = df[0:size], df[size:len(df)]


# In[28]:


from statsmodels.tsa.statespace.sarimax import SARIMAX


# In[29]:


import warnings
warnings.filterwarnings('ignore')


# In[30]:


model =SARIMAX(X_train['Time'], order = (0,1,1), seasonal_order = (0,1,1,6))


# In[31]:


result = model.fit()
result.summary()


# In[32]:


start_index = 0
end_index = len(X_train)-1
train_prediction = result.predict(start_index, end_index)


# In[33]:


start_index = len(X_train)
end_index = len(df)-1
prediction = result.predict(start_index, end_index).rename('predicted Time')


# In[34]:


prediction


# In[35]:


prediction.plot(legend=True)
X_test['Time'].plot(legend=True)


# In[36]:


import math
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_absolute_percentage_error


# In[37]:


trainScore = math.sqrt(mean_squared_error(X_train, train_prediction))
print('trainScore:% 2f RMSE'% (trainScore))
testScore = math.sqrt(mean_squared_error(X_test, prediction))
print('testScore:% 2f RMSE'% (testScore))


# In[38]:


# Calculate MAE for training set
train_mae = mean_absolute_error(X_train, train_prediction)
print('Train MAE: %.2f' % train_mae)
test_mae = mean_absolute_error(X_test, prediction)
print('Test MAE: %.2f' % test_mae)


# In[39]:


# Calculate MAPE for training set
train_mape = mean_absolute_percentage_error(X_train, train_prediction)
print('Train MAPE: %.2f' % train_mape)
test_mape = mean_absolute_percentage_error(X_test, prediction)
print('Test MAPE: %.2f' % test_mape)


# In[40]:


from sklearn.metrics import r2_score
score = r2_score(X_test, prediction)
print("R2 score is:", score)


# In[61]:


forecast1 = result.predict(start=len(df)-85, end = (len(df)-1)+1*12, tup = 'levels').rename('forecast1')


# In[42]:


forecast = result.predict(start=len(df)-30, end = (len(df)-1)+1*12, tup = 'levels').rename('forecast')


# In[62]:


forecast1


# In[44]:


forecast


# In[42]:


plt.figure(figsize=(12,8))
plt.plot(X_train, label = 'Training', color = 'green')
plt.plot(X_test, label = 'Test', color = 'yellow')
plt.plot(forecast, label='forecast', color = 'cyan')
plt.legend(loc='upper left')
plt.show()


# In[44]:


plt.figure(figsize=(12,8))
plt.plot(X_train, label = 'Training', color = 'green')
plt.plot(X_test, label = 'Test', color = 'yellow')
plt.plot(forecast1, label='forecast', color = 'cyan')
plt.legend(loc='upper left')
plt.show()

