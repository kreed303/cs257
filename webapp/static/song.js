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

        // Fill tables with appropriate song data and links
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

        songHTML += '<table>';
        songList.innerHTML = songHTML;
    })

}