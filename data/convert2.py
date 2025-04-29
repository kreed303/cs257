import sys
import csv
import os
import pandas as pd
import pdb


def songsCSV(inputfile):
    metaData = pd.read_csv(inputfile)
    songIDs = [i for i in range(len(metaData))]
    songNames = metaData["title"]
    trackNumbers = metaData["tracknumber"]
    songLengths = metaData["length"]
    songBPMs = []

    newDF = pd.DataFrame([songIDs, songNames, trackNumbers, songLengths, songBPMs],
                         index = ["songID", "songName", "trackNumber", "songLength", "songBPM"]).T
    newDF.to_csv("songs.csv", index=False)

def albumsSongsCSV(albumsCSV, songsCSV):
    albums = pd.read_csv(albumsCSV)
    songs = pd.read_csv(songsCSV)
    
    newDF = pd.DataFrame([albums["albumID"], songs["songID"]], index = ["albumID", "songID"]).T
    newDF.to_csv("albumsSongs.csv", index=False)

def artistsSongsCSV(metaDataCSV, artistsCSV, songsCSV):
    metaData = pd.read_csv(metaDataCSV)
    artistIDS = pd.read_csv(artistsCSV)
    songIDS = pd.read_csv(songsCSV)
    artists = metaData["artist"]
    songs = metaData["title"]

    newDF = pd.DataFrame(columns = ["artistID", "songID"])


    for row in range(len(metaData)):
        temp = pd.DataFrame()
        print(metaData["title"][row])
    
    # newDF = pd.DataFrame([artistIDS[artists], songIDS[songs]], index = ["artistID", "songID"]).T
    # newDF.to_csv("artistsSongs.csv", index=False)

def artistsSongsCSV(inputFile):
    # DATABASE = os.path.join(os.getcwd(), '/data/songs.csv')

    songs = {}
    artists = {}
    albums = {}
    albumsSongs = []
    artistsAlbums = []
    artistsSongs = []

    playlists = {}
    tags = {}

    with open(inputFile) as f:
        reader = csv.reader(f)
        for songRow in reader:
            songName = songRow[4]
            albumName = songRow[1]
            artistName = songRow[5]
            trackNumber = songRow[8]
            songLength = songRow[3]
            albumYear = songRow[10]

            songKey = f"{songName}+{albumName}"
            artistKey = f"{artistName}"
            albumKey = f"{albumName}+{artistName}"
            
            # Write stuff to create dictionary entries based on keys
            if songKey not in songs:
                songs[songKey] = {"songID": len(songs),
                                  "songName": songName,
                                  "trackNumber": trackNumber,
                                  "songLength": songLength}
                
            if artistKey not in artists:
                artists[artistKey] = {"artistID": len(artists),
                                      "artistName": artistName}
                
            if albumKey not in albums:
                albums[albumKey] = {"albumID": len(albums),
                                      "albumName": albumName}
                
            albumsSongs.append((albums[albumKey]["albumID"], songs[songKey]["songID"]))
            artistsAlbums.append((artists[artistKey]["artistID"], albums[albumKey]["albumID"]))
            artistsSongs.append((artists[artistKey]["artistID"], songs[songKey]["songID"]))

    with open("artistsSongs.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(("artistID", "songID"))
        for songKey, artistKey in artistsSongs:
            writer.writerow((artistKey, songKey))

    with open("albumsSongs.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(("albumsID", "songID"))
        for albumKey, songKey in albumsSongs:
            writer.writerow((albumKey, songKey))


# songsCSV(sys.argv[1])
# artistsSongsCSV(sys.argv[1], sys.argv[2], sys.argv[3])

artistsSongsCSV(sys.argv[1])