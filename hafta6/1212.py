# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 20:37:52 2022

@author: mkara
"""
import numpy as np
from numpy import pi
a=np.arange(15).reshape(3,5)
print(type(a))
print(a.ndim)
b=a.shape


c=np.array([1,2,3,4,5,6,7,8,9]).reshape(3,3)

d=np.array([[1,3],[5,7],[7,9]])
print(d.ndim)

e=np.linspace(1,10, 100)
print(e)

k=np.linspace(0,2*pi, 100)
sinx=np.sin(k)
f=np.array([20,30,40,50])
g=np.arange(4)
sonuc1=f-g
sonuc2=f*g
sonuc3=f@g
sonuc3_2=f.dot(g)
ones=np.ones((2,4))
zeros=np.zeros((10,10))
rd=np.random.random((3,5))
top1=np.sum(rd)
maks=np.max(rd)
mini=np.min(rd)
kök=np.sqrt(f)
yenif=f[::-1]
yenif2=f[1:3]
sayilar=np.array([[0,5,10],[15,20,25]])
print(sayilar[:,-1])
print(sayilar[-1,:])
print(sayilar[:,0:2])
print(sayilar.ravel())

aa=np.floor(10*np.random.random((2,3)))
ab=np.floor(10*np.random.random((2,3)))
ca=np.vstack((aa,ab))
cb=np.hstack((aa,ab))






