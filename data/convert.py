import sys
import csv
import os

def main(inputFile):
    # DATABASE = os.path.join(os.getcwd(), '/data/songs.csv')

    songs = {}
    artists = {}
    albums = {}
    albums_songs = []
    artists_albums = []
    artists_songs = []

    with open(inputFile) as f:
        reader = csv.reader(f)
        for songRow in reader:
            songName = songRow[4]
            albumName = songRow[1]
            artistName = songRow[5]
            trackNumber = songRow[8]
            songLength = songRow[3]
            albumYear = songRow[10]

            songKey = f"{songName}+{artistName}"
            artistKey = f"{artistName}"
            albumKey = f"{albumName}+{artistName}"
            
            # Write stuff to create dictionary entries based on keys


    # From Jeff's csv2tables.py file
if len(sys.argv) != 2:
    print(f'Usage: {sys.argv[0]} original_csv_file', file=sys.stderr)
    exit()


main(sys.argv[1])

