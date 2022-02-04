from msilib.schema import Error
from urllib.request import urlopen
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

        self.titles = []
        self.artists = []

    def get_opening_info(self, opening):
        try:
            title = opening.find_all('span', class_='theme-song-title')[0].text.strip()
        except:
            title = opening.find_all('span',class_='theme-song-artist')[0].previous_sibling.text.strip()
        artist = opening.find_all('span',class_='theme-song-artist')[0].text.strip()
                    
        self.titles.append(title.replace('"',''))
        self.artists.append(artist.split(' ',1)[1])

    def anime_opening(self):
        soup = BeautifulSoup(self.page.content, 'html.parser')
        container = soup.find_all('div', class_='theme-songs js-theme-songs opnening')[0]
        openings = container.find_all('tr')[2:]

        if len(openings) == 1:
            if openings[0].find_all('span',class_='theme-song-artist') != []:
                self.get_opening_info(openings[0])
        else:
            for opening in openings:
                index = opening.find_all('span', class_='theme-song-index')
                if index == []:
                    self.get_opening_info(opening)
                    continue
                index_sibling = index[0].next_sibling
                if index_sibling.strip() != '':
                    artist = opening.find_all('span',class_='theme-song-artist')[0].text.strip()
                    
                    self.titles.append(index_sibling.text.strip().replace('"',''))
                    self.artists.append(artist.split(' ',1)[1])
                else:
                    self.get_opening_info(opening)
                    

    


    def __str__(self):
        return self.name