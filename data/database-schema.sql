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

