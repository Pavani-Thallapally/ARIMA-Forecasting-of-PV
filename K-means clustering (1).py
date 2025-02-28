#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import pandas as pd
import seaborn as sns


# In[3]:


df = pd.read_csv('C:/Users/pavan/OneDrive/Desktop/Var with uncertnity/PV-forecast-kmeans.csv')


# In[4]:


df.isna().sum()


# In[5]:


df.head()


# In[6]:


df.shape


# In[7]:


df.describe()


# In[8]:


print("The shape of data is", df.shape)


# In[9]:


df.tail()


# In[10]:


# Calculate probability for each column
column_probabilities = {}
total_rows = len(df)


# In[11]:


for column in df.columns:
       value_counts = df[column].value_counts()


# In[12]:


# Calculate probability of each unique value
probabilities = value_counts / total_rows


# In[13]:


# Store probabilities for the column
column_probabilities[column] = probabilities


# In[14]:


# Print probabilities for each column
for column, probabilities in column_probabilities.items():
    print(f"Probabilities for column {column}")
    print(probabilities)
    print()


# In[15]:


print(probabilities)
print()


# In[16]:


# Sample a subset of scenarios
sampled_data = df.sample(n=5, replace=False)


# In[17]:


# Optionally, you can export the sampled data to a new CSV file
sampled_data.to_csv('sampled_dataset.csv', index=False)


# In[18]:


#Reduced Scenarios
sampled_data


# In[19]:


from openpyxl import Workbook


# In[20]:


# Create a new Excel workbook
wb = Workbook()


# In[21]:


# Create a new worksheet
ws = wb.active


# In[22]:


# Your print output
print_output = sampled_data


# In[23]:


# Save the Excel file
wb.save('print_output.xlsx')


# In[24]:


#Reduced Scenarios for wind plant


# In[25]:


df1 = pd.read_csv('C:/Users/pavan/OneDrive/Desktop/Var with uncertnity/WT-Forecast-kmeans.csv')


# In[26]:


df1.isna().sum()


# In[27]:


df1.head()


# In[28]:


print("The shape of data is", df1.shape)


# In[29]:


df1.tail()


# In[30]:


# Calculate probability for each column
column_probabilities = {}
total_rows = len(df1)


# In[31]:


for column in df1.columns:
       value_counts = df1[column].value_counts()


# In[32]:


# Calculate probability of each unique value
probabilities = value_counts / total_rows


# In[33]:


# Store probabilities for the column
column_probabilities[column] = probabilities


# In[34]:


# Print probabilities for each column
for column, probabilities in column_probabilities.items():
    print(f"Probabilities for column {column}")
    print(probabilities)
    print()


# In[35]:


# Sample a subset of scenarios
sampled_data1 = df1.sample(n=10, replace=False)


# In[36]:


# Optionally, you can export the sampled data to a new CSV file
sampled_data1.to_csv('sampled_dataset.csv', index=False)


# In[37]:


#Reduced Scenarios
sampled_data1


# In[ ]:





# In[ ]:





# In[ ]:





# In[45]:


import matplotlib.pyplot as plt


# In[103]:


x=df.iloc[:,[3,4,5,6]].values


# In[104]:


from sklearn.cluster import KMeans


# In[105]:


wcss=[]


# In[ ]:


for i in range(1,11)
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




