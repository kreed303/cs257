-- Returns list of all songs on the Cordial album--
SELECT songName
FROM songs
WHERE songID IN (
  SELECT songID
  FROM albumsSongs       
  WHERE albumssongs.albumID = (
    SELECT albumID
    FROM albums
    WHERE albums.albumName = 'Cordial'
  )
);

SELECT songName
FROM songs, albumssongs, albums
WHERE albums.albumName = 'Cordial'
AND albumssongs.albumID = albums.albumID
AND albumssongs.songID = songs.songID;

-- Returns list of all albums by Paul Simon--
SELECT albumName
FROM albums
WHERE albumID IN (
    SELECT albumID
    FROM artistsAlbums
    WHERE artistsAlbums.artistID = (
        SELECT artistID
        FROM artists
        WHERE artists.artistName = 'Paul Simon'
    )
);

-- Returns a list of all songs by La Bottine Souriante--
SELECT songName
FROM songs
WHERE songID IN (
    SELECT songID                                                                                                 
    FROM artistsSongs                                                                                        
    WHERE artistsSongs.artistID = (
        SELECT artistID
        FROM artists
        WHERE artists.artistName = 'La Bottine Souriante'
    )
);

-- Returns a list of songs and their ID that were realeased in 2001
SELECT songID, songName
FROM songs
WHERE songID IN (
  SELECT songID
  FROM albumsSongs
  WHERE albumID IN (
    SELECT albumID
    FROM albums
    WHERE (
      albums.albumYear = '2001'
    )
  )
);

-- adding a new song to song --
INSERT INTO songs (songid, songname, tracknumber, songlength, songbpm) 
values ((SELECT count(*) from songs) + 1, 'tempSong', '1', '123123123', '0' );

-- delete last songs from songs -- 

DELETE FROM songs WHERE songID = (SELECT count(*) from songs);

SELECT * FROM songs WHERE  songName = 'The Winner Takes It All
' OR trackNumber = '5' ;