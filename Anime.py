from urllib.request import urlopen

class Anime:
    def __init__(self, name, URL) -> None:
        self.name = name
        self.URL = URL
        self.page = urlopen(self.URL).read()

    def anime_opening(self):
        self.page = str(self.page)
        self.type = type(self.page)
        self.title = self.page.split('"theme-song-title"')
        self.title = self.title[1].split('"')[1]

        self.artist = self.page.split('"theme-song-artist"')
        self.artist = self.artist[1].split('<')[0][5:]

    def __str__(self):
        return self.name
