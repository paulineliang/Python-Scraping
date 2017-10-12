import requests
from bs4 import BeautifulSoup
import urllib
import re
res = requests.get("http://vmus.co/%E5%AE%85%E7%94%B7%E8%A1%8C%E4%B8%8D%E8%A1%8C%E7%94%9F%E6%B4%BB%E5%A4%A7%E7%88%86%E7%82%B8-the-big-bang-theory/")
# print(res.text)

soup = BeautifulSoup(res.text.encode("utf-8"), "html5lib")
# print(soup)

Table = soup.findAll("p")
# print(Table)

youtubeLink = "http://www.youtube.com"
SongList = []

for _Table in Table:
    Video = _Table.findAll("a",{"href":re.compile('s01') })

    for _Video in Video:
        link = _Video["href"]
        # print(link)
        title = _Video.text
        # print(title)
        print(title +"\n"+ link)

#         Songjson ={'title':title, 'link':link}
#         SongList += [Songjson]
# print(SongList[7]['title'])
