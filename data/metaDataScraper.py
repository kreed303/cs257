# Conda activate MusicApp

import os
from mutagen.mp3 import MP3  
from mutagen.easyid3 import EasyID3  
import pandas as pd
import pdb

DIRECTORY = os.getcwd()
print(DIRECTORY)
album_csv = pd.DataFrame(columns=["album", "composer", "length", "title", "artist", "album artist", "organization", "tracknumber"," genre", "date"])

for path, _, files in os.walk(DIRECTORY):
    for name in files:
        filename = os.path.join(path, name)
        try:
            if filename.endswith(".mp3"):
                mp3file = MP3(filename, ID3 = EasyID3)
                print(mp3file.values())
                # pdb.set_trace()
                mp3data = [x[0].strip() for x in mp3file.values()]
                #print(mp3data)
                album_csv = pd.concat([pd.DataFrame([mp3data], columns = album_csv.columns), album_csv], ignore_index = True)
        except:
            pass
            # print(filename)
# print(album_csv)
album_csv.to_csv("songs.csv")

    # print(os.stat(filename))
    # try:
    #     with open(filename, "r") as f:
    #         data = f.read()
    #         print(data)
    # except UnicodeDecodeError:
    #     print("oops")