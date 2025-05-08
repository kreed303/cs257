SELECT songs.songid, songs.songname, songs.tracknumber, songs.songlength, songs.songbpm FROM songs
JOIN artistssongs ON artistssongs.songid = songs.songid
JOIN artists ON artists.artistid = artistssongs.artistid
JOIN artistsalbums ON artists.artistid = artistsalbums.artistid
WHERE LOWER(artists.artistname) = LOWER('aBbA')
ORDER BY artists.artistid DESC, artistsalbums.albumid DESC;


SELECT * FROM songs
JOIN songsplaylists ON songsplaylists.songid = songs.songid
JOIN playlists ON playlists.playlistid = songsplaylists.playlistid
WHERE LOWER(playlists.playlistname) = LOWER('testPlaylist');

SELECT COUNT(*) FROM playlists;

INSERT INTO playlists (playlistid, playlistname)
VALUES ('1', 'testPlaylist');

INSERT INTO playlistssongs (playlistid, songid)
VALUES (1, 1);