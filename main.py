import re

from models.crawler import Crawler
from models.film import Film, FilmFile
from utils import REGEX
root = "/mnt/d/Films"

c = Crawler(root)

f = FilmFile.random(c.movies)
ff = Film("continent", "country","director","title","year",f)



films = list()

for movie in c.movies:
    matches = re.findall(REGEX, movie)
    if matches:
        films.append(Film(*matches[0][:5], FilmFile(movie)))

print(len(films))