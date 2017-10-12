import requests
from bs4 import BeautifulSoup
res = requests.get("https://www.youtube.com/playlist?list=PLcg8nKocl9k8lhH4RvyX9JED8ILVkVpw2")
# print(res.text)

soup = BeautifulSoup(res.text.encode("utf-8"), "html5lib")
# print(soup)

Table = soup.findAll("td",{'class':"pl-video-title"})
# print(Table)

youtubeLink = "http://www.youtube.com"
SongList = []
#
for _Table in Table:
    Video = _Table.findAll("a",{'class':"pl-video-title-link yt-uix-tile-link yt-uix-sessionlink spf-link "})
    # print(Title)
    for _Video in Video:
        link = youtubeLink + _Video["href"]
        title = _Video.text
        Songjson ={'title':title, 'link':link}
        SongList += [Songjson]
print(SongList)

import json
with open('SongList.json', 'w') as outfile:
    json.dump(SongList, outfile)
