fnl=lambda a:a*2
print(fnl(5))
#ELGİNKAN
#YAZILAN METNİ TERSİNE ÇEVİREN LAMBDA
# tersCevir=lambda s : s[::-1]

# print(tersCevir("ELGİNKAN"))
# sayilar=[1,2,3,4,5]
# sonuc=list(lambda sayi:sayi**2,sayilar)
# print(sonuc)

def myfunc(n):
    return len(n)
x=map(myfunc,['elma','armut','çilek'])
print(*x)


