import urllib.request as rq
import re
from datetime import datetime,timedelta
from tkinter import *
from PIL import ImageTk,Image




# sehirsec=input("hangi şehirin hava durumunu istiyorsunuz.")
# url=f"http://www.havadurumu15gunluk.net/havadurumu/{sehirsec}-hava-durumu-15-gunluk.html"
# site=rq.urlopen(url).read().decode("utf-8")
# gunduz='<td width="45">&nbsp;&nbsp;(.*)°C</td>'
# # print(site)
# hd1=gunduzhavadurumu=re.findall(gunduz,site)
# gunduzhavadurumu[0]
gun1=0
# # for i in re.findall(gunduz,site):
# #     tarih=datetime.now()+timedelta(days=gun1)
# #     print(tarih.strftime("%d/%m/%y"),"=> ",i)
# #     gun1+=1
# dosya=open("havadurumu.txt","w+",encoding="utf-8")
# dosya.write(str(gunduzhavadurumu))
# dosya.close()

# "aydın":{
    
# }
def btngetir():
    sehirsec=entry.get()
    url=f"http://www.havadurumu15gunluk.net/havadurumu/{sehirsec}-hava-durumu-15-gunluk.html"
    site=rq.urlopen(url).read().decode("utf-8")
    gunduz='<td width="45">&nbsp;&nbsp;(.*)°C</td>'
    gece='<td width="45">&nbsp;(.*)°C</td>'
    gunduzhavadurumu=re.findall(gunduz,site)[0]
    gecehavadurumu=re.findall(gece,site)[1]
    havaolayi=f'<td width="170"><div align="left"><img src="/havadurumu/images/trans.gif" alt="{sehirsec.capitalize()} Hava durumu 15 günlük" width="1" height="1">(.*)</div></td>'
    havaolayi=re.findall(havaolayi,site)[0]
    print(havaolayi)
    lbl2["text"]="gündüz:" +gunduzhavadurumu+ "°C"
    lbl3["text"]="gece:" +gecehavadurumu+ "°C"
    resimsaganak=ImageTk.PhotoImage(Image.open("hafta3/saganak.jpg"))
    resimyagmurlu=ImageTk.PhotoImage(Image.open("hafta3/yagmurlu.jpg"))
    
    if havaolayi=="Sağanak Yağiş":
        lbl4["image"]=resimsaganak
    if havaolayi=="Çok Bulutlu":
        pass


pencere=Tk("Ana Ekran")
pencere.title("ELGİNKAN HAVA DURUMU")
pencere.geometry("600x400")
lbl=Label(pencere,text="HAVA DURUMU",font="Verdana 20 bold",bg="red",fg="white")
lbl.place(x=200,y=50)
lbl2=Label(pencere,font="Verdana 12 bold")
lbl2.place(x=300,y=150)
lbl3=Label(pencere,font="Verdana 12 bold")
lbl3.place(x=300,y=180)
lbl4=Label(pencere)
lbl4.place(x=200,y=250)

entry=Entry(pencere,width=50)
entry.place(x=200,y=100)
btnsorgula=Button(pencere, text="Sorgula",command=btngetir)
btnsorgula.place(x=300,y=125)
pencere.mainloop()










































