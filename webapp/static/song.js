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

// function playSong(){
//     var URL = getAPIBaseURL() + '/1.0/play/' + songID;
// }

function addSongData() {
    var URL = getAPIBaseURL() + '/1.0/songs/' + songID;
    fetch(URL, {method: 'get'})
    .then((response) => response.json())
    .then(function(song) {
        song = song[0]
        var songList = document.getElementById('pageData');
        console.log(song)
        var songHTML = '';

        songHTML += '<table class="musicDataTable">';

        var key = "artistname"
        songHTML += '<tr><td class="musicDataEntry nonClickableMusicDataEntry"> Artist Name:    ' + song[key] + '</td></tr>';

        var key = "albumname"
        songHTML += '<tr><td class="musicDataEntry nonClickableMusicDataEntry"> Album Name:    ' + song[key] + '</td></tr>';

        var key = "tracknumber"
        songHTML += '<tr><td class="musicDataEntry nonClickableMusicDataEntry"> Track Number:    ' + song[key] + '</td></tr>';

        var key = "songlength"
        songHTML += '<tr><td class="musicDataEntry nonClickableMusicDataEntry"> Song Length:    ' + Math.floor(song[key] / 60000) + ":" +  Math.floor((song[key] / 10000) % 60) + '</td></tr>';

        // for (let i = 0; i < Object.keys(song).length; i++) {
        //     var key = Object.keys(song)[i];
        //     var value = song[key];
        //     songHTML += '<tr><td class="musicDataEntry">' + key + ":    " + value + '</td></tr>';
        //     console.log(key, value);
        // }
        songHTML += '<table>';
        songList.innerHTML = songHTML;
    })

}