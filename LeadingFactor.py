#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas_datareader as web


# In[2]:


# import asset data

Equity = web.get_data_yahoo("SPY",
                            start = "2005-01-01",
                            end = "2010-05-01")
Equity_price = Equity['Adj Close'].resample('M').ffill()

PrivateEquity = pd.read_excel('/Users/vicky/Desktop/Risk Lab/TRPEI.xlsx',header=0, index_col=0)


PrivateEquity_price = PrivateEquity['PX_LAST'][0:64]

#print(PrivateEquity_price)
#print(Equity_price)

FixedIncome = web.get_data_yahoo("LQD",
                            start = "2005-01-01",
                            end = "2010-05-01")
FixedIncome_price = FixedIncome['Adj Close'].resample('M').ffill()

RealEstate = web.get_data_yahoo("NVU-UN.TO",
                            start = "2005-01-01",
                            end = "2010-05-01")
RealEstate_price = RealEstate['Adj Close'].resample('M').ffill()

#Cash = web.get_data_yahoo("^IRX",
  #                          start = "2005-01-01",
   #                         end = "2010-05-01")
#Cash_price = Cash['Adj Close'].resample('M').ffill()


# In[48]:


# import 10 factor data

Factor = pd.read_csv('/Users/vicky/Desktop/Risk Lab/factor.csv',header=0, index_col=0, parse_dates=True)

CPI = Factor['CPI'][0:64]
GDP = Factor['GDP'][0:64]
unemployment = Factor['unemployment'][0:64]
CLI = Factor['CLI'][0:64]
BCI = Factor['BCI'][0:64]
CCI = Factor['CCI'][0:64]
trade_in_good = Factor['trade in good'][0:64]
long_term_interest = Factor['long-term interest'][0:64]
short_term_interest = Factor['short-term interest'][0:64]
labor_force = Factor['labor force'][0:64]


# In[67]:


# scaling the data

from sklearn import preprocessing

CPI_scaled = preprocessing.scale(CPI)
GDP_scaled = preprocessing.scale(GDP)
unemployment_scaled = preprocessing.scale(unemployment)
CLI_scaled = preprocessing.scale(CLI)
BCI_scaled = preprocessing.scale(BCI)
CCI_scaled = preprocessing.scale(CCI)
trade_in_good_scaled = preprocessing.scale(trade_in_good)
long_term_interest_scaled = preprocessing.scale(long_term_interest)
short_term_interest_scaled = preprocessing.scale(short_term_interest)
labor_force_scaled = preprocessing.scale(labor_force)

Equity_scaled = preprocessing.scale(Equity_price)
PE_scaled = preprocessing.scale(PrivateEquity_price)
FI_scaled = preprocessing.scale(FixedIncome_price)
RE_scaled = preprocessing.scale(RealEstate_price)
#Cash_scaled = preprocessing.scale(Cash_price)


# In[70]:


date = np.array('2005-01-31', dtype=np.datetime64)
date = date + pd.to_timedelta(np.arange(185), 'M')
#print(date)


# In[73]:


# plot each factor with five asset classes

plt.figure(figsize=(12,5))
plt.xlabel('Date')
plt.ylabel('Scaled Price')

#x = date

# change y1 here for different factors 
y1 = CPI_scaled


# five asset classes
y2 = Equity_scaled
y3 = PE_scaled
y4 = FI_scaled
y5 = RE_scaled
#y6 = Cash_scaled

plt.plot(y1, label="Factor")
plt.plot(y2, '-.',label="Equity")
plt.plot(y3, '-.',label="PE")
plt.plot(y4, '-.',label="FI")
plt.plot(y5, '-.',label="RE")
#plt.plot(y6, '-.',label="Cash")

plt.legend(loc='upper left')
plt.title("Asset Prices Time Series")
plt.show()


# In[114]:


#### for check only



# In[ ]:




