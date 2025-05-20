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

    .then(function(response) {
        var changeString = '<table class="musicDataTable">';
        for (var i = 0; i < response.length; i++)
            changeString += '<tr><td class="musicDataEntry">' + response[i]['artistName']  + '</td></tr>';
        changeString += "</table>";
        var element = document.getElementById('pageData');
        element.innerHTML = changeString;
    })

    .catch(function(error) {
        console.log(error);
    });

}

