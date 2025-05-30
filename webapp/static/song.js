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
    var URL = getAPIBaseURL() + '/1.0/songs/' + songID;
}

function addSongData() {
    var URL = getAPIBaseURL() + '/1.0/play/' + songID;

    fetch(URL, {method: 'get'})
}