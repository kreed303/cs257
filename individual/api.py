# Music Genre API Assignment
# Written by Katelyn Reed, April 2025
# Rough structure borrowed from flask_sample.py from Jeff's repo

import sys
import os
import argparse
import flask # type: ignore
import json
import csv

app = flask.Flask(__name__)

DATABASE = os.path.join('/home/kreed303/SoftwareDesign-CS257/cs257/data/songs.csv')

@app.route("/")
def home():
    return "Welcome to the music library!"

@app.route("/genre/<genre>")
def getGenre(genre):
    genre = genre.capitalize()
    genreSongs = []
    
    with open(DATABASE) as songsDB:
        songsList = csv.reader(songsDB)

        for song in songsList:
            if song[9] == genre:
                songDict = {"title": song[4].strip()}
                genreSongs.append(songDict)

    return json.dumps(genreSongs, ensure_ascii=False)

@app.route("/help")
def getHelp():
    return flask.render_template('help.html')


if __name__ == '__main__':
    parser = argparse.ArgumentParser('A sample Flask application/API')
    parser.add_argument('host', help='the host on which this application is running')
    parser.add_argument('port', type=int, help='the port on which this application is listening')
    arguments = parser.parse_args()
    app.run(host=arguments.host, port=arguments.port, debug=True)