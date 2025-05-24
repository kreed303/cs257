import { createMenu, getAPIBaseURL } from './webapp.js';

window.addEventListener("load", initialize);

function initialize() {
    createMenu();
    addSongData();
}

function addSongData() {
    var URL = getAPIBaseURL() + '/1.0/songs/' + songID;

    fetch(URL, {method: 'get'})
    .then((response) => response.json())
    .then(function(song) {
        var songList = document.getElementById('pageData');
        var songHTML = '<table class="musicDataTable">';
        song = song[0]
        console.log(song[0])
        for (let i = 0; i < Object.keys(song).length; i++) {
            var key = Object.keys(song)[i];
            var value = song[key];
            songHTML += '<tr class="musicDataEntry"><td>' + key + ":    " + value + '</td></tr>';
            console.log(key, value);
        }
        songHTML += '<table>';
        songList.innerHTML = songHTML;
    })

}