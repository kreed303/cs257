import sys
import csv
import os
import pandas as pd
import pdb

def artistsCSV():
    metaData = pd.read_csv("metaData.csv")
    artists = list(metaData["artist"].unique())
    artistID = [i for i in range(len(artists))]
    newDF = pd.DataFrame([artistID, artists], index = ["artistID", "artist"]).T
    newDF.to_csv("artists.csv", index=False)
    
    # pdb.set_trace()

def albumsCSV():
    metaData = pd.read_csv("metaData.csv")
    # pdb.set_trace()
    albums = metaData[["album", "date"]].drop_duplicates()
    albums["albumID"] = [i for i in range(len(albums))]
    albums = albums.iloc[:, [2, 0, 1]]
    albums.to_csv("albums.csv", index = False)


def artistAlbumCSV():
    metaData = pd.read_csv("metaData.csv")
    artists = pd.read_csv("artists.csv")
    albums = pd.read_csv("albums.csv")
    artistAlbum = pd.DataFrame(index = ["artistID", "albumID"])
    for _, row in metaData[["artist","album"]].drop_duplicates().iterrows():
        pdb.set_trace()
        artists[artists["artist"] == row["artist"]]["artistID"]
    pdb.set_trace()

def songCSV(inputFile):
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



    print(f'Usage: {sys.argv[0]} original_csv_file', file=sys.stderr)
    exit()

# artistsCSV()
artistAlbumCSV()

