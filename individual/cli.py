# Sort Songs by Genre
# Written by Katelyn Reed, 4/17/25

# NAME: cli.py - Command Line Interface Exercise
# SYNOPSIS: python3 cli.py genre
# DESCRIPTION: Shows a list of songs from the given library that are of the specified genre

import argparse
import os
import csv


def main():
    args = getParsedArgs()
    directory = os.getcwd()
    CSV = os.path.join(directory, '../data/songs.csv')

    print(CSV)
    with open(CSV) as songs:
        songList = csv.reader(songs)

        if args.genre not in ("Rock", "Dance", "Pop", "World"):
            print("There are no songs in the library of that genre.")
            print("The options are Dance, Pop, Rock, and World music.")
        else:    
            for song in songList:
                if (song[9] == (args.genre)):
                    print(f"Song: {song[4].strip()}, Artist: {song[5].strip()}, Album: {song[1].strip()}")    


def getParsedArgs():
    parser = argparse.ArgumentParser(prog='Find Songs By Genre', 
                                     description='Search a library for a list of songs by genre')
    parser.add_argument('genre', help='Music genre to filter songs by')
    parsedArgs = parser.parse_args()
    return parsedArgs


if __name__ == '__main__':
    main()