import { createMenu, getAPIBaseURL } from './webapp.js';

window.addEventListener("load", initialize);

function initialize() {
    var shuffle = false;
    createMenu();
    addSongsTable(shuffle);
    
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

        // Fill tables with appropriate song data and links
        var songsHTML = '<table class="musicDataTable"> <tr><th class="musicDataHeader">Song Title</th><th class="musicDataHeader">Artist</th><th class="musicDataHeader">Album</th>';
        for (var i=0; i<songs.length; i++) { 
            var song = songs[i]
            songsHTML += '<tr><td class="musicDataEntry"><a class="musicLink" href="/songs/' + song.songID + '">' + song.songName + '</a></td> <td class="musicDataEntry"> <a class="musicLink" href="/artists/' + song.artistID + '">' + song.artistName + '</a></td> <td class="musicDataEntry"> <a class="musicLink" href="/albums/' + song.albumID + '">' + song.albumName + '</a></td></tr>';
        }

        songsHTML += '</table>';
        songsList.innerHTML = songsHTML;    
    })

    .catch(function(error) {
        console.log(error);
    });
}