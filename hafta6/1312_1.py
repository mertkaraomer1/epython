# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 20:16:32 2022

@author: mkara
"""

import pandas as pd
dffilm=pd.read_csv("imdb_1000.csv")
kolon=dffilm.columns
dffilm.info()
# baslik=dffilm['title']
# star=dffilm[['title','star_rating']]
# star1=dffilm[['title','star_rating']].head(50)
# rat=dffilm[dffilm['star_rating']>=8.0][["title","star_rating"]]
# #puanı 7.5 ile 8 arasındaki filmler
# #rati=dffilm[dffilm['star_rating']>=7.5 & dffilm['star_rating']<8.0]

# rating2=dffilm.query('star_rating>=7.5 & star_rating<=8.0')
# rating2=rating2.title.sort_values(ascending=False)
# dur=dffilm[["title","duration"]].sort_values(by="duration")

# filmuzunluk=[]
# for i in dffilm.duration:
#     if i<80:
#         filmuzunluk.append('kısa')
#     elif i>=80 and i<115:
#         filmuzunluk.append('orta')
#     else:
#         filmuzunluk.append('uzun')
# dffilm['uzunluk']=filmuzunluk

# #süresi kısa olan filmleri yazdırın
# dffilm['uzunluk']=filmuzunluk
# uz=dffilm.query("uzunluk=='kısa'")
#puanı 9 dan büyük veya türü macera olan filmler
ADa=dffilm.query('star_rating>9 | genre=="Adventure"')
mf=dffilm[dffilm.actors_list.str.contains('Morgan Freeman')]
grup=dffilm.groupby('genre').star_rating.agg(["mean","max","min","count"]).sort_values(by='mean',ascending=False)







