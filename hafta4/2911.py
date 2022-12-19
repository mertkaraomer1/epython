#nesne tabanlı programlama
#from testlib import *
# import testlib
# print(topla(5, 8))

class calisan():
    ad=""
    soyad=""
    zamorani=1.2 #class veriable
    def __init__(self,ad="",soyad="",maas=10000):
        self.ad=ad
        self.soyad=soyad
        self.maas=maas
        self.eposta=ad.lower()+soyad.lower()+"@elginkan.org"
    def fonk1(self):
        return self.maas
    def tamad(self):
        return f"ad={self.ad} soyad={self.soyad} maas={self.maas}"
    def zamyap(self):
        self.maas*=self.zamorani
    @classmethod
    def zamoranıdeğiş(cls,yenioran):
        cls.zamorani=yenioran
class yonetici(calisan):
    def calisanekle(self,eleman):
        self.calisanlar.append(eleman)
    def calisansil(self,eleman):
         self.calisanlar.remove(eleman)
    def __init__(self,ad,soyad,maas=50000,calisanlar=None):
        calisan.__init__(self,ad,soyad,maas)
        if calisanlar is None:
            self.calisanlar=[]
        else:
            self.calisanlar=calisanlar
    def calisanlistele(self):
        for i in self.calisanlar:
            print(i.tamad())
        
#zam=float(input("maas zammı ne kadar olsun="))
calisan.zamoranıdeğiş(2.5)
per1=calisan("ali","can",12000)
per3=calisan("ender","aslan",8000)
per2=calisan()
per2.ad="mahmut"
per2.soyad="tuncer"

#per1.zamoranıdeğiş(5) her ikisinide etkiler.
print(per2.fonk1())
per1.zamyap()
per2.zamyap()
print("yeni maaşı=",per1.maas)
print("per1 yeni maaşı=",per1.maas)
print("per2 yeni maaşı=",per2.maas)
print(per1.eposta)
mudur=yonetici("abdullah", "uyar",60000,[per1,per2])
#mudur.calisanlistele()
mudur.calisanekle(per3)
mudur.calisansil(per2)
mudur.calisanlistele()






















