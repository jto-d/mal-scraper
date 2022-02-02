import json
import re
from urllib.request import urlopen
from Anime import Anime

ANIME_LIST = 'https://myanimelist.net/animelist/Lxmonade?status=2'

text = urlopen(ANIME_LIST).read()
text = text.decode("utf-8")
text = text.replace("&quot;",'"')

titles = text.split('"anime_title"')
titles.pop(0)

def animeTitle(title):
    anime_name = title.split('"')[1]
    if anime_name == 'anime_title_eng':
        return title.split(',',)[0][1:]
    
    # apostrophe instead of text
    if '&#039;' in anime_name:
        return anime_name.replace('&#039;', "'")
    return anime_name

animes = [animeTitle(title) for title in titles]
# print(animes)

r_URLs = text.split('"anime_url"')
r_URLs.pop(0)

def animeURL(init_URL):
    URL = init_URL.replace('\\','')
    URL = URL.split('"')[1]
    return "https://myanimelist.net" + URL

URLs = [animeURL(URL) for URL in r_URLs]

# print(len(URLs))
# print(len(animes))




for i in range(5):
    anime = Anime(animes[i], URLs[i])
    anime.anime_opening()
    print("Title: " + anime.title + "\nArtist: " + anime.artist)
# print(animes)



