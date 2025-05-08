import flask
import os
import psycopg2
import config
import sys
import json
import random

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




def getConnection():
    try:
        return psycopg2.connect(database=config.database,
                                user=config.user,
                                password=config.password)
    except Exception as e:
        print(e, file=sys.stderr)
        exit()

print("here")
print(getSongsFromArtist('abbA', shuffle= False))



