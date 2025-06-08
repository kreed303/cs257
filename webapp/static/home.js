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
    var URL = getAPIBaseURL() + '/1.0/songs?shuffle=true'

    fetch(URL, {method: 'get'})

    .then((response) => response.json())

    .then(function(songs) {
        var songsList = document.getElementById('songs');

        var songsHTML = '<table class="musicDataTable"> <tr><th class="musicDataHeader">Song Title</th><th class="musicDataHeader">Artist</th><th class="musicDataHeader">Album</th>';
        for (var i=0; i<5; i++) {
            var song = songs[i]

            songsHTML += '<tr> <td class="musicDataEntry"> <a class="musicLink" href="/songs/' + song.songID + '">' + song.songName + '</a></td> <td class="musicDataEntry"> <a class="musicLink" href="/artists/' + song.artistID + '">' + song.artistName + '</a></td> <td class="musicDataEntry"> <a class="musicLink" href="/albums/' + song.albumID + '">' + song.albumName + '</a></td></tr>';
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

        var albumsHTML = '<table class="musicDataTable"> <tr><th class="musicDataHeader">Album</th><th class="musicDataHeader">Arist</th>';
        for (var i=0; i<5; i++) {
            var album = albums[i];
            albumsHTML += '<tr><td class="musicDataEntry"> <a class="musicLink" href="/albums/' + album.albumID + '">'
            + album.albumName + '</a></td> <td class="musicDataEntry"> <a class="musicLink" href="/artists/' + album.artistID + '">'
            + album.artistName + '</a></td></tr>';
        }

        albumsHTML += '</table>';

        albumsList.innerHTML += albumsHTML;
    })

    .catch(function(error) {
        console.log(error);
    });
}