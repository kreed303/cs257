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

        var albumsHTML = '<table class="musicDataTable">';
        for (var i=0; i<albums.length; i++) {
            var album = albums[i];
            albumsHTML += '<tr class="musicDataEntry"><td> <a href="/albums/' + album.albumID + '">'
            + album.albumName + '</a></td></tr>';
        }

        albumsHTML += '</table>';

        albumsList.innerHTML = albumsHTML;
    })

    .catch(function(error) {
        console.log(error);
    });
}