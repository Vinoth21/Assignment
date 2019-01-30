#Parse Title from given URL
from bs4 import BeautifulSoup
import requests

source=requests.get("https://news.ycombinator.com/").text

soup= BeautifulSoup(source,'lxml')

for title in soup.find_all("a", class_="storylink"):
    print (title.text)