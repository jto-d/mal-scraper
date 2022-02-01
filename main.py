import requests
from bs4 import BeautifulSoup as bs
import json

URL = "https://myanimelist.net/animelist/Robbery92?status=2"
page = requests.get(URL)

soup = bs(page.content, 'html.parser')

container = soup.find(id="list-container")
print(container.find_all(class_="list-block"))


# anime_info = soup.find_all("table")

# anime_list = soup.find_all("tbody", class_="list-item")
# for element in anime_list:
#     print(element, end="/n"*2 )