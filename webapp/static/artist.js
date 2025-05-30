import { createMenu, getAPIBaseURL } from './webapp.js';

window.addEventListener("load", initialize);

function initialize() {
    createMenu();
    addArtistAlbums()
    addArtistSongs()


    var shuffle = false;
    var shuffleButton = document.getElementById('shuffleButton');
    if (shuffleButton) {
        shuffleButton.onclick = shuffleSongs;
    }

    var playButton = document.getElementById('playButton');
    if (playButton) {
        playButton.onclick = orderSongs;
    }
}


function addArtistAlbums() {
    var URL = getAPIBaseURL() + '/1.0/artists/' + artistID;

    fetch(URL, {method: 'get'})

    .then((response) => response.json())

    .then(function(albums) {
        var albumsList = document.getElementById('artistAlbums');

        var albumsHTML = '<table class="musicDataTable">'
        for (var i=0; i<albums.length; i++) {
            albumsHTML += '<tr><td class="musicDataEntry"><a class="musicLink" href="/albums/' + albums[i].albumID + '">' + albums[i].albumName + '</a></td></tr>';
        }

        albumsHTML += '</table>';
        albumsList.innerHTML = albumsHTML;
    })
}

function shuffleSongs(){
    addArtistSongs(true);
}

function orderSongs(){
    addArtistSongs(false);
}


function addArtistSongs(shuffle) {
    var URL = getAPIBaseURL() + '/1.0/artistssongs/' + artistID + '?shuffle=' + shuffle;

    fetch(URL, {method: 'get'})

    .then((response) => response.json())

    .then(function(songs) {
        var songsList = document.getElementById('artistSongs');

        var songsHTML = '<table class="musicDataTable">';
        for (var i=0; i<songs.length; i++) {
            var song = songs[i]
            songsHTML += '<tr class="musicDataEntry">\
            <td> <a href="/songs/' + song.songID + '">' + song.songName + '</a> </td>\
            <td>' + song.albumName + '\
            </tr>';
        }

        songsHTML += '</table>';
        songsList.innerHTML = songsHTML;
    })

    .catch(function(error) {
        console.log(error);
    });

}
