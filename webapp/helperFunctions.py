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

def _get(request, table, key, input):
    conn = getConnection()
    curs = conn.cursor()

    query = sql.SQL("SELECT {request} FROM {table} WHERE {key} = %s").format(request = sql.Identifier(request.lower()), table = sql.Identifier(table.lower()), key = sql.Identifier(key.lower()))

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
    return _get("playlistName", "playlists", "playlistId", playlistID)
    
def _getPlaylistID(playlistName):
    '''
    Helper Function to return playlistID 
    input: playlistID
    return: playlistName
    '''
    return _get("playlistid", "playlists", "playlistname", playlistName)

def _getSongID(songName):
    '''
    Helper Function to return songID
    input: songName 
    return: songID
    '''
    return _get("songid", "songs", "songname", songName)


def _getSongName(songID):
    '''
    Helper Function to return song name 
    input: songID
    return: songName
    '''
    return _get("songname", "songs", "songid", songID)

def _getArtistID(artistName):
    '''
    Helper Function to return artistID 
    input: artistName
    return: artistID
    '''
    return _get("artistId", "artists", "artistName", artistName)

def _getAlbumName(albumID):
    '''
    Helper Function to return albumID 
    input: albumName
    return: albumID
    '''
    return _get("albumName", "albums", "albumID", albumID)

def _getAlbumID(albumName):
    '''
    Helper Function to return albumID 
    input: albumName
    return: albumID
    '''
    return _get("albumID", "albums", "albumName", albumName)


