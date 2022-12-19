import sys
from PyQt5 import QtWidgets,uic
from datetime import datetime
import sqlite3
from pymongo import MongoClient
import dns
class Windowapp(QtWidgets.QMainWindow):#QMainWindow
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.MongoDBConnect()
        self.win=uic.loadUi("giris.ui")
        self.win2=uic.loadUi("anaekran.ui")
        self.win.show()
        #self.win2.hide()
        self.win.Btn1.clicked.connect(self.btnGirisFonk)
        # self.win2.liste.setColumnWidth(0,250)
        # self.win2.liste.setColumnWidth(1,250)
        #self.win2.liste.setHorizantalHeaderLabels(["id"])
        # people=[{"name":"ender","surname":"zeybek"},{"name":"ali","surname":"kuş"}]
        # row=0
        # for person in people:
        #     self.win2.liste.setItem(row,0,QtWidgets.QTableWidgetItem(person["name"]))
        #     self.win2.liste.setItem(row,1,QtWidgets.QTableWidgetItem(person["surname"]))
        
        self.win2.liste.setItem(0,0,QtWidgets.QTableWidgetItem("test"))
        
    def baglanti_sql(self):
        self.baglanti=sqlite3.connect("database.db")
        self.cursor=self.baglanti.cursor()
    def fileRead(self,kad,sifre):
        dosya=open("calisanlar.txt","r+",encoding="utf-8")
        data=eval(dosya.read())
        dosya.close()


        if kad in data:
            if sifre==data[kad]["sifre"]:
                print("kullanıcı adı ve şifresi doğru")
                simdiki=datetime.now()
                data[kad]["songiris"]=simdiki.strftime("%d/%m/%y,%H%M%S")
                with open("calisanlar.txt","w",encoding="utf-8") as dosya:
                    dosya.write(str(data))
                self.personel=data[kad]
                self.win.hide()
                self.win2.show()
                self.win2.lbl1.setText("Hosgeldin"+data[kad]["isim"].upper())
        else:
            print("kayit yok")
    def sqlread(self,kad,sifre):
        self.baglanti_sql()
        self.cursor.execute("select * from personel where kad=? and sifre=?",(kad,sifre))
        return self.cursor.fetchall()
        
    def btnGirisFonk(self):
        #1-)DOSYA KONTROL 2-)SQL KONTROL 3-)MONGODB KONTROL
        #self.win.kadiline.setText()
        kad=self.win.kadiline.text()
        sifre=self.win.passline.text()

        self.data=self.sqlread(kad, sifre)
        data=self.data
        print(data)
        if len(self.sqlread(kad, sifre))==0:
            self.win.label.setText("hatalı giriş")
        else:
            self.win.hide()
            self.win2.show()
            self.win2.label.setText("hoşgeldiniz."+str(data[0][1]).upper()+" "+str(data[0][2].upper()))
            self.cursor.execute("update personel set songiris=? where kad=? and sifre=?",(datetime.now(),kad,sifre))
            #son giriş tarihi güncellenecek    
            self.baglanti.commit() 
            data=self.ambaryeriget()
            print(data)
            for d in data:
                #print(d[1])
                self.win2.cmbambar.addItem(str(d[1]),str(d[0]))
            self.win2.urunekle.clicked.connect(self.btnurunekle),
            self.urunlergetir()
    def btnurunekle(self):
        urnadi=self.win2.urunadi.text()
        stk=self.win2.stok.text()
        ambyrid=self.win2.cmbambar.currentData() 
        #print(self.win2.cmbambar.currentText()) 
        self.cursor.execute("insert into urunler(urunadi,urunresmi,stok,eklenmetarihi,ambaryeri,ekleyenid) values (?,?,?,?,?,?)",(urnadi," ",stk,ambyrid,self.data[0][0],str(datetime.now())))
        self.win2.liste.setRowCount(0)
        self.baglanti.commit()
    def ambaryeriget(self):
        self.cursor.execute("select id,ambaradi from ambar")
        data=self.cursor.fetchall()
        return data
    def urunlergetir(self):
        self.cursor.execute("select urunler.id,urunadi,stok,ambar.ambaradi from urunler join ambar on urunler.ambaryeri=ambar.id where ekleyenid=?",(str(self.data[0][0])))
        urunler=self.cursor.fetchall()

        row=0
        for urun in urunler:
            self.win2.liste.insertRow(row)
            self.win2.liste.setItem(row,0,QtWidgets.QTableWidgetItem(str(urun[0])))
            self.win2.liste.setItem(row,1,QtWidgets.QTableWidgetItem(urun[1]))
            self.win2.liste.setItem(row,2,QtWidgets.QTableWidgetItem(urun[2]))
            self.win2.liste.setItem(row,3,QtWidgets.QTableWidgetItem(urun[3]))
    def MongoDBConnect(self):
       mongoClient=("mongodb+srv://mert:mert@cluster0.pwbyref.mongodb.net/?retryWrites=true&w=majority") 
       try:
           db=conn["mertdb"]
           collection=db["urunler"]
           print("bağlandı.")
       except:
           print("hatalı")

    
#if __name__=="__main__":
app=QtWidgets.QApplication(sys.argv)
uyg=Windowapp()
sys.exit(app.exec())
