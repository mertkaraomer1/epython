import requests
from bs4 import BeautifulSoup
url="http://www.imdb.com/chart/top"
icerik=requests.get(url).content
soup=BeautifulSoup(icerik,"html.parser")
# print(soup)
#imdb rating i 8 üzerindeki filmleri listeyelim
basliklar=soup.find_all("td",{"class":"titleColumn"})
rating=soup.find_all("td",{"class":"ratingColumn imdbRating"})
rat=float(input("rating girin"))
for baslik,rating in zip(basliklar,rating):
    baslik=baslik.text.strip()
    baslik=baslik.replace("\n","")
    rating=rating.text
    rating=rating.strip()
    rating=rating.replace("\n","")
    rating=float(rating)
    if rating>=rat:
        print(f"Başlık:{baslik} Rating:{rating}")
   