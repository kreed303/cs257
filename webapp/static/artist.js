import { createMenu, getAPIBaseURL } from './webapp.js';

window.addEventListener("load", initialize);

function initialize() {
    createMenu();
    addArtistAlbums()
}


function addArtistAlbums() {
    var URL = getAPIBaseURL() + '/1.0/artists/' + artistID;

    fetch(URL, {method: 'get'})

    .then((response) => response.json())

    .then(function(albums) {
        var albumsList = document.getElementById('pageData');
        console.log(albums);

        var albumsHTML = '<table class="musicDataTable">'
        for (var i=0; i<albums.length; i++) {
            albumsHTML += '<tr><td class="musicDataEntry"><a href="/artists/' + artistID + '/' + albums[i].albumID + '">' + albums[i].albumName + '</a></td></tr>';
        }

        albumsHTML += '</table>';
        albumsList.innerHTML = albumsHTML;
    })
}
