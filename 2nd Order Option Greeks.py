#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import numpy as np
import matplotlib.pyplot as plt


# # Option Parameters

# In[2]:


S = 100 # underlying price
K = 100 # strike price
r = 0.05 #risk-free rate
q = 0.02 # dividend yield
T = 0.5 # time to maturity
sigma = 0.2 #volatility


# # Black-Scholes-Merton formula for vanilla call option price

# In[3]:


d1 = (math.log(S/K) + (r-q+sigma**2/2)*T)/(sigma*math.sqrt(T))
d2 = d1-sigma*math.sqrt(T)
N_d1 = 0.5 + 0.5*math.erf(d1/math.sqrt(2))
N_d2 = 0.5 + 0.5*math.erf(d2/math.sqrt(2))
C = S*math.exp(-q*T)*N_d1 - K*math.exp(-r*T)*N_d2


# # Option Greeks

# In[4]:


delta = math.exp(-q*T) * N_d1
gamma = math.exp(-q*T) * math.exp(-d1**2/2) / (S*sigma*math.sqrt(2*math.pi*T))
speed = -gamma*d1/(S*sigma*math.sqrt(T))
vega = S*math.exp(-q*T)*math.exp(-d1**2/2)*math.sqrt(T)/(100*100)
vomma = vega*d1*d2/sigma
charm = -math.exp(-q*T) * (N_d1*d2*math.exp(-d1**2/2))/(2*T*sigma*math.sqrt(T))
vanna = -math.exp(-q*T) * N_d1 * d2 / sigma
color = -math.exp(-q*T) * math.exp(-d1**2/2) * (d2/(sigma*math.sqrt(T))) * (1-d1*d2/(sigma*math.sqrt(T)))


# # Visualize Option Greeks

# In[5]:


greeks = [delta, gamma, speed, vega, vomma, charm, vanna, color]
greeks_labels = ['Delta', 'Gamma', 'Speed', 'Vega', 'Vomma', 'Charm', 'Vanna', 'Color']


# In[6]:


fig, ax = plt.subplots(figsize=(8, 6))
ax.bar(greeks_labels, greeks)
ax.set_title('Option Greeks for Call Option')
ax.set_ylabel('Value')
ax.axhline(y=0, color='black', linestyle='--', linewidth=0.5)
plt.show()


# In[ ]:




