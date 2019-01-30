#Parse Title from given URL
from bs4 import BeautifulSoup
import requests

source=requests.get("https://news.ycombinator.com/").text

soup= BeautifulSoup(source,'lxml')
lst=[]

for title in soup.find_all("span", class_="score"):
    title=title.text.split()[0]
    lst.append(int(title))
lst.sort(reverse=True)
print (lst)