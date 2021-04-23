import os
from random import choice

from moviepy.editor import VideoFileClip

from utils import *


class FilmFile:

    @classmethod
    def random(cls, available_movies):
        return cls(choice(available_movies))

    def __init__(self, filepath):
        self.filepath = filepath
        self.extension = filepath.split(".")[-1]  # FixMe UGLYYYYY
        self.subclip_start = None
        self._clip = None
        self._subclip = None

    @property
    def clip(self):
        if not self._clip:
            self._clip = VideoFileClip(self.filepath)
        return self._clip

    @property
    def subclip(self):
        if not self._subclip:
            self.subclip_start = chose_start(self.clip.duration)
            self._subclip = self.clip.subclip(self.subclip_start, self.subclip_start + 180)
        return self._subclip

    def __str__(self):
        return self.filepath

    def __repr__(self):
        return self.filepath

    def save_subclip(self, output_path):
        self.subclip.write_videofile(output_path, codec="mpeg4", bitrate="12000k")
        with open(LOG, "a+") as f:
            f.write("\n\nMovie: {}\nStart: {}".format(self.filepath, format_time(self.subclip_start)))
        # os.system('/mnt/c/Program\\ Files/VideoLAN/VLC/vlc.exe "{}" &'.format(output_path))

    def save_still(self, output_path):
        self.subclip.save_frame(output_path, 1)


class Film:

    def __init__(self, continent, country, director, title, year, filmfile):
        self.continent = continent
        self.country = country
        self.director = director
        self.title = title
        self.year = year
        self.filmfile = filmfile

    def ideal_path(self, root):
        title_year = "{} ({})".format(self.title, self.year)
        return os.path.join(root, self.continent, self.country, self.director, title_year,
                            "{}.{}".format(title_year, self.filmfile.extension))
