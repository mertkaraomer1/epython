# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 18:26:28 2022

@author: mkara
"""

import numpy as np
from matplotlib import pyplot as plt

# x=np.arange(1,11)
# y=2*x+10
# plt.title("demo")
# plt.xlabel("x ekseni")
# plt.ylabel("y ekseni")
# plt.plot(x, y)
# plt.savefig(r"C:\Users\mkara\OneDrive\Masaüstü\epython\hafta6\test.png")
# plt.show()

x=np.arange(0,3*np.pi,0.1)
y=np.sin(x)
plt.plot(x, y)
plt.show()




















