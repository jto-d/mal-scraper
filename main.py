
from Anime import Anime
from List import List
import time

lists = List('Anilist', 'Lxmonade')
lists.get_anime_list()
print(len(lists.animes))
print(lists.animes[0])

# open txt file
f = open('anime_openings_1.txt', 'w', encoding='utf-8')



# IMPORTANT
# LIKELY NEED TO ADD A TIMER BECAUSE OF RATE LIMITING
# for i in range(len(animes)):
#     anime = Anime(animes[i], urls[i])
#     try:
#         anime.anime_opening()
#     except:
#         print('\nMAL LIMIT\n60 SECOND PAUSE\nINDEX NUMBER: ' + i + '\nSUBMIT MAL CHECK\n')
#         time.sleep(60)
#         anime.anime_opening()
#     f.write(str(anime)+'\n')
#     print(str(anime))        
#     if anime.titles != []:
#         print("COMPLETING....")
#         for op in range(len(anime.titles)):
#             f.write(str(op+1) + ': ' + anime.titles[op] + ' by ' + anime.artists[op] + '\n')
#     else:
#         f.write("No Openings\n")
#         print("NO OPENINGS")
#     f.write('\n')

# f.close()



