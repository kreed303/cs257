import { createMenu, getAPIBaseURL } from './webapp.js';

window.addEventListener("load", initialize);

function initialize() {
    createMenu();
    addSongsTable();
}

function addSongsTable() {
    var URL = getAPIBaseURL() + '/1.0/songs'

    fetch(URL, {method: 'get'})

    .then((response) => response.json())

    .then(function(songs) {
        var songsList = document.getElementById('pageData');

        var songsHTML = '<table class="musicDataTable">';
        for (var i=0; i<songs.length; i++) {
            songsHTML += '<tr class="musicDataEntry"><td>' + songs[i].songName + '</td></tr>';
        }

        songsHTML += '</table>';
        songsList.innerHTML = songsHTML;
    })

    .catch(function(error) {
        console.log(error);
    });
}