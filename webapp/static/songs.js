import { createMenu, getAPIBaseURL } from './webapp.js';

window.addEventListener("load", initialize);

function initialize() {
    
    createMenu();
    addSongsTable(shuffle);

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
    addSongsTable(true);
}

function orderSongs(){
    addSongsTable(false);
}
function addSongsTable(shuffle) {
    
    var URL = getAPIBaseURL() + '/1.0/songs?shuffle=' + shuffle

    fetch(URL, {method: 'get'})

    .then((response) => response.json())

    .then(function(songs) {
        var songsList = document.getElementById('pageData');
        console.log(songs)

        var songsHTML = '<table class="musicDataTable">';
        for (var i=0; i<songs.length; i++) {
            var song = songs[i]
            songsHTML += '<tr class="musicDataEntry"><td> <a href="/songs/' + song.songID + '">' + song.songName + '</a></td><td>' + song.artistName+ '</td><td>' + song.albumName+ '</td></tr>';
        }

        songsHTML += '</table>';
        songsList.innerHTML = songsHTML;
    })

    .catch(function(error) {
        console.log(error);
    });
}