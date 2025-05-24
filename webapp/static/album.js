import { createMenu, getAPIBaseURL } from './webapp.js';

window.addEventListener("load", initialize);

function initialize() {
    createMenu();
    addAlbumSongs();
}


// function addAlbumName() {
//     const albumID = document.getElementById('albumID').textContent;
//     var URL 

// }

function addAlbumSongs() {
    // const albumID = document.getElementById('albumID').textContent;
    var URL = getAPIBaseURL() + '/1.0/albums/' + albumID;

    fetch(URL, {method: 'get'})
    .then((response) => response.json())
    .then(function(songs) {
        var songsList = document.getElementById('pageData');

        var songsHTML = '<table class="musicDataTable">';
        for (var i=0; i<songs.length; i++) {
            var song = songs[i]
            songsHTML += '<tr class="musicDataEntry"><td> <a href="/songs/' + song.songID + '">' + song.songName + '</a></td></tr>';
        }

        songsHTML += '</table>';
        songsList.innerHTML = songsHTML;
    })

    .catch(function(error) {
        console.log(error);
    });
}