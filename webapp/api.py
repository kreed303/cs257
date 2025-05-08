# Music Library API
# Katelyn Reed & Sam Reiter


import os
import argparse
import flask # type: ignore
import json
import csv
import sys
import psycopg2
import config
import pdb
import random

from itertools import groupby
from collections import defaultdict


app = flask.Flask(__name__)

# @app.route('api/1.0')
def home():
    conn = getConnection()
    curs = conn.cursor()

    curs.execute("SELECT tablename FROM pg_tables " \
                "WHERE tableowner = 'reedk2';")
    tables = curs.fetchall()
    
    conn.close()
    curs.close()

    # print(json.dumps(tables))

    # Returns list of single element lists with names of tables
    return json.dumps(tables) 


@app.route('/api/1.0/artists')
def getArtists():
    conn = getConnection()
    curs = conn.cursor()
    query = 'select * from artists'
    curs.execute(query)
    tables = curs.fetchall()
    artists = []
    for artist in tables:
        print(artist)
        artistDict = {'artistID': artist[0], 'artistName': artist[1]}  
        artists.append(artistDict)

    conn.close()
    curs.close()

    return json.dumps(artists)


@app.route('/api/1.0/artists/<artist>?shuffle=shuffle')
def getSongsFromArtist(artist, shuffle=False):
    conn = getConnection()
    curs = conn.cursor()
    query = '''SELECT songs.songid, songs.songname, songs.tracknumber, 
            songs.songlength, songs.songbpm FROM songs
            JOIN artistssongs ON artistssongs.songid = songs.songid
            JOIN artists ON artists.artistid = artistssongs.artistid
            JOIN artistsalbums ON artists.artistid = artistsalbums.artistid
            WHERE LOWER(artists.artistname) = LOWER(%s)
            ORDER BY artists.artistid DESC, artistsalbums.albumid DESC;'''
    curs.execute(query, (artist, ))
    songs = []
    for row in curs:
        songDict = {'songID': row[0], 'songName': row[1], 
                    'trackNumber': row[2], 'songLength': row[3], 'songBPM': row[4]}
        songs.append(songDict)
    if shuffle:
        random.shuffle(songs)
    curs.close()
    conn.close()

    return json.dumps(songs)


# @app.route('api/1.0/albums')
def getAlbums():
    conn = getConnection()
    curs = conn.cursor()

    curs.execute("SELECT * FROM albums;")
    albumsTuples = curs.fetchall()
    albums = []

    for i in albumsTuples:
        albums.append({'albumID': i[0], 'albumName': i[1], 'albumYear': i[2]})
        
    conn.close()
    curs.close()

    print(albums)
    # return json.dumps(albums)

# @app.route('/api/1.0/albums/<album>?shuffle=shuffle&tags=tags&contains=contains')
def getSongsFromAlbum(album, shuffle=False, tags = "", contains = ""):
    conn = getConnection()
    curs = conn.cursor()

    query = '''SELECT songs.songid, songs.songname, songs.tracknumber, 
            songs.songlength, songs.songbpm FROM songs
            JOIN albumssongs ON albumssongs.songid = songs.songid
            JOIN albums ON albums.albumid = albumssongs.albumid
            WHERE LOWER(albums.albumName) = LOWER(%s)'''
    
    curs.execute(query, (album,))
    songsTuples = curs.fetchall()

    songs = []
    for i in songsTuples:
        songs.append({'songID': i[0], 'songName': i[1], 'trackNumber': i[2], 
                      'songLength': i[3], 'songBPM': i[4]})
        
    if shuffle:
        random.shuffle(songs)

    conn.close()
    curs.close()
   
    # return json.dumps(songs)


# Helper function to create psycopg2 connection object
def getConnection():
    try:
        return psycopg2.connect(database=config.database,
                                user=config.user,
                                password=config.password)
    except Exception as e:
        print(e, file=sys.stderr)
        exit()
    


# From Jeff's API code
# if __name__ == '__main__':
#     parser = argparse.ArgumentParser('A sample Flask application/API')
#     parser.add_argument('host', help='the host on which this application is running')
#     parser.add_argument('port', type=int, help='the port on which this application is listening')
#     arguments = parser.parse_args()
#     app.run(host=arguments.host, port=arguments.port, debug=True)