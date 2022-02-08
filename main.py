
from Anime import Anime
from List import List
import time

lists = List('MAL', 'Lxmonade')
lists.get_anime_list()
print(lists.animes)

# ANIME_LIST = 'https://myanimelist.net/animelist/Lxmonade?status=2'

# text = urlopen(ANIME_LIST).read()
# text = text.decode("utf-8")
# text = text.replace("&quot;",'"')

# titles = text.split('"anime_title"')
# titles.pop(0)

# def animeTitle(title):
#     anime_name = title.split('"')[1]
#     if anime_name == 'anime_title_eng':
#         return title.split(',',)[0][1:]
    
#     # apostrophe instead of text
#     if '&#039;' in anime_name:
#         return anime_name.replace('&#039;', "'")
#     return anime_name

# animes = [animeTitle(title) for title in titles]


# r_URLs = text.split('"anime_url"')
# r_URLs.pop(0)

# def animeURL(init_URL):
#     URL = init_URL.replace('\\','')
#     URL = URL.split('"')[1]
#     return "https://myanimelist.net" + URL

# URLs = [animeURL(URL) for URL in r_URLs]

# open txt file
f = open('anime_openings_1.txt', 'w', encoding='utf-8')



# IMPORTANT
# LIKELY NEED TO ADD A TIMER BECAUSE OF RATE LIMITING
for i in range(len(animes)):
    anime = Anime(animes[i], URLs[i])
    try:
        anime.anime_opening()
    except:
        print('\nMAL LIMIT\n60 SECOND PAUSE\nINDEX NUMBER: ' + i + '\nSUBMIT MAL CHECK\n')
        time.sleep(60)
        anime.anime_opening()
    f.write(str(anime)+'\n')
    print(str(anime))        
    if anime.titles != []:
        print("COMPLETING....")
        for op in range(len(anime.titles)):
            f.write(str(op+1) + ': ' + anime.titles[op] + ' by ' + anime.artists[op] + '\n')
    else:
        f.write("No Openings\n")
        print("NO OPENINGS")
    f.write('\n')

f.close()



