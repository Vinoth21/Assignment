#COmplete

#Parse Title from given URL
from bs4 import BeautifulSoup
import requests
import collections

source=requests.get("https://news.ycombinator.com").text
dict={}   
soup= BeautifulSoup(source,'lxml')

for title in soup.find_all("tr", class_="athing"):
    titleid= title.get("id")
    
    title=title.find(class_="storylink").text
    print(title)
    score_id="score_"+titleid
    score=soup.find(id=score_id)
    if score!=None:
            score=score.text.split()[0]
    else:
        score=0
    #score=score.text.split()[0]
    dict[int(score)]=title
       
    #source = driver.find_element_by_link_text('More')

c=collections.OrderedDict(sorted(dict.items(), reverse=True))
#print (sorted(dict.items(), reverse=True)) 
file =open("Upvote_count.txt","w")
for vote, title in c.items(): 
    file.write(str(title))
    file.write("\t"+str(vote))
    file.write("\n")
file.close()