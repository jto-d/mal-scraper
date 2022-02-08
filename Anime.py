from msilib.schema import Error
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

class Anime:
    def __init__(self, name, url, typ) -> None:
        self.name = name
        self.url = url
        self.page = requests.get(self.url)
        self.type = typ

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

    def mal_openings(self):
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
    
    def anilist_openings(self):
        soup = BeautifulSoup(self.page.content, 'html.parser')
        container = soup.find_all('div', class_='list-wrap')
        print(container)

    def get_openings(self):
        if self.type == 'MAL':
            self.mal_openings()
        else:
            self.anilist_openings()



      
    def __str__(self):
        return self.name
