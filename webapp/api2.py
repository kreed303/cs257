# Previous versions of some API code that we are hanging onto for now, but are not used in the actual webapp


import flask
import os
import psycopg2
import config
import sys
import json
import random
from helperFunctions import _getSongID, getConnection, _getPlaylistID, _getAlbumID, _getArtistID

app = flask.Flask(__name__)




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

@api.route('/1.0/play/<songId>')
def playSong(songId):
    pygame.mixer.init()
    pygame.mixer.music.load(f"musicFiles/{songId}.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)

@app.route('/api/1.0/artists/<artist>?shuffle=shuffle')
def getSongsFromArtist(artist, shuffle=False):
    conn = getConnection()
    curs = conn.cursor()
    query = '''SELECT songs.songid, songs.songname, songs.tracknumber, songs.songlength, songs.songbpm FROM songs
        JOIN artistssongs ON artistssongs.songid = songs.songid
        JOIN artists ON artists.artistid = artistssongs.artistid
        JOIN artistsalbums ON artists.artistid = artistsalbums.artistid
        WHERE LOWER(artists.artistname) = LOWER(%s)
        ORDER BY artists.artistid DESC, artistsalbums.albumid DESC;'''
    curs.execute(query, (artist, ))
    songs = []
    for row in curs:
        songDict = {'songID': row[0], 'songName': row[1], 'trackNumber': row[2], 'songLength': row[3], 'songBPM': row[4]}
        songs.append(songDict)
    if shuffle:
        random.shuffle(songs)
    curs.close()
    conn.close()

    return json.dumps(songs)

def createPlaylist(playlistName):
    '''
    create playlist method where playlistID is the length of playlists table + 1
    prints error if the playlist already exists 
    input: playlist name
    return: none
    '''

    conn = getConnection()
    curs = conn.cursor()

    # get playlistID
    getPlaylistID = 'SELECT COUNT(*) FROM playlists'
    curs.execute(getPlaylistID)
    playlistID = curs.fetchone()[0] + 1
    

    # Check if playlist exists
    checkPlaylistName = 'SELECT count(*) FROM playlists WHERE playlistName = %s'
    curs.execute(checkPlaylistName, (playlistName, ))
    if curs.fetchone()[0] > 0:
        print("this playlist already exists")
    else:
        # create and commit playlist
        createPlaylist = '''INSERT INTO playlists (playlistid, playlistname)
            VALUES (%s, %s)'''
        print(f"playlist ID: {playlistID}, playlist name: {playlistName}")
        curs.execute(createPlaylist, (playlistID, playlistName))
        conn.commit()
    
    curs.close()
    conn.close()

def addSongToPlaylistFromIDs(playlistID, songID):
    '''
    adds song to a playlist based on songID
    NOTE: doesn't prevent/warn user from adding the same song twice
    input: playlist name
    return: none
    '''
    conn = getConnection()
    curs = conn.cursor()

    # add song and commit
    addSong = '''INSERT INTO playlistssongs (playlistid, songid)
        VALUES (%s, %s);'''
    curs.execute(addSong, (playlistID, songID))
    
    conn.commit()
    
    curs.close()
    conn.close()

def addSongToPlaylistFromNames(playlistName, songName):
    '''
    Alternate way to add song from playlist, probably the way prefered by the user
    input: playlistname, song name
    return: none
    '''

    # setup
    playlistID = _getPlaylistID(playlistName)
    songID = _getSongID(songName)

    # add song
    addSongToPlaylistFromIDs(playlistID, songID)
    print(f"songName {songName}, playlistName {playlistName}")


def addSongToAlbum(songName, albumID, albumName):
    assert (albumName != None) or (albumID != None):
        pass

def createSong(songName, trackNumber, artistName = None, artistID = None, SongLength = 0, songBPM = 0, albumName = None, albumID = None):
    '''
    create playlist method where playlistID is the length of playlists table + 1
    prints error if the playlist already exists 
    input: playlist name
    return: none
    '''
    assert (artistName != None) or (artistID != None)
    conn = getConnection()
    curs = conn.cursor()

    # get songID
    getSongID = 'SELECT COUNT(*) FROM songs'
    curs.execute(getSongID)
    songID = curs.fetchone()[0] + 1
    

    # Check if song exists
    checkSongName = 'SELECT count(*) FROM songs WHERE songName = %s'
    curs.execute(checkSongName, (songName, ))
    if curs.fetchone()[0] > 0:
        matchID = _getSongID(songName)
        # Check if song matches previous artist
        checkArtistName = ''' SELECT COUNT(*) FROM artists
            JOIN artistssongs ON artistssongs.artistid = artists.artistid
            WHERE songs.songid = %s'''
        curs.execute(checkArtistName, matchID)
        if curs.fetchone()[0] > 0:
            print('This song matches both in artist and name a previous song in the database')
            curs.close()
            conn.close()
            return

    # create and commit song into songs
    createSong = '''INSERT INTO songs (songid, songname, tracknumber, songlength, songbpm)
        VALUES (%s, %s, %s, %s, %s)'''
    curs.execute(createSong, (songID, songName, trackNumber, SongLength, songBPM))

    # add song to songsartists
    if artistID == None:
        artistID = _getArtistID(artistName)
    
    addToArtists = '''INSERT INTO artistssongs (artistid, songid)
        VALUES (%s, %s)
        '''
    curs.execute(addToArtists, (artistID, songID))

    # add song to album
    if (albumName != None) or (albumID != None):
        if albumID == None:
            albumID = _getAlbumID(albumName)
        
        addToAlbums = '''INSERT INTO albumsSongs (albumid, songid)
        VALUES (%s, %s)
        '''
        curs.execute(addToAlbums, (albumID, songID))


    conn.commit()
    
    curs.close()
    conn.close()


# addSongToPlaylist(1,1)
print(_getSongID("Take a Chance on Me"))


createSong("yay", "1" , artistName= "ABBA")