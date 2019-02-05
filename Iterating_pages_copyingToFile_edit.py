from selenium import webdriver
from bs4 import BeautifulSoup
import collections

#URL of the website to be parsed
URL = "https://news.ycombinator.com/"
driver = webdriver.Firefox()
driver.get(URL)
dict={}

#Looping through different pages & parsing required data
while True:
    soup = BeautifulSoup(driver.page_source, 'lxml')
    for title in soup.find_all("tr", class_="athing"):
        titleid= title.get("id")
        title=title.find(class_="storylink").text
        score_id="score_"+titleid
        score=soup.find(id=score_id)
        if score!=None:
            score=score.text.split()[0]
        else:
            score=0
        dict[title]=int(score)
           
    try:
        driver.find_element_by_link_text('More').click()
    except:
        break

driver.quit()

# Data sorting by values using OrderedDict
c=collections.OrderedDict(sorted(dict.items(),reverse=True, key=lambda x: x[1]))

#Writing content to a file
file =open("Upvote_count_Allpages.txt","w")
for vote, title in c.items(): 
    file.write(str(title))
    file.write("\t"+str(vote))
    file.write("\n")
file.close()
