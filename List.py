from Anime import Anime
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import requests


class List:
    def __init__(self, typ, username) -> None:
        self.type = typ.upper()
        self.user = username

        self.titles = []
        self.urls = []

    def get_anime_url(self, init_url):
        if self.type == 'MAL':
            url = init_url.replace('\\','')
            url = url.split('"')[1]
            return 'https://myanimelist.net' + url
        # elif self.type == 'Anilist':


    def get_anime_title(self, title):
        if self.type == 'MAL':
            anime_name = title.split('"')[1]
            if anime_name == 'anime_title_eng':
                return title.split(',',)[0][1:]
            
            # apostrophe instead of text
            if '&#039;' in anime_name:
                return anime_name.replace('&#039;', "'")
            return anime_name
        # elif self.type == 'ANILIST':



    def get_anilist_list(self):
        
        self.url = 'https://anilist.co/user/' + self.user + '/animelist'
        # req = Request(self.url, headers={'User-Agent': 'Mozilla/5.0'})

        # text = urlopen(req).read()
        # self.text = text.decode("utf-8")
        # self.text = self.text

        page = requests.get(self.url)

        soup = BeautifulSoup(page.content, 'html.parser')
        container = soup.find_all('div', class_='list-wrap')[:4]

        self.animes = []
        
        self.animes.extend(container[1].select('div.row'))
        
            
                


    def get_MAL_list(self):
        for i in range(1,5):
            self.url = 'https://myanimelist.net/animelist/' + self.user + '?status=' + str(i)
            
            text = urlopen(self.url).read()
            text = text.decode("utf-8")
            text = text.replace("&quot;",'"')

            titles = text.split('"anime_title"')
            titles.pop(0)

            self.titles.extend([self.get_anime_title(title) for title in titles])

            init_urls = text.split('"anime_url"')
            init_urls.pop(0)

            self.urls.extend([self.get_anime_url(url) for url in init_urls])

    def get_anime_list(self):
        if self.type == 'MAL':
            self.get_MAL_list()
        elif self.type == 'ANILIST':
            self.get_anilist_list()

            

