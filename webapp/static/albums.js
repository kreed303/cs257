import { createMenu, getAPIBaseURL } from './webapp.js';

window.addEventListener("load", initialize);

function initialize() {
    createMenu();
    addAlbumsTable();
}

function addAlbumsTable() {
    var URL = getAPIBaseURL() + '/1.0/albums'

    fetch(URL, {method: 'get'})

    .then((response) => response.json())

    .then(function(albums) {
        var albumsList = document.getElementById('pageData');

        // Create tables with apprpriate data and links
        var albumsHTML = '<table class="musicDataTable"> <tr><th class="musicDataHeader">Album</th><th class="musicDataHeader">Artist</th></tr>';
        for (var i=0; i<albums.length; i++) {
            var album = albums[i];
            console.log(album);
            albumsHTML += '<tr><td class="musicDataEntry"> <a class="musicLink" href="/albums/' + album.albumID + '">'
            + album.albumName + '</a></td>';
            albumsHTML += '<td class="musicDataEntry"> <a class="musicLink" href="/artists/' + album.artistID + '">'
            + album.artistName + '</a></td></tr>';
        }

        albumsHTML += '</table>';

        albumsList.innerHTML = albumsHTML;
    })

    .catch(function(error) {
        console.log(error);
    });
}