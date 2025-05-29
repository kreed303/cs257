import { createMenu, getAPIBaseURL } from './webapp.js';

window.addEventListener("load", initialize);

function initialize() {
    
    createMenu();
    addAlbumSongs();


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

function shuffleSongs(){
    addAlbumSongs(true);
}

function orderSongs(){
    addAlbumSongs(false);
}




function addAlbumSongs(shuffle) {
    // const albumID = document.getElementById('albumID').textContent;
    var URL = getAPIBaseURL() + '/1.0/albums/' + albumID + '?shuffle=' + shuffle;

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