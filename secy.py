import requests
from bs4 import BeautifulSoup
import csv
page = requests.get("https://summerofcode.withgoogle.com/archive/2019/projects/")
soup = BeautifulSoup(page.content,"html.parser")
html = list(soup.select('main div div a'))
fhtml=[]
for j in range(len(html)-1):
    fhtml.append(html[j].get_text())
body = list(soup.select('main div div div'))
fbody=[]
for k in range(len(body)-1):
    fbody.append(body[k].get_text())
final = []
for i in range(0,len(fhtml)) :
    final.insert(3*i,fhtml[i])
    final.insert(3*i+1,fbody[2*i+1])
    final.insert(3*i+2,fbody[2*i])

with open('pclub.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name","Organisation","Project"])
    for w in range(0,len(final),3):
         writer.writerow([final[w],final[w+1],final[w+2]])
    