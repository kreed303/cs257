import { createMenu, getAPIBaseURL } from './webapp.js';


window.addEventListener("load", initialize);

function initialize() {
    createMenu();
    addArtistsTable();
    addAlbumsTable();
    addSongsTable();
}


function addArtistsTable () {
    var URL = getAPIBaseURL() + '/1.0/artists'
    fetch(URL, {method: 'get'})

    .then((response) => response.json())

    .then(function(artists) {
        var artistsHTML = '<table class="musicDataTable">';

        for (var i=0; i<3; i++) {
            var artist = artists[i]
            artistsHTML += '<tr><td class="musicDataEntry"> <a class="musicLink" href="/artists/' + artist.artistID + '">' + artist.artistName + '</a></td></tr>';
        }
        artistsHTML += "</table>";
        var element = document.getElementById('artists');
        element.innerHTML += artistsHTML;
    })

    .catch(function(error) {
        console.log(error);
    });
}

function addSongsTable() {
    var URL = getAPIBaseURL() + '/1.0/songs'

    fetch(URL, {method: 'get'})

    .then((response) => response.json())

    .then(function(songs) {
        var songsList = document.getElementById('songs');

        var songsHTML = '<table class="musicDataTable">';
        for (var i=0; i<5; i++) {
            var song = songs[i]
            songsHTML += '<tr><td class="musicDataEntry"> <a class="musicLink" href="/songs/' + song.songID + '">' + song.songName + '</a></td></tr>';
        }

        songsHTML += '</table>';
        songsList.innerHTML += songsHTML;
    })

    .catch(function(error) {
        console.log(error);
    });
}


function addAlbumsTable() {
    var URL = getAPIBaseURL() + '/1.0/albums'

    fetch(URL, {method: 'get'})

    .then((response) => response.json())

    .then(function(albums) {
        var albumsList = document.getElementById('albums');

        var albumsHTML = '<table class="musicDataTable">';
        for (var i=0; i<5; i++) {
            var album = albums[i];
            albumsHTML += '<tr><td class="musicDataEntry"> <a class="musicLink" href="/albums/' + album.albumID + '">'
            + album.albumName + '</a></td></tr>';
        }

        albumsHTML += '</table>';

        albumsList.innerHTML += albumsHTML;
    })

    .catch(function(error) {
        console.log(error);
    });
}