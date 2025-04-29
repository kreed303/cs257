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