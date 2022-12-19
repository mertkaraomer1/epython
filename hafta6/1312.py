# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 18:29:04 2022

@author: mkara
"""
import pandas as pd
import numpy as np
data=np.array(["ali","mehmet","salih"])
s=pd.Series(data,index=[1,2,3])
s.to_excel("deneme.xlsx")
print(s[1])
s3=pd.Series(5,index=[1,2,3,4,5])
data=[10,20,30,40,50]
df=pd.DataFrame(data)
data2=[["ali",25,"kocaeli"],["mehmet",35,"izmir"]]
df2=pd.DataFrame(data2,columns=["isim","yaş","şehir"])
df2.to_excel("deneme2.xlsx")
#kaggle veri ile ilgili incelemelerin yapıldığı yer

df=pd.read_excel("deneme2.xlsx")
notlar=pd.read_csv("grades.csv")
print(notlar.head())
print(notlar.tail())
print(notlar[:11])
lc=notlar.loc[9]
print(notlar.info())

#sonuç alanı olucak 50 den büyükse geçti küçükse kaldı yazıcak.

notlar.columns=["isim","soyisim","ssn","test1","test2","test3","test4","final","sonuç"]
print(notlar.loc[:,"isim":"soyisim"])
print(notlar.loc[:3,["isim","soyisim","final"]])
print(notlar.iloc[:3,0:2])
print(notlar.loc[::-1,:"isim"])











