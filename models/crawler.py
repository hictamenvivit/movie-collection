import os
from functools import reduce
from operator import add

extensions = [".mkv", ".mp4", ".avi", ".m4v"] #FixMe chage that !!

def find_movies(path, liste=None):
    if liste is None:
        liste = list()
    if os.path.isdir(path):
        return reduce(add, [find_movies(os.path.join(path, child), liste) for child in os.listdir(path)], list())
    else:
        if any(path.endswith(e) for e in extensions):
            return [path]
    return list()


class Crawler:

    def __init__(self, root):
        self.root = root
        self.movies = find_movies(self.root)
