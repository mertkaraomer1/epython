#boyu 175 olan kişi sayısı
with open("hafta4/person_data.txt","r",encoding="utf-8") as dosya:
    boylis=[]
    for veri in dosya.readlines():
        print(veri)
        boy=veri.strip().split()[2]
        boylis.append(boy)
#print(boylis.count("175"))
boylar={x:boylis.count(x) for x in boylis}
boysirali=sorted(boylar.items(),key=lambda x:x[1],reverse=True)
print(boysirali)