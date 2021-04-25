import os
from flask import Flask, render_template, send_file
app = Flask(__name__)

from models.crawler import Crawler
from models.film import Film, FilmFile
from time import sleep

ROOT = "/mnt/d/Films"

c = Crawler(ROOT)

def get_movie_and_save_still(path):


    try:
        f = FilmFile.random(c.movies)
        f.save_still(path)
        return f.filepath
    except:
        return get_movie_and_save_still(path)



@app.route("/")
def index():
    # try:
    #     os.remove("images/a.jpg")
    # except OSError:
    #     pass
    movie_path = get_movie_and_save_still("front/images/a.jpg")
    # while not os.path.exists("front/images/a.jpg"):
    #     sleep(1)
    return render_template("index.html", movie_path=movie_path)

@app.route("/picture")
def get_picture():
    return send_file("images/a.jpg", mimetype='image/jpeg')