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
import pygame # type: ignore
import time

from helperFunctions import *

api = flask.Flask(__name__, static_folder='static', template_folder='templates')
api = flask.Blueprint('api', __name__)


#
# --------------
# The stuff for the links
#

@api.route('/1.0/menuHTML')
def getMenuHTML():
    # f = open("templates/menu.html", "r")
    # x = f.read()
    return flask.render_template('menu.html')



# 
# ---------------------
# stuff that has to do with artists
# 
@api.route('/1.0/artists')
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

@api.route('/1.0/artists/<artistID>')
def getAlbumsFromArtist(artistID):
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
            WHERE artists.artistid = %s;'''
    curs.execute(query, (artistID,))
    albumsTuples = curs.fetchall()

    # organize data
    albums = []
    for i in albumsTuples:
            albums.append({'albumID': i[0], 'albumName': i[1], 'albumYear': i[2]})
    albums = sorted(albums, key=lambda x: (x['albumName']))

    return json.dumps(albums)

@api.route('/1.0/artistssongs/<artistId>') 
def getSongsFromArtist(artistId, shuffle=None):
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
            songs.songlength, songs.songbpm, albums.albumname FROM songs
            JOIN artistssongs ON artistssongs.songid = songs.songid
            JOIN artists ON artists.artistid = artistssongs.artistid
            JOIN artistsalbums ON artists.artistid = artistsalbums.artistid
            JOIN albums ON albums.albumid = artistsalbums.albumid
            JOIN albumssongs ON albumssongs.albumid=albums.albumid 
            AND albumssongs.songid=songs.songid
            WHERE artists.artistid = %s
            ORDER BY albums.albumname,
            songs.tracknumber;'''
    curs.execute(query, (artistId, ))
    songsTuples = curs.fetchall()
    songs = []

    # organize data
    for row in songsTuples:
        songs.append({'songID': row[0], 'songName': row[1], 
                    'trackNumber': row[2], 'songLength': row[3], 'songBPM': row[4], 'albumName': row[5]})
    if shuffle:
        random.shuffle(songs)

    curs.close()
    conn.close()

    return json.dumps(songs)

#
# --------------------------
# Stuff that has to do with albums
# 
@api.route('/1.0/albums')
def getAlbums():
    '''
    This allows the user to get a list of all available albums
    INPUT: NONE
    RETURN: all names of albums and their associated information
    '''

    # create and run query
    conn = getConnection()
    curs = conn.cursor()
    query = '''
    SELECT albums.albumID, albums.albumName, albums.albumYear, artists.artistName, artists.artistId
    FROM albums
    JOIN artistsalbums ON albums.albumID = artistsalbums.albumID
    JOIN artists ON artistsalbums.artistID = artists.artistID;'''
    curs.execute(query)
    albumsTuples = curs.fetchall()
    albums = []

    # organize data
    for i in albumsTuples:
        albums.append({'albumID': i[0], 'albumName': i[1], 'albumYear': i[2], 'artistName': i[3], 'artistID':i[4]})
        
    conn.close()
    curs.close()

    return json.dumps(albums)

@api.route('/1.0/albums/<albumID>')
def getSongsFromAlbum(albumID, albumName = None, shuffle=None):
    '''
    This allows the user to get a list of all available songs in a specific album
    INPUT: albumName
    RETURN: all names of songs and their associated information in a specific album
    '''

    albumName = flask.request.args.get('albumName', default = None)
    shuffle = flask.request.args.get('shuffle', default = 'false').lower() in ('true','t') if shuffle is None else shuffle

    assert albumID != None or albumName != None    
    # Get data from database
    conn = getConnection()
    curs = conn.cursor()

    if albumID == None:
        albumID = _getAlbumID(albumName)
    if albumName != None:
        albumName = albumName.lower()

    query = '''SELECT songs.songid, songs.songname, songs.tracknumber, 
            songs.songlength, songs.songbpm FROM songs
            JOIN albumssongs ON albumssongs.songid = songs.songid
            JOIN albums ON albums.albumid = albumssongs.albumid
            WHERE albums.albumid = %s'''

    curs.execute(query, (albumID,))
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

def getAlbumArtist(albumID):

    conn = getConnection()
    curs = conn.cursor()

    query = '''SELECT artists.artistname FROM artists
        JOIN artistsalbums ON artistsalbums.artistID = artists.artistID
        JOIN albums ON albums.albumID = artistsalbums.albumID
        WHERE albums.albumid = %s'''
    
    curs.execute(query, (albumID,))
    artistName = curs.fetchall()[0][0]

    conn.close()
    curs.close()

    return artistName


#
# -------------------------
# stuff that has to do with songs
#

@api.route('/1.0/songs')
def getSongs(shuffle=None):
    '''
    This allows the user to get a list of all available songs
    INPUT: NONE
    RETURN: all names of songs and their associated information
    '''
    # shuffle = flask.request.args.get('shuffle').lower() in ('true', 't')
    shuffle = flask.request.args.get('shuffle', default = 'false').lower() in ('true','t') if shuffle is None else shuffle
    # create and run query
    conn = getConnection()
    curs = conn.cursor()
    getSongsQuery = '''SELECT 
    songs.songid, songs.songname, songs.tracknumber, songs.songlength, songs.songbpm, artists.artistname, albums.albumname FROM songs
    JOIN albumssongs ON  albumssongs.songid = songs.songid 
    JOIN artistssongs ON songs.songid = artistssongs.songid
    JOIN albums ON albums.albumid = albumssongs.albumid
    JOIN artists ON artists.artistid = artistssongs.artistid'''
    curs.execute(getSongsQuery)
    songs = []

    # organize songs
    for row in curs:
        songs.append({'songID': row[0], 'songName': row[1], 
                    'trackNumber': row[2], 'songLength': row[3], 'songBPM': row[4], 'artistName': row[5], 'albumName': row[6]})
    if shuffle:
        random.shuffle(songs)
    else: 
        songs = sorted(songs, key=lambda x: (x['songName']))
    


    return json.dumps(songs)

@api.route('/1.0/songs/<songID>')
def getSong(songID):
    conn = getConnection()
    curs = conn.cursor()
    getSongsQuery = '''SELECT songs.songid, songs.songname, songs.tracknumber, songs.songlength, songs.songbpm, artists.artistname, albums.albumname FROM songs
    JOIN albumssongs ON  albumssongs.songid = songs.songid 
    JOIN artistssongs ON songs.songid = artistssongs.songid
    JOIN albums ON albums.albumid = albumssongs.albumid
    JOIN artists ON artists.artistid = artistssongs.artistid
    WHERE songs.songid = %s'''
    curs.execute(getSongsQuery, (songID, ))
    song = curs.fetchone()
    songDict = dict()
    columns = [desc[0] for desc in curs.description]
    for i in range(len(columns)):
        songDict[columns[i]] = song[i]
    songDict = [songDict]

    curs.close()
    conn.close()
    print(songDict)
    return json.dumps(songDict)




# From Jeff's API code
# if __name__ == '__main__':
#     parser = argparse.ArgumentParser('A sample Flask application/API')
#     parser.add_argument('host', help='the host on which this application is running')
#     parser.add_argument('port', type=int, help='the port on which this application is listening')
#     arguments = parser.parse_args()
#     api.run(host=arguments.host, port=arguments.port, debug=True)
