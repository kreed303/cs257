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
        

        var key = "songname"
        songHTML += '<h2>' + song[key] + '</h2>';

        songHTML += '<table class="musicDataTable">';


        songHTML += '<tr><td class="musicDataEntry"> Track Number:    ' + song.tracknumber + '</td></tr>';

        songHTML += '<tr><td class="musicDataEntry"><a class="musicLink" href="/artists/' + song.artistid + '">' + 'Artist Name:    ' + song.artistname + '</a></td></tr>'

        songHTML += '<tr><td class="musicDataEntry"><a class="musicLink" href="/albums/' + song.albumid + '">' + 'Album Name:    ' + song.albumname + '</a></td></tr>'

        songHTML += '<tr><td class="musicDataEntry"> Song Length:    ' + Math.floor(song.songlength / 60000) + ":" +  Math.floor((song.songlength / 10000) % 60) + '</td></tr>';

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