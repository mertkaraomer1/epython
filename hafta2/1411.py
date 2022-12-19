#list tupple dict
a=[1,2,3]
sozluk={1:'bir',2:'iki',3:'üç'}
#print(sozluk[1])

# sozluk[4]='dört'#değiştirir
# print(sozluk)


# #sozluk[3]='dört'#günceller
# print(sozluk.keys())
# print(sozluk.values())

# print(sozluk.pop(4))
# print(sozluk)

# for i in sozluk:
#     print("key:",i,"value:",sozluk[i])

# for i in sozluk.values():
#     print(i)

# for i,z in sozluk.items():
#     print(i,"----",z)
from datetime import datetime
# calisanlar={
#     "ali":{
#         "ad"
#         "memleket":"amasya",
#         "dTarihi":"05-08-2000",
#         "tel":"3243252454"
#     },
#     "ayşe":{
#         "memleket":"hatay",
#         "dTarihi":"07-05-2003",
#         "tel":"4252452352"
#     },  
#      "ceyda":{
#         "memleket":"kcoaeli",
#         "dTarihi":"06-03-2001",
#         "tel":"4233243243"
#     }
# }
#çalışana ait bilgi için adını giriniz.
# calisan=input("çalışanın adını giriniz.")
# if calisan in calisanlar:
#     print("""
#           ***Bulundu***
#           """)
    
#     dtarih=calisanlar[calisan]['dTarihi']
#     simdiki=datetime.now()
#     dgunu=datetime.strptime(dtarih,"%d-%m-%Y")
#     simdiki=datetime.now()
#     yas=simdiki.year-dgunu.year-((simdiki.month,simdiki.day)<(dgunu.month,dgunu.day))
#     print(f"MEMLEKETİ:{calisanlar[calisan]['memleket']},YAŞ:{yas},Telefon{calisanlar[calisan]['tel']}")
# else:
#     print("bulunamadı")
""" 
EKLEMEK İSTEDİĞİNİZ KİŞİ ADI
 MEMLEKETİm
DTARİH
TELEFON
"""
#YENİ KAYIT
# ad=input("adı giriniz.")
# memleket=input("memleketini giriniz.")
# dtarihi=input("dtarihi giriniz(gün-ay-yıl).")
# telefon=input("telefon giriniz başında sıfır olmadan.")
# calisanlar[ad]={"memleket":memleket,"dTarihi":dtarihi,"tel":telefon}
# print(calisanlar)
#SİLME
# ad=input("silmek istediğiniz kişinin adını giriniz.")
# calisanlar.pop(ad)
# print(calisanlar)
#GÜNCELLEME

# calisanlar[ad]["memleket"]=memleket
# calisanlar[ad]["dTarihi"]=dtarihi
# calisanlar[ad]["tel"]=telefon

#MEMLEKETİ HATAY OLANIN BİLGİLERİ
# sehir=input("şehir giriniz.").lower()
# bulundu=False
# for x,y in calisanlar.items():
#     if y["memleket"].lower()==sehir:
#         print("adı:",x,"dTarihi:",y["dTarihi"],"tel:",y["tel"])
#         bulundu=True
#     if bulundu=false
        
   
    

# from datetime import *

# simdiki=datetime.now()
# dtarih=("05-12-2000")
# print("YAŞ:",datetime.now().year - int(dtarih.split("-")[2]))
# #print(datetime.now().strftime("%c"))
# dgunu=datetime.strptime(dtarih,"%d-%m-%Y")
# yas=simdiki.year-dgunu.year-((simdiki.month,simdiki.day)<(dgunu.month,dgunu.day))
# print("gerçek Yaşı",yas)

calisanlar={
    "123":{
        "ad":"ali",
        "soyad":"çalış",
        "memleket":"amasya",
        "dTarihi":"05/08/2000",
        "bölüm":"insan kaynakları",
        "tel":"3243252454"
    },
    "456":{
        "ad":"mert",
        "soyad":"karaömer",
        "memleket":"hatay",
        "dTarihi":"07/05/1996",
        "bölüm":"IT",
        "tel":"5434080041"
        
    }

}
# 1-MENÜ OLUŞTURULCAK
# 2-DOSYADAN OKUMA YAZMA
# 3-GÖRSEL ARAYÜZ İLE DOSYADAN OKUYUP YAZACAK(PDF AKTARMA,EXELE AKTARMA)
# (GRAFİK EKLEME)
# 4-MONGODB İLE VERİTABANINDAN OKUYUP YAZACAK


#SETS VERİ TİPİ indexleme yok
meyveler={"elma","armut","kiraz","mandalina","portakal"}
sebzeler={"kabak","marul","domates","havuç","patlıcan"}
# urun=input("ürünü giriniz.")
# if urun in meyveler:
#     print(f"{urun} meyvedir.")
# elif urun in sebzeler:
#     print(f"{urun} sebzedir.")

# print(type(meyveler))
# meyveler.add("kavun")#ikinci kez girileni eklemiyor.
# meyveler.update(["karpuz"])
# for i in meyveler:
#     print(i)

a=["çilek","muz"]
b=["elma","muz","kavun"]
a=b
b[0]="karpuz"
print(a,b)





