import { createMenu, getAPIBaseURL } from './webapp.js';

window.addEventListener("load", initialize);

function initialize() {
    createMenu();
    addSongData();

    // var playButton = document.getElementById('playButton');
    // if (playButton) {
    //     playButton.onclick = playSong;
    // }
}

function playSong(){
    var URL = getAPIBaseURL() + '/1.0/play/' + songID;
}

function addSongData() {
    var URL = getAPIBaseURL() + '/1.0/songs/' + songID;
    fetch(URL, {method: 'get'})
        .then((response) => response.json())
        .then(function(songs) {
            var songsList = document.getElementById('pageData');

            var songsHTML = '<table class="musicDataTable">';
            for (var i=0; i<songs.length; i++) {
                var song = songs[i]
                songsHTML += '<tr><td class="musicDataEntry"> <a class="musicLink" href="/songs/' + song.songid + '">' + song.songname + '</a></td></tr>';
            }

            songsHTML += '</table>';
            songsList.innerHTML = songsHTML;
        })

        .catch(function(error) {
            console.log(error);
        });
}