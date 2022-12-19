# print("merhaba")
# print(100/5)
# print(True)
# print(50.8)
# print(2**3)

# a=b=c=5
# print(c)

# a,b,c=7,8,9
# print(a,b,c)

# a=12
# b=5
#print(a//b)#bölüm kısmını alıyor
#print(a%b)#mod alma
#print(a**b)#üs alma

# ogrAd="ahmet"
# ogrSoyad="çınar"
# yas=20 
# adsoyad=ogrAd+" "+ogrSoyad
# print(f"adım {ogrAd} soyadım {ogrSoyad} yaşım {yas}")
# print(adsoyad)

# print(adsoyad[-1])
# print(adsoyad[0])
# print(len(adsoyad))
#print(adsoyad[len(adsoyad)-1])
# print(adsoyad[0:5])
# print(adsoyad[0:7])
# print(adsoyad[3:])
# print(adsoyad[-30:-7])
# print(adsoyad[2:10:3])#en son çift nokta sonrası gelen kaç kaç atlıcvağını belli edeer
# print(adsoyad[::-3])#tersine çevirme için iki kere çift nokta

# print("benim adım {}".format(adsoyad))

# print("adım {} soyadım {} yaşım {}".format(ogrAd,ogrSoyad,yas))

# print("adım" , ogrAd , "soyadım", ogrSoyad,"yaş",yas,sep=" \n ")
# print("adım" + ogrAd + "soyadım"+ ogrSoyad+"yaş"+ str(yas),sep=" ")

# print(f"adım {ogrAd} soyadım {ogrSoyad} yaşım {yas}")
# print(f'adım {ogrAd} soyadım {ogrSoyad} yaşım {yas}')
# print(f"adım {ogrAd} 'soyadım' {ogrSoyad} yaşım {yas}")
# print(f'adım {ogrAd} soyadım esma\'nın {ogrSoyad} yaşım {yas}')

kurum="ahmet elgınkan"
#a ve e harfini büyütelim
# print('A'+kurum[1:5] + ' E' +kurum[7:])
# print(kurum.upper())
# print(kurum.lower())
# print(kurum.title())
# print(kurum.capitalize())
# print(kurum.strip())
# print(' Kurum '.strip(),end='')
# print('test')
msg="PYTHON KURSUNA HOŞGELDİNİZ. AHMET ELGİNKAN mesleki ve eğitim merkezi"
# sonuc=msg.split()
# print(sonuc[0])
# #yukarıdaki ilk cümlede kaç kelime var
# sonuc=msg.split('.')
# print(len(sonuc[0].split()))
# print(msg[msg.index("eğitim"):])
# print(msg.replace("PYTHON", "SQL"))
# print(msg.startswith('p'))#baş harfe göre true false veriyor
# print(msg.endswith('i'))#son harfe göre true false veriyor
# print(msg.replace(msg.split()[0], "SQL")*3)

# site="www.aemtem.org.tr"
# #aetem yazdıralım
# sonuc=site.split(".")[1]
# print(sonuc)
# #site içerisinde kaç tane e var
# print(site.count('e'))
# print(site.find('tr'))
# print('abc'.isalpha())#içinde sayı olsa false olurdu
# print('12345'.isdigit())#içinde harf olsa false olcaktı
"""
0-20 yaşındaysan çok gençsin
20-65 orta yaşlısın
65-80 yaşlısın.
"""

# yas=input("lütfen yaşınızı giriniz:")
# if(yas.isdigit()):
#     yas=int(yas)

#     if 0<yas<20:
#         print("yaşınız çok genç")
#     elif 20<=yas<65:
#         print("orta yaşlısınız")
#     elif 65<=yas<85:
#         print("çok yalısın")
# else:
#     print("lütfen yaşınızı düzgün giriniz")

#LİSTELER
sayilar=[1,2,3,4]
print(type(sayilar))
# print(sayilar[0:2])
# sayilar[0]=20
# print("sayı listesi=",sayilar)
# #son elamanı -100 yapın
# sayilar[3]=-100
#print("sayı listesi=",sayilar)
# sayilar=sayilar[::-1]
# #print("sayı listesi=",sayilar)
# liste1=["ALİ","MEHMET","CAN"]
# liste2=["EFE","Tuğçe"]
# #liste1 deki isimlerin ilk harfleri büyük olsun
# # print(liste1)#['Ali','Mehmet','Can']

# liste1[0]=liste1[0].title()
# liste1[1]=liste1[1].title()
# liste1[2]=liste1[2].title()
# # print(liste1)
# # print(liste1+liste2)
# ogrenciler=[liste1,liste2]
# print(ogrenciler[1][0])

# telefon=["samsung s20","ıphone14","oppo","xiaomi","huawei"]
# telefon=telefon +["REDMİ"]
# print(telefon)
# if 'samsung s20' in telefon:
#     print('evet var stokta')
# else:
#     print('hayır yok')

# ogrenci1=["Ahmet","yiğit",2005,[70,80,70]]
# ogrenci2=["aslı","tuna",2007,[50,40,70]]
# ogrenci3=["melih","aslan",2000,[80,40,90]]

# ogrenciler=[ogrenci1,ogrenci2,ogrenci3]
# for i in ogrenci1:
#     print(i)
# for ogr in ogrenciler:
#     print(ogr)
    
"""
 1.öğrecinin adı ahmet soyadı : yiğit yaşı not ortalaması
 2.öğrecinin adı aslı soyadı : tuna yaşı not ortalaması
 3.öğrecinin adı melih soyadı : aslan yaşı not ortalaması
 
 """
# count=1
# for ogr in ogrenciler:
#     print(f"{count}.ogrencinin adı {ogr[0]} soyadı {ogr[1]} yaşı {2022 - ogr[2]} not ortalamsı {(ogr[3][0]+ogr[3][1]+ogr[3][2])/len(ogr[3])}")
#     count=+1
    
# ogrnot1=ogr[3]
# print(max(ogrnot1))
# print(min(ogrnot1))
# liste=['a','e','w']
# print(max(liste))
# ogrnot1.append(100)
# print(ogrnot1)
# ogrnot1.insert(2,00)
# print(ogrnot1)
# ogrnot1.insert(-1,100)
# print(ogrnot1)
# ogrnot1.insert(len(ogrnot1), 70)
# print(ogrnot1)

# liste=[70,20,90,30,50]
# # liste.pop(2)
# # print(liste)
# # liste.remove(70)
# # print(liste)

# # liste.sort(reverse=True)
# # print(liste)


# print(liste.index(20))
# #listenin içindeki 50 yi 100 yapınız.
# liste[liste.index(50)]=100
# print(liste)


# tuple.append(10)
# tuple[1]=5
# print(tuple)
# dizi=list()
# dizi=[]
# ogr1=("123","ahmet","ali",[])
# ogr2=("321","mehmet","murat",[])
# ogrenciler=[ogr1,ogr2]
# ogrenci=input("hangi öğrenicinin notunu gireceksiniz")
# notu=input("notu giriniz.")
# bulundu=False
# for ogr in ogrenciler:
#     if ogrenci in ogr:
#         ogr[-1].append(notu) 
#         bulundu=True
# if bulundu==False:
#     print("kayıt bulunamadı")  
# else:
#    print(ogrenciler)

plakalar={'kocaeli':41,'istanbul':34,'izmir':35}   #dict()
print(plakalar['kocaeli'])
print(plakalar['istanbul'])

ogrenciler={
    'python':{
        "ad":'erhan',
        "soyad":'al',
        "not":[50,80]
    },
    'sql':{        
        "ad":'ayşe',
        "soyad":'bal',
        "not":[20,100]
        
    }
}
print("sql öğrencilernin ortalaması:",end=" ")
print((ogrenciler['sql']["not"][0]+ogrenciler['sql']["not"][1])/2)



































































































    



