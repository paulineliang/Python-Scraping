import requests
from bs4 import BeautifulSoup
res = requests.get("http://www.youtube.com")
# print(res.text)

soup = BeautifulSoup(res.text.encode("utf-8"), "html5lib")
# print(soup)

Table = soup.findAll("h3")
# print(Table)

youtubeLink = "http://www.youtube.com"
SongList = []

for _Table in Table:
    Video = _Table.findAll("a",{"href": True})
    # print(Title)
    for _Video in Video:
        link = youtubeLink + _Video["href"]
        title = _Video["title"]
        # print(link+"\n"+title)

        Songjson ={'title':title, 'link':link}
        SongList += [Songjson]
print(SongList[7]['title'])
