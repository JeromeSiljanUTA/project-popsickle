#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd
from d01_data.load_data import load_from_db
from statsmodels.graphics.tsaplots import plot_pacf, plot_acf
from statsmodels.tsa.arima.model import ARIMA
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


model = ARIMA(train_data, order=(24, 0, 0))
model_fit = model.fit()


# In[ ]:


model_fit.summary()

