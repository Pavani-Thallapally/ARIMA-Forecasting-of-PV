#!/usr/bin/env python
# coding: utf-8

# In[40]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm


# In[41]:


df=pd.read_csv('C:/Users/pavan/OneDrive/Desktop/Var with uncertnity/AG1-Prof_New.csv')


# In[42]:


df.head()


# In[43]:


df.tail()


# In[44]:


df.describe()


# In[45]:


for column in df.columns:
    plt.plot(df.index, df[column], label=column)
# Add legend
plt.legend(labels=df.columns)


# In[46]:


ax = df['Scen1'].pct_change().plot(kind='hist')
ax.set_title("Scen1 Percentage Change Histogram")


# In[47]:


ax = df['Scen2'].pct_change().plot(kind='hist')
ax.set_title("Scen2 Percentage Change Histogram")


# In[48]:


ax = df['Scen3'].pct_change().plot(kind='hist')
ax.set_title("Scen3 Percentage Change Histogram")


# In[49]:


ax = df['Scen4'].pct_change().plot(kind='hist')
ax.set_title("Scen4 Percentage Change Histogram")


# In[50]:


# Obtain percentage change per stock
returns = df.pct_change().dropna()

# Calculate the portfolio returns as the weighted average of the individual asset returns
weights = np.full((5), 0.25) # assuming equal weight
port_returns = (weights * returns).sum(axis=1) # weighted sum


# In[51]:


returns


# In[52]:


# Filter out non-finite values from port_returns
port_returns_filtered = port_returns[np.isfinite(port_returns)]

# Calculate the range for the histogram based on the minimum and maximum values of port_returns
hist_range = (np.min(port_returns_filtered), np.max(port_returns_filtered))


# In[53]:


plt.hist(port_returns_filtered, bins=10, range=hist_range, density=True, alpha=0.5)
plt.xlabel("Portfolio Returns")
plt.ylabel("Density")
plt.title(f"Portfolio Percentage Returns")
plt.show()


# In[54]:


#Historical method
# Assume initial portfolio value
initial_portfolio = 100000


# In[55]:


# Obtain percentage change per stock
returns = df.pct_change()


# In[56]:


# Calculate the portfolio returns as the weighted average of the individual asset returns
weights = np.full((5), 0.1) # assuming equal weight
individual_port_returns = weights * returns  # Element-wise multiplication
port_returns = (weights * returns).sum(axis=1) # weighted sum


# In[57]:


# Calculate the portfolio's VaR at 95% confidence level
confidence_level = 0.95
# Calculate P(Return <= VAR) = alpha
var = port_returns.quantile(q=1-confidence_level)
# Calculate CVAR by computing the average returns below the VAR level
cvar = port_returns[port_returns <= var].mean()


# In[58]:


# Multiply the VaR and CVaR by the initial investment value to get the absolute value
var_value = var * initial_portfolio
cvar_value = cvar * initial_portfolio


# In[59]:


print(f"Historical VaR at {confidence_level} confidence level: {var_value:.2f} ({var:.2%})")
print(f"Historical CVaR at {confidence_level} confidence level: {cvar_value:.2f} ({cvar:.2%})")


# In[60]:


plt.hist(port_returns_filtered, bins=10, range=hist_range, density=True, alpha=0.5)
# Add VAR CVAR to the histogram
plt.axvline(x=var, color='red', linestyle='--', label=f"VaR: {var:.2%}")
plt.axvline(x=cvar, color='blue', linestyle='--', label=f"CVaR: {cvar:.2%}")

plt.legend()
plt.xlabel("Portfolio Returns")
plt.ylabel("Density")
plt.title(f"Portfolio Percentage Returns for 95% confidence interval")
plt.show()


# In[61]:


# Calculate actual losses
initial_portfolio_value = 1000000  # Example initial portfolio value
actual_losses = initial_portfolio_value * (1 + returns) - initial_portfolio_value


# In[62]:


# Compare with VaR estimates
var_violations = actual_losses < -var


# In[63]:


# Old behavior (deprecated)
mean_value = df.mean()


# In[64]:


# Updated behavior (to avoid FutureWarning)
mean_value = df.mean()  # Compute mean along the columns
import warnings
# Suppress FutureWarning
warnings.simplefilter(action='ignore', category=FutureWarning)


# In[65]:


# Calculate violation frequency
violation_frequency = np.mean(var_violations)


# In[66]:


selected_columns = ['Scen1', 'Scen2', 'Scen3', 'Scen4', 'Scen5']
series = df[selected_columns]


# In[67]:


# Display the selected columns
print(series)


# In[68]:


violation_frequency_scalar = violation_frequency.iloc[0]


# In[69]:


# Print violation frequency with percentage formatting
print(f"Violation Frequency: {violation_frequency_scalar:.2%}")


# In[70]:


# Calculate the portfolio's VaR at 90% confidence level
confidence_level = 0.90
# Calculate P(Return <= VAR) = alpha
var = port_returns.quantile(q=1-confidence_level)
# Calculate CVAR by computing the average returns below the VAR level
cvar = port_returns[port_returns <= var].mean()


# In[71]:


# Multiply the VaR and CVaR by the initial investment value to get the absolute value
var_value = var * initial_portfolio
cvar_value = cvar * initial_portfolio


# In[72]:


print(f"Historical VaR at {confidence_level} confidence level: {var_value:.2f} ({var:.2%})")
print(f"Historical CVaR at {confidence_level} confidence level: {cvar_value:.2f} ({cvar:.2%})")


# In[73]:


plt.hist(port_returns_filtered, bins=10, range=hist_range, density=True, alpha=1.0)
# Add VAR CVAR to the histogram
plt.axvline(x=var, color='red', linestyle='--', label=f"VaR: {var:.2%}")
plt.axvline(x=cvar, color='blue', linestyle='--', label=f"CVaR: {cvar:.2%}")

plt.legend()
plt.xlabel("Portfolio Returns")
plt.ylabel("Density")
plt.title(f"Portfolio Percentage Returns for 90%")
plt.show()


# In[74]:


# Calculate the portfolio's VaR at 98% confidence level
confidence_level = 0.98
# Calculate P(Return <= VAR) = alpha
var = port_returns.quantile(q=1-confidence_level)
# Calculate CVAR by computing the average returns below the VAR level
cvar = port_returns[port_returns <= var].mean()


# In[75]:


# Multiply the VaR and CVaR by the initial investment value to get the absolute value
var_value = var * initial_portfolio
cvar_value = cvar * initial_portfolio


# In[76]:


print(f"Historical VaR at {confidence_level} confidence level: {var_value:.2f} ({var:.2%})")
print(f"Historical CVaR at {confidence_level} confidence level: {cvar_value:.2f} ({cvar:.2%})")


# In[77]:


plt.hist(port_returns_filtered, bins=10, range=hist_range, density=True, alpha=0.2)
# Add VAR CVAR to the histogram
plt.axvline(x=var, color='red', linestyle='--', label=f"VaR: {var:.2%}")
plt.axvline(x=cvar, color='blue', linestyle='--', label=f"CVaR: {cvar:.2%}")
plt.legend()
plt.xlabel("Portfolio Returns")
plt.ylabel("Density")
plt.title(f"Portfolio Percentage Returns for 98%")
plt.show()


# In[78]:


import warnings

# Filter out the specific warning
warnings.filterwarnings("ignore", message="invalid value encountered in subtract")


# In[79]:


confidence_level = 0.95


# In[80]:


# Initialize a dictionary to store VaR values for each column
var_values = {}


# In[81]:


var_values = {}
# Loop through each column in the DataFrame
for column in df.columns:
    sorted_data = np.sort(df[column])
    var_index = int((1 - confidence_level) * len(sorted_data))
    var_values[column] = sorted_data[var_index]


# In[82]:


# Print VaR values for each column
for column, var in var_values.items():
    print(f"VaR for {column} at {confidence_level*100}% confidence level: {var}")


# In[83]:


sorted_data = np.sort(df)


# In[84]:


num_samples = len(sorted_data)


# In[85]:


cvar_index = int((1 - confidence_level) * num_samples)


# In[86]:


cvar = np.mean(sorted_data[:cvar_index])

# Print CVaR result
print(f"CVaR at {confidence_level*100}% confidence level: {cvar}")


# In[87]:


# Calculate CVaR for each column
cvar_values = {}
for column in df.columns:
    sorted_data = np.sort(df[column])
    cvar_index = int(confidence_level * len(sorted_data))
    cvar_values[column] = np.mean(sorted_data[:cvar_index])


# In[88]:


# Print CVaR values at confidence_level for each column
for column, cvar in cvar_values.items():
    print(f"CVaR for {column}: {cvar}")


# In[89]:


confidence_level_1 = 0.98


# In[90]:


# Initialize a dictionary to store VaR values for each column
var_values1 = {}


# In[109]:


# Print VaR values for each column
for column, var in var_values1.items():
    print(f"VaR for {column} at {confidence_level_1*100}% confidence level: {var}")


# In[102]:


var_values1 = {}
# Loop through each column in the DataFrame
for column in df.columns:
    sorted_data = np.sort(df[column])
    var_index = int((1 - confidence_level_1) * len(sorted_data))
    var_values1[column] = sorted_data[var_index]


# In[103]:


sorted_data = np.sort(df)


# In[104]:


num_samples = len(sorted_data)


# In[105]:


cvar_index = int((1 - confidence_level_1) * num_samples)


# In[106]:


cvar = np.mean(sorted_data[:cvar_index])

# Print CVaR result
print(f"CVaR at {confidence_level_1*100}% confidence level: {cvar}")


# In[107]:


# Print CVaR values for each column
for column, cvar in cvar_values.items():
    print(f"CVaR for {column}: {cvar}")


# In[108]:


#Calculate mean column-wise
mean_columns = np.mean(df, axis=0)


# In[99]:


print("Mean of each column:")
print(mean_columns)


# In[ ]:




