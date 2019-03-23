# Import Libraries
import requests
from bs4 import BeautifulSoup

# Store first page of CNBC breaking news
page = requests.get('https://www.cnbc.com/breaking-news/?page=1')
soup = BeautifulSoup(page.text, 'html.parser')

# Go down DOM to find headlines
cnbc_contents = soup.find(class_ = 'cnbc-contents')
cnbc_body = cnbc_contents.find(class_ = 'cnbc-body')
cols = cnbc_body.find(class_ = 'cols2')
col1 = cols.find(class_ = 'unit col1')
stories_linup = col1.find(class_ = 'stories-lineup bigHeader')
stories_assetlist = stories_linup.find(class_ = 'stories_assetlist')

card_list = stories_assetlist.find_all('li')
cards = card_list.find_all(class_ = 'asset cnbcnewsstory imgasset desc_size160_105 card')
headline_containers = cards.find_all(class_ = 'headline')
headline_links = headline_containers.find_all('a')

for link in headline_links:
    print(link.prettify())


