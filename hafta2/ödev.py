urunler = [
{'name':'iphone 8', 'price': '8000' },
{'name':'iphone 8 Plus', 'price': '12000' },
{'name':'iphone X', 'price': '9500' },
{'name':'iphone XR', 'price': '12000' },
{'name':'iphone 14', 'price': '32000' },
{'name':'samsung s20', 'price': '22000' },
]
toplam=0
for i in urunler:
    toplam=toplam+(int(i['price']))
print(toplam)


        

# 1) İki yönden de aynı şekilde okunan sayılara palindromik sayılar denir. 2 haneli 2 sayıdan oluşturulabilecek en büyük palindrom değeri 9009’dur. (91 x 99)  3 haneli iki sayıdan oluşturulabilecek en büyük palindromik sayıyı bulunuz.
palsayi=[]
for i in range(100,1000):
    for j in range(100,1000):
        carpim=i*j
        if str(carpim)==str(carpim)[::-1]:
            palsayi.append(carpim)
print(max(palsayi))






