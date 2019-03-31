import requests
import time
from bs4 import BeautifulSoup
#Quantitative Investment Society

#Change "notToday" and if statement "if 'Today'..." to make it more than 1 day


fileName = input("File name to write to: ")
file = open(fileName, 'a')
notToday = False
count = 1
while notToday == False: #change if more days
    url = "https://www.cnbc.com/breaking-news/"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
    response = requests.get(url, headers = headers)
    
    try:
        soup = BeautifulSoup(response.content, "html.parser")
        newslst = soup.find(id="cnbc-contents")
        x = newslst.find(class_ = "stories_assetlist")
        itemlst = x.find_all(class_="headline" )#newslst.find_all(class_="item")
        
        for i in itemlst:
            
            
            print(i.find('a').get_text().split("\n")[1])
            file.write(i.get_text().split('\n')[1])
            file.write("\n")
            
        count += 1
    except:
        print("Fucked up")
        print(response)
        break
    break
file.close()