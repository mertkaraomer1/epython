#1-
# a=0
# for i in range(10):
#     a=a+1
# for j in range(10):
#     a=a+1
# print(a)

#2-
# #t=0
# s=int(input("bir sayı"))
# for i in range(s,0,-1):
#     if i**2>20:
#         continue
#     t+=i
# print(t)        
 
# 3-
# kutu=["cetvel","silgi","kalem",["zımba","delgeç"],"gönye"]      
# print(kutu[3][0])      
        
# 4-
# t=0
# s=int(input("bir sayı"))
# for i in range(s,0,-1):
#     if i>5:
#         t+=i
#         continue
    
# print(t)        
        
# 5-
# def fun(i=2,j=3):
#     return i*j
# print(fun(3))     

# 6-
# thistuple = ("apple", "banana", "cherry")
# thistuple[3] = "orange" 
# print(list(thistuple))     

# 7-
# def basamak(sayi):
#     sayac=0
#     while sayi:
#         sayac+=1
#         sayi=sayi//10


#     return sayac

 

# print(basamak(5311))       

# 8-
# for i in range(3):
#     print("a")
#     continue
#     for j in range(3):
#         print("b")
      
# 9-
# names = ['Ahmet', 'Mehmet', 'Ali', 'Aslıhan']
# print(names[-1][-1])      

# 10-
# def ornek(sayı):
#     ex=1
#     ex_str=""
#     while(sayı>=1):
#             ex*=sayı
#             ex_str+=str(sayı)+"x"
#     sayı-=1
#     ex_str+="="+str(ex)
#     return ex_str


# print(ornek(5))

# 11-
# def fonksiyonum2(şehir,*args):
#     print ("Şehir:", şehir)
#     islem=0
#     for i in args:
#             islem+=i
#     print(islem)


# fonksiyonum2("Kocaeli", 10,11,20)

# 12-
# for i in range(10,50,5):
#     if i%10==0:
#         continue
#     print(i)
#     if i==30:
#         break












