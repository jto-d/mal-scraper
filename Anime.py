from urllib.request import urlopen
import codecs
from bs4 import BeautifulSoup
import requests

# class Anime:
#     def __init__(self, name, URL) -> None:
#         self.name = name
#         self.URL = URL
#         self.page = urlopen(self.URL).read()

#     def anime_opening(self):
#         self.page = str(self.page)
#         self.title = self.page.split('"theme-song-index"')
#         # self.title = self.page.split('"theme-song-title"')
#         # self.title = self.title[1].split('"')[1]

#         self.artist = self.page.split('"theme-song-artist"')
#         self.artist = self.artist[1].split('<')[0][5:]

#     def __str__(self):
#         return self.name

class Anime:
    def __init__(self, name, URL) -> None:
        self.name = name
        self.URL = URL
        self.page = requests.get(self.URL)

    def anime_opening(self):
        soup = BeautifulSoup(self.page.content, 'html.parser')
        openings = soup.find_all('div', class_='theme-songs js-theme-songs opnening')[0]
        ops = openings.find_all('span', class_='theme-song-index')
        print(ops)
        if len(ops) == 0:
            self.title = openings.find_all('span',class_='theme-song-title')[0].text.strip()
            self.artist = openings.find_all('span',class_='theme-song-artist')[0].text.strip()

            self.title = self.title.replace('"','')
            self.artist = self.artist.split(' ')[1] 
        # else:
            # self.titles = openings.find_all('span')
             


    def __str__(self):
        return self.name