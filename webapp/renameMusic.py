import os
from helperFunctions import _getSongID
from psycopg2 import sql
from shutil import copy
import pdb
import time

import pygame

def loadSong():
    for dirpath, dirnames, filenames in os.walk('musicFiles'):
        for song in filenames:
            if song.endswith(".mp3"):
                songName = song[3:-4]
                songId = _getSongID(songName, like=True)
                copy(f"{dirpath}/{song}", f"musicFiles/{songId}.mp3")

def pygameExperiment(songID):
    pygame.mixer.init()
    pygame.mixer.music.load(f"musicFiles/{songID}.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)

    # init()
    # print("here")
    # play() 

pygameExperiment(2)
