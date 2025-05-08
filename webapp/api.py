# Music Library API
# Katelyn Reed & Sam Reiter


'''
GET:
home 
artists 
artist -> all albums
*artist -> songs from an album TAG LOGIC
albums
*album -> all songs TAG LOGIC
tags
*tag -> all songs
*tag -> all artists
*tag -> all albums
*tag -> all playlists
playlists
*playlist - all songs

CREATE:
playlist
tag
tag entries?
'''

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


# app = flask.Flask(__name__)

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


# @app.route('/api/1.0/artists')
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


# @app.route('/api/1.0/artists/<artist>?shuffle=shuffle&tags=tags&contains=contains')
def getSongsFromArtist(artist, shuffle=False, tags = '', contains = ''):
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
        songs.append({'songID': row[0], 'songName': row[1], 
                    'trackNumber': row[2], 'songLength': row[3], 'songBPM': row[4]})
    
    if shuffle:
        random.shuffle(songs)
    else: 
        songs = sorted(songs, key=lambda x: (x['trackNumber']))

    # ADD LOGIC ABOUT TAGS AND CONTAINS
    
    curs.close()
    conn.close()

    return json.dumps(songs)

# ADD THIS API (just returns albums of a particular artist, not songs)
# @app.route('/api/1.0/artists/<artist>?')
def getAlbumsFromArtist(artist):
    conn = getConnection()
    curs = conn.cursor()

    query = '''SELECT albums.albumid, albums.albumname, albums.albumyear
            FROM albums
            JOIN artistsalbums ON artistsalbums.albumid = albums.albumid
            JOIN artists ON artists.artistid = artistsalbums.artistid
            WHERE LOWER(artists.artistname) = LOWER(%s);'''

    curs.execute(query, (artist,))
    albumsTuples = curs.fetchall()
    albums = []

    for i in albumsTuples:
            albums.append({'albumID': i[0], 'albumName': i[1], 'albumYear': i[2]})
    albums = sorted(albums, key=lambda x: (x['albumName']))

    return json.dumps(albums)
    
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

    # print(albums)
    return json.dumps(albums)

# @app.route('/api/1.0/albums/<album>?shuffle=shuffle&tags=tags&contains=contains')
def getSongsFromAlbum(album, shuffle=False, tags = "", contains = ""):
    conn = getConnection()
    curs = conn.cursor()
    tagsList = tags.split()
    containsList = contains.split()

    query = '''SELECT songs.songid, songs.songname, songs.tracknumber, 
            songs.songlength, songs.songbpm FROM songs
            JOIN albumssongs ON albumssongs.songid = songs.songid
            JOIN albums ON albums.albumid = albumssongs.albumid
            WHERE LOWER(albums.albumName) = LOWER(%s)'''

    # Figure out logic for how to isolate songs based on tags
    if (tags):
        query = '''SELECT songs.songid, songs.songname, songs.tracknumber, 
                songs.songlength, songs.songbpm FROM songs
                JOIN albumssongs ON albumssongs.songid = songs.songid
                JOIN albums ON albums.albumid = albumssongs.albumid
                WHERE LOWER(albums.albumName) = LOWER(%s)'''

    curs.execute(query, (album,))
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

    print(songs)
    # return json.dumps(songs)

# @app.route('/api/1.0/tags')
def getTags():
    conn = getConnection()
    curs = conn.cursor()

    curs.execute("SELECT * FROM tags;")
    tagsTuples = curs.fetchall()
    tags = []

    for i in tagsTuples:
        tags.append({'tagID': i[0], 'tagName': i[1]})
        
    conn.close()
    curs.close()

    # print(tags)
    return json.dumps(tags)

# @app.route('/api/1.0/playlists')
def getPlaylists():
    conn = getConnection()
    curs = conn.cursor()

    curs.execute("SELECT * FROM playlists;")
    playlistsTuples = curs.fetchall()
    playlists = []

    for i in playlistsTuples:
        playlists.append({'playlistID': i[0], 'playlistName': i[1]})
        
    conn.close()
    curs.close()

    # print(playlists)
    return json.dumps(playlists)


# @app.route('/api/1.0/playlists/<playlist>?shuffle=shuffle&tags=tags&contains=contains')
def getSongsfromPlaylist(playlist, shuffle = False, tags = "", contains = ""):
    conn = getConnection()
    curs = conn.cursor()
    tagsList = tags.split()
    containsList = contains.split()

    query = '''SELECT songs.songid, songs.songname, songs.tracknumber, 
            songs.songlength, songs.songbpm FROM songs
            JOIN playlistssongs ON playlistssongs.songid = songs.songid
            JOIN playlists ON playlists.playlistid = playlistssongs.playlist.id
            WHERE LOWER(playlists.playlistname) = LOWER(%s);'''
    
    curs.execute(query, (playlist,))
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
        songs = sorted(songs, key=lambda x: (x['playlistOrder']))

    return json.dumps(songs)


# From Jeff's API code
# if __name__ == '__main__':
#     parser = argparse.ArgumentParser('A sample Flask application/API')
#     parser.add_argument('host', help='the host on which this application is running')
#     parser.add_argument('port', type=int, help='the port on which this application is listening')
#     arguments = parser.parse_args()
#     app.run(host=arguments.host, port=arguments.port, debug=True)


# getSongsFromAlbum('Cordial', True)