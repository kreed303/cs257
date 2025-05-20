window.addEventListener("load", initialize);

function initialize() {
    createMenu();
    var element = document.getElementById('helpButton');
    if (element) {
        element.onclick = clickHelpButton;
    }

    var element = document.getElementById('artistsPage');
    if (element){
        element.onclick = clickNewPage;
    }

    var element = document.getElementById('something');
    if (element){
         element.onclick = doSomething;
    }
}


function doSomething(){
    var change = document.getElementById("changeSomething");
    var URL = 'http://localhost:5555/api/1.0/songs';
    fetch(URL, {method: 'get'})

    .then((response) => response.json())

    .then(function(change) {
        var change = change;
        var element = document.getElementById('changeSomething');
        element.innerHTML = change;
    })

    .catch(function(error) {
        console.log(error);
    });
}

function getAPIBaseURL() {
    var baseURL = window.location.protocol
                    + '//' + window.location.hostname
                    + ':' + window.location.port;
    return baseURL;
}

function clickNewPage() {
    return window.location.href = 'http://localhost:5555/help';

}

function createMenu() {
    var menu = document.getElementById('menu');

    if (!menu) {
        console.error('Could not find #menu');
        return;
    }
    menu.innerHTML =
    `Menu
    <div class="menuItems" id="homeNavButton">
        <a href="">Home</a></div>
    <div class="menuItems" id="playlistsNavButton">
        <a href="">Playlists</a></div>
    <div class="menuItems" id="artistsNavButton">
        <a href="">Artists</a></div>
    <div class="menuItems" id="albumsNavButton">
        <a href="">Albums</a></div>
    <div class="menuItems" id="songsNavButton">
        <a href="">Songs</a></div>
    <div class="menuItems" id="tagsNavButton">
        <a href="">Tags</a></div>
    <div class="menuItems" id="filterNavButton">
        <a href="">Filter</a></div>`;
}

function clickHelpButton() {
    var url = 'http://localhost:5555/help';

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(help) {
        var helpText = help;
        var element = document.getElementById('helpText');
        element.innerHTML = helpText;
    })

    .catch(function(error) {
        console.log(error);
    });
}