# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 18:38:27 2022

@author: mkara
"""

import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
data=pd.read_csv("hw_25000.csv")
print(data.columns)
# plt.scatter(data.Height,data.Weight)
# plt.show()
boy=data.Height.values.reshape(-1,1)
kilo=data.Weight.values.reshape(-1,1)

lreg=LinearRegression()
lreg.fit(boy,kilo)
print(lreg.predict([[62]]))
plt.scatter(data.Height,data.Weight)
x=np.arange(min(data.Height),max(data.Height)).reshape(-1,1)
plt.plot(x,lreg.predict(x),color="red")
plt.show()
print(r2_score(kilo,lreg.predict(boy)))



