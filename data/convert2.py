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


def CSVs(inputFile):
    songs = {}
    artists = {}
    albums = {}
    albumsSongs = []
    artistsAlbums = []
    artistsSongs = []

    with open(inputFile) as f:
        reader = csv.reader(f)
        next(reader)
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
                songs[songKey] = {"songID": len(songs) + 1,
                                  "songName": songName,
                                  "trackNumber": trackNumber,
                                  "songLength": songLength,
                                  "songBPM": 0}
                
            if artistKey not in artists:
                artists[artistKey] = {"artistID": len(artists) + 1,
                                      "artistName": artistName}
                
            if albumKey not in albums:
                albums[albumKey] = {"albumID": len(albums) + 1,
                                    "albumName": albumName,
                                    "albumYear": albumYear}
                
            albumsSongs.append((albums[albumKey]["albumID"], songs[songKey]["songID"]))
            artistsSongs.append((artists[artistKey]["artistID"], songs[songKey]["songID"]))
            if ((artists[artistKey]["artistID"], albums[albumKey]["albumID"]) not in artistsAlbums):
                artistsAlbums.append((artists[artistKey]["artistID"], albums[albumKey]["albumID"]))
    
    with open("songs.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(("songID", "songName", "trackNumber", "songLength", "songBPM"))
        for songKey in songs:
            song = songs[songKey]
            row = (song["songID"], song["songName"], 
                   song["trackNumber"], song["songLength"], song["songBPM"])
            writer.writerow(row)

    with open("albums.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(("albumID", "albumName", "albumYear"))
        for albumKey in albums:
            album = albums[albumKey]
            row = (album["albumID"], album["albumName"], album["albumYear"])
            writer.writerow(row)   

    with open("artists.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(("artistID", "artistName"))
        for artistKey in artists:
            artist = artists[artistKey]
            row = (artist["artistID"], artist["artistName"])
            writer.writerow(row)   


    with open("artistsSongs.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(("artistID", "songID"))
        for artistKey, songKey in artistsSongs:
            writer.writerow((artistKey, songKey))

    with open("albumsSongs.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(("albumsID", "songID"))
        for albumKey, songKey in albumsSongs:
            writer.writerow((albumKey, songKey))

    with open("artistsAlbums.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(("artistID", "albumID"))
        for artistKey, albumKey in artistsAlbums:
            writer.writerow((artistKey, albumKey))


CSVs(sys.argv[1])