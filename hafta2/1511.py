#for döngüsü
#liste=range(1,100,5)
# for i in range(0,100,5):
#     print(i)

# for i in range(100,0,-5):
#     print(i)

# 1 den n kadar sayıları toplamıyla birlikte yazdırsın
# bir sayı giriniz 5

# sayi=int(input("bir sayı giriniz."))
# toplam=0
# for i in range(1,sayi+1):
#     if i!=(sayi):
#         print(i,end="+")
#     else:
#         print(i,end="=")
#     toplam+=i
# print(toplam)

# 1x1=1
# 1x2=2
# .
# .
# .
# .
# .
# 1x9=9
# 2x1=2
# .
# .
# .
# .
# 10x10=100



# for x in range(1,11):
#     for y in range(1,11):
#         print(f"{x}x{y}={x*y}",end=" ")
#     print("",end="\n")

# 1
# 1 3
# 1 3 5
# 1 3 5 7
# 1 3 5 7 9
# 1 3 5 7 9 11

# for i in range(1,12,2):
#     for j in range(1,i,2):
#         print(j,end=" ")
#     print(i,end="\n")

# while 1:
#     print("Merhaba")

# 1*2*3*4*5=120
# sayi=int(input("sayi giriniz.: "))
# fakt=1
# while sayi>0:
#     fakt*=sayi
#     sayi-=1
# print("Fact=",fakt)
    
# urunler=["ıphone 14","ıphone x","oppo","huawei","samsung s10","ıphone 14 pro max"]
#ürünler listesinde ıphone kaç tane var.
# sayac=0
# for urun in urunler:
#     if urun.find("ıphone")==0:
#         sayac+=1
# print(f"{sayac} tane ıphone bulundu.")



# i=0
# sayac=0
# while i<len(urunler):
#     if urunler[i].find("ıphone")==0:
#          sayac+=1
#     i+=1   
# print(f"{sayac} tane ıphone bulundu.") 

import random
#print(random.randint(1,6))
#1 ile 10 arasında 6 tane sayıyı loto listesine ekleyin(sayılar tekrar etmesin)
# loto=[]
# sayac=0
# for i in range(1,7):
#     loto.append(random.randint(1,10))
# while True:
#     rsayi=random.randint(1,100)
#     if rsayi not in loto:
#         loto.append(rsayi)
#         sayac+=1
#     if sayac==6:
#         break
# print("sayısal loto sonucu",loto)
 
# isimlistesi=["ali","mehmet","aslı","meral","aslı"]
# print(random.choice(isimlistesi))
# print(random.sample(list(set(isimlistesi)), 2))

# sayilar=list(range(1,11))+["kız","joker","papaz"]
# semboller=["maça","kupa","sinek","karo"]
# kagitlar=[]
# for i in semboller:
#     for j in sayilar:
#         kagitlar.append(i+" "+str(j))
# kagitlar=random.sample(kagitlar, 52)
# print(kagitlar)
# isimlistesi=["ali","mehmet","aslı","meral"]
# a=0
# b=13
# oyuncu=[]
# isimlistesi2={}
# for i in range(len(isimlistesi)):
#     #oyuncu.append(kagitlar[a:b])
#     isimlistesi2[isimlistesi[i]]=kagitlar[a:b]
#     a+=12
#     b+=12
# print(isimlistesi2)

#taş kağıt makas oyunu
#3 olan kazansın
# kullanicipuan=0
# bilpuan=0
# while True:
#     secim=input("seçim yapın (taş->t kağıt->k makas->m)")
#     if secim=="q":
#         break
#     bilsecim=random.choice(["t","k","m"])

    
#     if (secim=="m" and bilsecim=="m") or (secim=="k" and bilsecim=="k") or (secim=="t" and bilsecim=="t"):
#         print("ayni seçimi yaptınız.")
#         continue
        
#     if (secim=="m" and bilsecim=="k") or (secim=="k" and bilsecim=="t") or (secim=="t" and bilsecim=="m"):
#         kullanicipuan+=1
#     else:
#         bilpuan+=1
#     if kullanicipuan==3 or bilpuan==3:
#         print("oyun bitti.Kazanan{}".format("Siz"if kullanicipuan>bilpuan else "PC."))


#     print("puan durumu PC{bilpuan},siz{kullanicipuan}")


#banka atm programı
#kadi ve şifreyi girin şifre ve id eşleşmesine bakıcak(3 den fazla yanlış girilirse kart bloke olucak)
#menü olucak
#1 e basılırsa para çekme yapılacak 100 ve katları şeklinde verilecektir.
#2 para yatıralacak
#3 bakiye öğrenme
#4 çıkış yapılacak kartınız alınızşeklinde
kadi="elginkan"
sifre="123"
bakiye=10000
user=input("kullanıcı adını giriniz.")
passw=input("şifreyi giriniz.")
if user==kadi and passw==sifre:
    while True:
        print("""
              ****MENÜ****
              1-PARA ÇEKME
              2-PARA YATIRMA
              3-BAKİYE GÖRÜNTÜLEME
              4-ÇIKIŞ
              """)
        islem=input("seçim yapınız.")
        if islem=='4':
            break
        elif islem=='3':
            print("GÜNCEL BAKİYENİZ.",bakiye)
            if miktar>bakiye:
                miktar=float(input())






































