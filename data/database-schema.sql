--Music App Database Design--
--Katelyn Reed & Sam Reiter--

--Basic tables based on current CSV data--
CREATE TABLE songs (
    songID integer NOT NULL,
    songName TEXT,
    trackNumber integer,
    songLength integer
    --songBPM integer?--
);

CREATE TABLE artists (
    artistID integer NOT NULL,
    artistName TEXT
);

CREATE TABLE albums (
    albumID integer NOT NULL,
    albumName TEXT,
    albumYear integer
);

CREATE TABLE albums_songs (
    albumID integer NOT NULL,
    songID integer NOT NULL
);

CREATE TABLE artists_albums (
    artistID integer NOT NULL,
    albumID integer NOT NULL
);

CREATE TABLE artists_songs (
    artistID integer NOT NULL,
    songID integer NOT NULL
);


--Tables we'd like to create to be modified by user inputted data--
CREATE TABLE playlists (
    playlistID integer NOT NULL,
    playlistName TEXT,
);

CREATE TABLE tags (
    tagID integer NOT NULL,
    tagName TEXT,
);

CREATE TABLE playlists_songs (
    playlistID integer NOT NULL,
    songID integer NOT NULL
);

CREATE TABLE tags_songs (
    tagID integer NOT NULL,
    songID integer NOT NULL
);

CREATE TABLE tags_artists (
    tagID integer NOT NULL,
    artistID integer NOT NULL
);

CREATE TABLE tags_albums (
    tagID integer NOT NULL,
    albumID integer NOT NULL
);

CREATE TABLE tags_playlists (
    tagID integer NOT NULL,
    playlistID integer NOT NULL
);