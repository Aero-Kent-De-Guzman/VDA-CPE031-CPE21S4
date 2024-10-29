# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 13:00:20 2024

@author: TIPQC
"""

import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("Technological-Products-Sample-Data.csv")
df = pd.DataFrame(data)

######
"""
A&B
"""

x1 = df["Date of Release"]
y1 = df["Price (USD)"]

#plt.plot(x1, y1, marker = 'o', color = 'red', linewidth = '3')
#plt.xlabel("Year")
#plt.ylabel("Sales")
#plt.show()

#####
"""
 F
"""

country = df["Country of Origin"]
plt.pie(country)
plt.show()

#####