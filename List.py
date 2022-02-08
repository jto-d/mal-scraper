from Anime import Anime
from bs4 import BeautifulSoup
from urllib.request import urlopen


class List:
    def __init__(self, typ, username) -> None:
        self.type = typ
        self.user = username

        self.animes = []
        self.urls = []

    def get_anime_url(self, init_url):
        url = init_url.replace('\\','')
        url = url.split('"')[1]
        return 'https://myanimelist.net' + url

    def get_anime_title(self, title):
        anime_name = title.split('"')[1]
        if anime_name == 'anime_title_eng':
            return title.split(',',)[0][1:]
        
        # apostrophe instead of text
        if '&#039;' in anime_name:
            return anime_name.replace('&#039;', "'")
        return anime_name

    def get_MAL_list(self):
        for i in range(1,5):
            self.url = 'https://myanimelist.net/animelist/' + self.user + '?status=' + str(i)
            
            text = urlopen(self.url).read()
            text = text.decode("utf-8")
            text = text.replace("&quot;",'"')

            titles = text.split('"anime_title"')
            titles.pop(0)

            self.animes.extend([self.get_anime_title(title) for title in titles])

            init_urls = text.split('"anime_url"')
            init_urls.pop(0)

            self.urls.extend([self.get_anime_url(url) for url in init_urls])

    def get_anime_list(self):
        if self.type == 'MAL':
            self.get_MAL_list()
        # elif self.type == 'Anilist':
            

