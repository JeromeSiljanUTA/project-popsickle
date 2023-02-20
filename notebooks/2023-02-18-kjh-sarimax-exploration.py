#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pickle
import matplotlib.pyplot as plt
import pandas as pd
import pmdarima as pm
from d01_data.load_data import load_from_db
from statsmodels.graphics.tsaplots import plot_pacf, plot_acf
from statsmodels.tsa.statespace.sarimax import SARIMAX
import datetime as dt


# In[2]:


POWER_DATA=1
power_df = load_from_db(POWER_DATA, notebook=True)
power_df.set_index("Time", inplace=True)


# In[3]:


ercot = power_df["ERCOT"]
plt.plot(ercot)


# In[4]:


plot_pacf(ercot)
plt.show()


# In[5]:


plot_acf(ercot)
plt.show()


# In[15]:


train_end = dt.datetime(2021,1,1)

train_data = ercot['2003':'2021'].asfreq('h')
test_data = ercot['2022'].asfreq('h')
plt.plot(train_data)
plt.show()


# In[7]:


plt.plot(test_data)
plt.show()


# In[ ]:


train_data.dropna(inplace=True)
stepwise_fit = pm.auto_arima(train_data, start_p=1, d=1, start_q=1, max_p=7, 
        max_q=7, m=7, seasonal=True, stationary=False, information_criterion='aic', 
        stepwise=False, sippress_warnings=True).to_dict()

model = SARIMAX(train_data, order=stepwise_fit['order'], seasonal_order=stepwise_fit['seasonal_order'])
model_fit = model.fit()


# In[ ]:


model_fit.summary()


# In[ ]:
with open('sarimax_1_0_0.obj', 'wb') as handle:
        pickle.dump(model_fit, handle, protocol=pickle.HIGHEST_PROTOCOL)