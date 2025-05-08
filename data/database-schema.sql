--Music App Database Design--
--Katelyn Reed & Sam Reiter--

--Basic tables based on current CSV data--
CREATE TABLE songs (
    songID integer NOT NULL,
    songName TEXT,
    trackNumber integer,
    songLength integer,
    songBPM integer
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

CREATE TABLE albumsSongs (
    albumID integer NOT NULL,
    songID integer NOT NULL
);

CREATE TABLE artistsAlbums (
    artistID integer NOT NULL,
    albumID integer NOT NULL
);

CREATE TABLE artistsSongs (
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

CREATE TABLE playlistsSongs (
    playlistID integer NOT NULL,
    songID integer NOT NULL
);

CREATE TABLE tagsSongs (
    tagID integer NOT NULL,
    songID integer NOT NULL
);

CREATE TABLE tagsArtists (
    tagID integer NOT NULL,
    artistID integer NOT NULL
);

CREATE TABLE tagsAlbums (
    tagID integer NOT NULL,
    albumID integer NOT NULL
);

CREATE TABLE tagsPlaylists (
    tagID integer NOT NULL,
    playlistID integer NOT NULL
);

