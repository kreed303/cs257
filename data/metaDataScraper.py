# Conda activate MusicApp

import os
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3  
from mutagen.id3 import ID3
import pandas as pd
import pdb

def writeTagsToCsv():
    album_csv = pd.DataFrame(columns=["album", "composer", "length", "title", "artist", "albumartist", "organization", "tracknumber","genre", "date"])
    for path, _, files in os.walk(DIRECTORY):
        for name in files:
            filename = os.path.join(path, name)
            if filename.endswith(".mp3"):
                mp3data = []
                mp3file = MP3(filename, ID3 = EasyID3)
                for item in album_csv.columns:
                    if item in mp3file.keys():
                        mp3data.append(mp3file[item][0].strip())
                    elif item == "title":
                        mp3data.append(name.split(".")[0].lstrip("012345679 "))
                    else:
                        mp3data.append("-")
                album_csv = pd.concat([pd.DataFrame([mp3data], columns = album_csv.columns), album_csv], ignore_index = True)
            album_csv.to_csv("songs.csv")

def CreateEmptyTags():
    for path, _, files in os.walk(DIRECTORY):
        for name in files:
            filename = os.path.join(path, name)       
            if filename.endswith(".mp3"):
                try:
                    tags = ID3(filename)
                except:
                    tags = ID3()
                tags.save(filename)

if __name__ == "__main__":
    DIRECTORY = os.getcwd()
    print(DIRECTORY)
    CreateEmptyTags()
    writeTagsToCsv()