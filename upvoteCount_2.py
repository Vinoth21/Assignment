#Parse Title from given URL
from bs4 import BeautifulSoup
import requests
key=[]
value=[]
dict={}
for num in range(15):
    source=requests.get("https://news.ycombinator.com/news?p=%2d" %num).text
    soup= BeautifulSoup(source,'lxml')
    for title in soup.find_all("span", class_="score"):
        title=title.text.split()[0]
        key.append(int(title))
    for title in soup.find_all("a", class_="storylink"):
        value.append(title.text)

for i in range(len(key)):
    dict[key[i]]=value[i]

key.sort(reverse=True)

file =open("Upvote_count.txt","w")
for x in key:
    if x in dict.keys():
        file.write(str(dict[x])+"\t " +str(x)+"\n")
file.close()
