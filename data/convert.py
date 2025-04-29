import sys
import csv
import os
import pandas as pd
import pdb

def artistCSV(inputfile):
    metaData = pd.read_csv(inputfile)
    artists = list(metaData["artist"].unique())
    artistIndex = [i for i in range(len(artists))]
    newDF = pd.DataFrame([artistIndex, artists], index = ["artistIndex", "arist"]).T
    newDF.to_csv("artists.csv", index=False)
    
    # pdb.set_trace()

def albumCSV(inputFile):
    # DATABASE = os.path.join(os.getcwd(), '/data/songs.csv')

    songs = {}
    artists = {}
    albums = {}
    albums_songs = []
    artists_albums = []
    artists_songs = []

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
                
            albums_songs.append((albums[albumKey]["albumID"], songs[songKey]["songID"]))
            artists_albums.append((artists[artistKey]["artistID"], albums[albumKey]["albumID"]))
            artists_songs.append((artists[artistKey]["artistID"], songs[songKey]["songID"]))


    with open("songs.csv", "w") as f:
        writer = csv.writer(f)
        for songKey in songs:
            song = songs[songKey]
            row = (song["songID"], song["songName"], song["trackNumber"], song["songLength"])
            writer.writerow(row)


# From Jeff's csv2tables.py file
if len(sys.argv) != 2:
    print(f'Usage: {sys.argv[0]} original_csv_file', file=sys.stderr)
    exit()


samConvert(sys.argv[1])

