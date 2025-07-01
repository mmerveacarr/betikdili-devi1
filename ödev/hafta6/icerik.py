import requests
from bs4 import BeautifulSoup
def content(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    tarih = soup.find("time")
    tarih = tarih.text.strip() \
        if tarih else "Tarih bulunamadı"
    tittle = soup.find("h1", {"class": "content-title"})
    tittle = tittle.text.strip() \
        if tittle else "Başlık bulunamadı"
    content_div = soup.find("div", {"class": "content-detail"})
    paragraphs = content_div.find_all("p") \
        if content_div else []
    icerik = ' '.join([p.text.strip() for p in paragraphs]) \
        if paragraphs else "İçerik bulunamadı"
    data = '{};{};{}'.format(tarih, tittle, icerik)
    with open("milligazete.txt", 'a', encoding='utf-8') as file:
        file.write(data + '\n')

url2 = 'http://www.milligazete.com.tr/haber/24244937/serdar-haydanli-kimdir'
content(url2)









from pylab import *
import matplotlib.pyplot as plt
x = [2,-3,-1.5,3]
y = [3,1,-2.5,-2]
color=['m','g','r','b']
a = x + [x[0]]
b = y + [y[0]]
fig = plt.figure()
ax = fig.add_subplot(111)
scatter(x,y, s=100 ,marker='o', c=color)
for i in range(len(x)):
    plt.plot(x[i:i+2], y[i:i+2],'ro-')
plt.plot(a,b)
left,right = ax.get_xlim()
low,high = ax.get_ylim()
arrow( left, 0, right -left, 0, length_includes_head = True, head_width = 0.15 )
arrow( 0, low, 0, high-low, length_includes_head = True, head_width = 0.15 )
xpoints = ypoints = ax.get_xlim()
ax.plot(xpoints, ypoints, linestyle='-', color='k', lw=3, scalex=False, scaley=False)
grid()
show()