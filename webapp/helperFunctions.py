import psycopg2
from psycopg2 import sql
import config
import sys
import pdb

def getConnection():
    '''Returns psycopg2 connection object'''
    try:
        return psycopg2.connect(database=config.database,
                                user=config.user,
                                password=config.password)
    except Exception as e:
        print(e, file=sys.stderr)
        exit()
        
def parseQuery(query, args = None):
    '''
    Query: query in SQL form
    args: a tuple
    '''

    conn = getConnection()
    curs = conn.cursor()
    
    curs.execute(query, args)

    jsonObj = []
    for row in curs:
        jsonDict = dict()
        columns = [desc[0] for desc in curs.description]
        for i in range(len(columns)):
            jsonDict[columns[i]] = row[i]
        jsonObj.append(jsonDict)

    curs.close()
    conn.close()
    return jsonObj

"""
A bunch of Get queries to speed up that process 

"""        

def _get(request, table, key, input, like = False):
    '''Generic get function that takes the specific query parameters and strings them into a correct SQL query'''
    
    conn = getConnection()
    curs = conn.cursor()
    if like:
        query = sql.SQL("SELECT {request} FROM {table} WHERE LOWER({key}) LIKE LOWER(%s)").format(request = sql.Identifier(request.lower()), table = sql.Identifier(table.lower()), key = sql.Identifier(key.lower()))
        curs.execute(query, (f"%{input}%", ))
    else:
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

def _getSongID(songName, like=False):
    '''
    Helper Function to return songID
    input: songName 
    return: songID
    '''
    return _get("songid", "songs", "songname", songName, like = like)


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
    return _get("artistname", "artists", "artistid", artistName)

def _getArtistName(artistID):
    '''
    Helper Function to return artistID 
    input: artistID
    return: artistName
    '''
    return _get("artistname", "artists", "artistid", artistID)

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


if __name__ == "__main__":
    query = '''SELECT 
    songs.songid, songs.songname, songs.tracknumber, songs.songlength, songs.songbpm, artists.artistname, albums.albumname FROM songs
    JOIN albumssongs ON  albumssongs.songid = songs.songid 
    JOIN artistssongs ON songs.songid = artistssongs.songid
    JOIN albums ON albums.albumid = albumssongs.albumid
    JOIN artists ON artists.artistid = artistssongs.artistid'''
    songs = parseQuery(query)
    print(songs)