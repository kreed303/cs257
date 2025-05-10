import flask
import os
import psycopg2
from psycopg2 import sql
import config
import sys
import json
import random

def getConnection():
    try:
        return psycopg2.connect(database=config.database,
                                user=config.user,
                                password=config.password)
    except Exception as e:
        print(e, file=sys.stderr)
        exit()

def _get(key, input, request, table):
    conn = getConnection()
    curs = conn.cursor()

    query = sql.SQL('SELECT {request} FROM {table} WHERE {key} = %s').format(request = sql.Identifier(request), table = sql.Identifier(table), key = sql.Identifier(key))

    curs.execute(query, (input, ))
    returnValue = curs.fetchone()[0]

    curs.close()
    conn.close()

    return(returnValue)


def _getPlaylistName(playlistID):
    '''
    Helper Function to return playlist name 
    input: playlistID
    return: playlistName
    '''
    conn = getConnection()
    curs = conn.cursor()

    getPlaylistName = "SELECT playlistName FROM playlists WHERE playlistID = %s"
    curs.execute(getPlaylistName, (playlistID, ))
    playlistName = curs.fetchone()[0]

    curs.close()
    conn.close()

    return(playlistName)
    
def _getPlaylistID(playlistName):
    '''
    Helper Function to return playlistID 
    input: playlistID
    return: playlistName
    '''
    conn = getConnection()
    curs = conn.cursor()

    getPlaylistID = "SELECT playlistName FROM playlists WHERE playlistID = %s"
    curs.execute(getPlaylistID, (playlistName, ))
    playlistID = curs.fetchone()[0]

    curs.close()
    conn.close()

    return(playlistID)

def _getSongID(songName):
    '''
    Helper Function to return songID
    input: songName 
    return: songID
    '''
    conn = getConnection()
    curs = conn.cursor()

    getSongID = "SELECT songID FROM songs WHERE songName = %s"
    curs.execute(getSongID, (songName, ))
    songID = curs.fetchone()[0]

    curs.close()
    conn.close()

    return(songID)


def _getSongName(songID):
    '''
    Helper Function to return song name 
    input: songID
    return: songName
    '''
    conn = getConnection()
    curs = conn.cursor()

    getSongName = "SELECT songname FROM songs WHERE songID = %s"
    curs.execute(getSongName, (songID, ))
    songName = curs.fetchone()[0]

    curs.close()
    conn.close()

    return(songName)

def _getArtistID(artistName):
    '''
    Helper Function to return artistID 
    input: artistName
    return: artistID
    '''
    conn = getConnection()
    curs = conn.cursor()

    getArtistID = "SELECT artistID FROM artists WHERE artistID = %s"
    curs.execute(getArtistID, (artistName, ))
    artistID = curs.fetchone()[0]

    curs.close()
    conn.close()

    return(artistID)

def _getAlbumID(albumName):
    '''
    Helper Function to return albumID 
    input: albumName
    return: albumID
    '''
    conn = getConnection()
    curs = conn.cursor()

    getAlbumID = "SELECT albumID FROM albums WHERE albumName = %s"
    curs.execute(getAlbumID, (albumName, ))
    albumID = curs.fetchone()[0]

    curs.close()
    conn.close()

    return(albumID)


