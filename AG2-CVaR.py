#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm


# In[2]:


df=pd.read_csv('C:/Users/pavan/OneDrive/Desktop/Var with uncertnity/AG2-Prof_New.csv')


# In[3]:


df.head()


# In[4]:


df.tail()


# In[5]:


df.describe()


# In[6]:


for column in df.columns:
    plt.plot(df.index, df[column], label=column)
# Add legend
plt.legend(labels=df.columns)


# In[7]:


# Obtain percentage change per stock
returns = df.pct_change().dropna()

# Calculate the portfolio returns as the weighted average of the individual asset returns
weights = np.full((5), 0.25) # assuming equal weight
port_returns = (weights * returns).sum(axis=1) # weighted sum


# In[8]:


returns


# In[9]:


# Filter out non-finite values from port_returns
port_returns_filtered = port_returns[np.isfinite(port_returns)]

# Calculate the range for the histogram based on the minimum and maximum values of port_returns
hist_range = (np.min(port_returns_filtered), np.max(port_returns_filtered))


# In[10]:


plt.hist(port_returns_filtered, bins=10, range=hist_range, density=True, alpha=0.5)
plt.xlabel("Portfolio Returns")
plt.ylabel("Density")
plt.title(f"Portfolio Percentage Returns")
plt.show()


# In[11]:


#Historical method
# Assume initial portfolio value
initial_portfolio = 100000


# In[12]:


# Obtain percentage change per stock
returns = df.pct_change()


# In[13]:


# Calculate the portfolio returns as the weighted average of the individual asset returns
weights = np.full((5), 0.1) # assuming equal weight
individual_port_returns = weights * returns  # Element-wise multiplication
port_returns = (weights * returns).sum(axis=1) # weighted sum


# In[14]:


# Calculate the portfolio's VaR at 95% confidence level
confidence_level = 0.95
# Calculate P(Return <= VAR) = alpha
var = port_returns.quantile(q=1-confidence_level)
# Calculate CVAR by computing the average returns below the VAR level
cvar = port_returns[port_returns <= var].mean()


# In[15]:


# Multiply the VaR and CVaR by the initial investment value to get the absolute value
var_value = var * initial_portfolio
cvar_value = cvar * initial_portfolio


# In[16]:


print(f"Historical VaR at {confidence_level} confidence level: {var_value:.2f} ({var:.2%})")
print(f"Historical CVaR at {confidence_level} confidence level: {cvar_value:.2f} ({cvar:.2%})")


# In[17]:


plt.hist(port_returns_filtered, bins=10, range=hist_range, density=True, alpha=0.5)
# Add VAR CVAR to the histogram
plt.axvline(x=var, color='red', linestyle='--', label=f"VaR: {var:.2%}")
plt.axvline(x=cvar, color='blue', linestyle='--', label=f"CVaR: {cvar:.2%}")

plt.legend()
plt.xlabel("Portfolio Returns")
plt.ylabel("Density")
plt.title(f"Portfolio Percentage Returns for 95% confidence interval")
plt.show()


# In[18]:


# Calculate actual losses
initial_portfolio_value = 1000000  # Example initial portfolio value
actual_losses = initial_portfolio_value * (1 + returns) - initial_portfolio_value


# In[19]:


# Compare with VaR estimates
var_violations = actual_losses < -var


# In[20]:


# Old behavior (deprecated)
mean_value = df.mean()


# In[21]:


# Updated behavior (to avoid FutureWarning)
mean_value = df.mean()  # Compute mean along the columns
import warnings
# Suppress FutureWarning
warnings.simplefilter(action='ignore', category=FutureWarning)


# In[22]:


# Calculate violation frequency
violation_frequency = np.mean(var_violations)


# In[23]:


selected_columns = ['Scen1', 'Scen2', 'Scen3', 'Scen4', 'Scen5']
series = df[selected_columns]


# In[24]:


# Display the selected columns
print(series)


# In[25]:


violation_frequency_scalar = violation_frequency.iloc[0]


# In[26]:


# Print violation frequency with percentage formatting
print(f"Violation Frequency: {violation_frequency_scalar:.2%}")


# In[27]:


# Calculate the portfolio's VaR at 90% confidence level
confidence_level = 0.90
# Calculate P(Return <= VAR) = alpha
var = port_returns.quantile(q=1-confidence_level)
# Calculate CVAR by computing the average returns below the VAR level
cvar = port_returns[port_returns <= var].mean()


# In[28]:


# Multiply the VaR and CVaR by the initial investment value to get the absolute value
var_value = var * initial_portfolio
cvar_value = cvar * initial_portfolio


# In[29]:


print(f"Historical VaR at {confidence_level} confidence level: {var_value:.2f} ({var:.2%})")
print(f"Historical CVaR at {confidence_level} confidence level: {cvar_value:.2f} ({cvar:.2%})")


# In[30]:


plt.hist(port_returns_filtered, bins=10, range=hist_range, density=True, alpha=1.0)
# Add VAR CVAR to the histogram
plt.axvline(x=var, color='red', linestyle='--', label=f"VaR: {var:.2%}")
plt.axvline(x=cvar, color='blue', linestyle='--', label=f"CVaR: {cvar:.2%}")

plt.legend()
plt.xlabel("Portfolio Returns")
plt.ylabel("Density")
plt.title(f"Portfolio Percentage Returns for 90%")
plt.show()


# In[31]:


# Calculate the portfolio's VaR at 98% confidence level
confidence_level = 0.98
# Calculate P(Return <= VAR) = alpha
var = port_returns.quantile(q=1-confidence_level)
# Calculate CVAR by computing the average returns below the VAR level
cvar = port_returns[port_returns <= var].mean()


# In[32]:


# Multiply the VaR and CVaR by the initial investment value to get the absolute value
var_value = var * initial_portfolio
cvar_value = cvar * initial_portfolio


# In[33]:


print(f"Historical VaR at {confidence_level} confidence level: {var_value:.2f} ({var:.2%})")
print(f"Historical CVaR at {confidence_level} confidence level: {cvar_value:.2f} ({cvar:.2%})")


# In[34]:


plt.hist(port_returns_filtered, bins=10, range=hist_range, density=True, alpha=0.2)
# Add VAR CVAR to the histogram
plt.axvline(x=var, color='red', linestyle='--', label=f"VaR: {var:.2%}")
plt.axvline(x=cvar, color='blue', linestyle='--', label=f"CVaR: {cvar:.2%}")
plt.legend()
plt.xlabel("Portfolio Returns")
plt.ylabel("Density")
plt.title(f"Portfolio Percentage Returns for 98%")
plt.show()


# In[35]:


import warnings

# Filter out the specific warning
warnings.filterwarnings("ignore", message="invalid value encountered in subtract")


# In[36]:


confidence_level = 0.95


# In[37]:


# Initialize a dictionary to store VaR values for each column
var_values = {}


# In[38]:


var_values = {}
# Loop through each column in the DataFrame
for column in df.columns:
    sorted_data = np.sort(df[column])
    var_index = int((1 - confidence_level) * len(sorted_data))
    var_values[column] = sorted_data[var_index]


# In[39]:


# Print VaR values for each column
for column, var in var_values.items():
    print(f"VaR for {column} at {confidence_level*100}% confidence level: {var}")


# In[40]:


sorted_data = np.sort(df)


# In[41]:


num_samples = len(sorted_data)


# In[42]:


cvar_index = int((1 - confidence_level) * num_samples)


# In[43]:


cvar = np.mean(sorted_data[:cvar_index])
# Print CVaR result
print(f"CVaR at {confidence_level*100}% confidence level: {cvar}")


# In[44]:


# Calculate CVaR for each column
cvar_values = {}
for column in df.columns:
    sorted_data = np.sort(df[column])
    cvar_index = int(confidence_level * len(sorted_data))
    cvar_values[column] = np.mean(sorted_data[:cvar_index])


# In[45]:


# Print CVaR values at confidence_level for each column
for column, cvar in cvar_values.items():
    print(f"CVaR for {column}: {cvar}") 


# In[46]:


confidence_level_1 = 0.98


# In[47]:


# Initialize a dictionary to store VaR values for each column
var_values1 = {}


# In[48]:


var_values1 = {}
# Loop through each column in the DataFrame
for column in df.columns:
    sorted_data = np.sort(df[column])
    var_index = int((1 - confidence_level_1) * len(sorted_data))
    var_values1[column] = sorted_data[var_index]


# In[49]:


# Print VaR values for each column
for column, var in var_values1.items():
    print(f"VaR for {column} at {confidence_level_1*100}% confidence level: {var}")


# In[50]:


sorted_data = np.sort(df)


# In[51]:


num_samples = len(sorted_data)


# In[52]:


cvar_index = int((1 - confidence_level_1) * num_samples)


# In[53]:


cvar = np.mean(sorted_data[:cvar_index])

# Print CVaR result
print(f"CVaR at {confidence_level_1*100}% confidence level: {cvar}")


# In[54]:


# Calculate CVaR for each column
cvar_values = {}
for column in df.columns:
    sorted_data = np.sort(df[column])
    cvar_index = int(confidence_level_1 * len(sorted_data))
    cvar_values[column] = np.mean(sorted_data[:cvar_index])


# In[55]:


# Print CVaR values at confidence_level for each column
for column, cvar in cvar_values.items():
    print(f"CVaR for {column}: {cvar}") 

