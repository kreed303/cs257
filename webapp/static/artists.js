import { createMenu, getAPIBaseURL } from './webapp.js';


window.addEventListener("load", initialize);

function initialize() {
    createMenu();
    addArtistsTable();
}

function addArtistsTable () {
    var URL = getAPIBaseURL() + '/1.0/artists'
    fetch(URL, {method: 'get'})
    
    .then((response) => response.json())

    .then(function(artists) {
        var changeString = '<table class="musicDataTable">';
        for (var i = 0; i < artists.length; i++)
            changeString += '<tr><td class="musicDataEntry"><a class="musicLink" href="artists/' + artists[i].artistID + '">' + artists[i]['artistName']  + '</a></td></tr>';
        changeString += "</table>";
        var element = document.getElementById('pageData');
        element.innerHTML = changeString;
    })

    .catch(function(error) {
        console.log(error);
    });

}

