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

from helperFunctions import *

app = flask.Flask(__name__, static_folder='static', template_folder='templates')


# 
# ---------------------
# stuff that has to do with artists
# 

@app.route('/1.0/artists')
def getArtists():
    '''
    This allows the user to get a list of all available artists
    INPUT: NONE
    RETURN: all names of artists and their associated information
    '''
    conn = getConnection()
    curs = conn.cursor()

    # the query and retrieval
    query = 'select * from artists'
    curs.execute(query)
    tables = curs.fetchall()

    # formatting return list
    artists = []
    for artist in tables:
        artistDict = {'artistID': artist[0], 'artistName': artist[1]}  
        artists.append(artistDict)

    conn.close()
    curs.close()

    return json.dumps(artists)

@app.route('/1.0/artists/<artistName>')
def getAlbumsFromArtist(artistName):
    '''
    This allows the user to get a list of all available albums from a specific artist
    INPUT: the name of the artist
    RETURN: all names of albums and their associated information by the specified artist
    '''
    # create and run query
    conn = getConnection()
    curs = conn.cursor()
    query = '''SELECT albums.albumid, albums.albumname, albums.albumyear
            FROM albums
            JOIN artistsalbums ON artistsalbums.albumid = albums.albumid
            JOIN artists ON artists.artistid = artistsalbums.artistid
            WHERE LOWER(artists.artistname) = LOWER(%s);'''
    curs.execute(query, (artistName,))
    albumsTuples = curs.fetchall()

    # organize data
    albums = []
    for i in albumsTuples:
            albums.append({'albumID': i[0], 'albumName': i[1], 'albumYear': i[2]})
    albums = sorted(albums, key=lambda x: (x['albumName']))

    return json.dumps(albums)

@app.route('/1.0/artists/<artistName>/songs') 
def getSongsFromArtist(artistName, shuffle=None):
    '''
    This allows the user to get a list of all available songs by a specific artist
    INPUT: the specified artist
    RETURN: all names of artists and their associated information
    '''
    shuffle = flask.request.args.get('shuffle', default = 'false').lower() in ('true','t') if shuffle is None else shuffle

    # create and run query
    conn = getConnection()
    curs = conn.cursor()
    query = ''' SELECT songs.songid, songs.songname, songs.tracknumber, 
            songs.songlength, songs.songbpm FROM songs
            JOIN artistssongs ON artistssongs.songid = songs.songid
            JOIN artists ON artists.artistid = artistssongs.artistid
            JOIN artistsalbums ON artists.artistid = artistsalbums.artistid
            JOIN albums ON albums.albumid = artistsalbums.albumid
            JOIN albumssongs ON albumssongs.albumid=albums.albumid 
            AND albumssongs.songid=songs.songid
            WHERE LOWER(artists.artistname) = LOWER(%s)
            ORDER BY albums.albumname,
            songs.tracknumber;'''
    
    curs.execute(query, (artistName, ))
    songsTuples = curs.fetchall()
    songs = []

    # organize data
    for row in songsTuples:
        songs.append({'songID': row[0], 'songName': row[1], 
                    'trackNumber': row[2], 'songLength': row[3], 'songBPM': row[4]})
    if shuffle:
        random.shuffle(songs)

    curs.close()
    conn.close()

    return json.dumps(songs)

@app.route('/1.0/artists/<artistName>/<albumName>')
def getSongsFromAlbumThroughArist(artistName, albumName, shuffle=None):
    '''
    This allows the user to get a list of all available songs in a specific album by an artist
    INPUT: the name of the artist and the album
    RETURN: all names of songs and their associated information based on the provided data
    '''
    return getSongsFromAlbum(albumName, shuffle = shuffle)

#
# --------------------------
# Stuff that has to do with albums
# 
@app.route('/api/1.0/albums')
def getAlbums():
    '''
    This allows the user to get a list of all available albums
    INPUT: NONE
    RETURN: all names of albums and their associated information
    '''

    # create and run query
    conn = getConnection()
    curs = conn.cursor()
    curs.execute("SELECT * FROM albums;")
    albumsTuples = curs.fetchall()
    albums = []

    # organize data
    for i in albumsTuples:
        albums.append({'albumID': i[0], 'albumName': i[1], 'albumYear': i[2]})
        
    conn.close()
    curs.close()

    return json.dumps(albums)

@app.route('/1.0/albums/<albumName>')
def getSongsFromAlbum(albumName, shuffle=None):
    '''
    This allows the user to get a list of all available songs in a specific album
    INPUT: albumName
    RETURN: all names of songs and their associated information in a specific album
    '''
    shuffle = flask.request.args.get('shuffle', default = 'false').lower() in ('true','t') if shuffle is None else shuffle
    
    # Get data from database
    conn = getConnection()
    curs = conn.cursor()

    query = '''SELECT songs.songid, songs.songname, songs.tracknumber, 
            songs.songlength, songs.songbpm FROM songs
            JOIN albumssongs ON albumssongs.songid = songs.songid
            JOIN albums ON albums.albumid = albumssongs.albumid
            WHERE LOWER(albums.albumName) = LOWER(%s)'''

    curs.execute(query, (albumName,))
    songsTuples = curs.fetchall()

    # Turn into list of dictionaries
    songs = []
    for i in songsTuples:
        songs.append({'songID': i[0], 'songName': i[1], 'trackNumber': i[2], 
                      'songLength': i[3], 'songBPM': i[4]})
        
    # Order or shuffle list
    if shuffle:
        random.shuffle(songs)
    else: 
        songs = sorted(songs, key=lambda x: (x['trackNumber']))

    conn.close()
    curs.close()

    return json.dumps(songs)

#
# -------------------------
# stuff that has to do with songs
#

@app.route('/1.0/songs')
def getSongs(shuffle=None):
    '''
    This allows the user to get a list of all available songs
    INPUT: NONE
    RETURN: all names of songs and their associated information
    '''
    shuffle = flask.request.args.get('shuffle', default = 'false').lower() in ('true','t') if shuffle is None else shuffle

    # create and run query
    conn = getConnection()
    curs = conn.cursor()
    getSongsQuery = '''SELECT songs.songid, songs.songname, songs.tracknumber, 
            songs.songlength, songs.songbpm FROM songs;
        '''
    curs.execute(getSongsQuery)
    songs = []

    # organize songs
    for row in curs:
        songs.append({'songID': row[0], 'songName': row[1], 
                    'trackNumber': row[2], 'songLength': row[3], 'songBPM': row[4]})
    if shuffle:
        random.shuffle(songs)
    else: 
        songs = sorted(songs, key=lambda x: (x['songName']))
    
    curs.close()
    conn.close()

    return json.dumps(songs)


# Other useful functions
@app.route('/1.0/menu')
def getMenuHTML():
    return json.dumps("menu.html")


# From Jeff's API code
if __name__ == '__main__':
    parser = argparse.ArgumentParser('A sample Flask application/API')
    parser.add_argument('host', help='the host on which this application is running')
    parser.add_argument('port', type=int, help='the port on which this application is listening')
    arguments = parser.parse_args()
    app.run(host=arguments.host, port=arguments.port, debug=True)
