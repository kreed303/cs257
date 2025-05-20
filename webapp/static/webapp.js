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

export function getAPIBaseURL() {
    var baseURL = window.location.protocol
                    + '//' + window.location.hostname
                    + ':' + window.location.port
                    + '/api';
                    
    return baseURL;
}

function doSomething(){

    var URL = getAPIBaseURL() + '/1.0/songs'
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



export function clickNewPage(link) {
    return window.location.href = 'http://localhost:5555/help';

}

export function createMenu() {
    var menu = document.getElementById('menu');

    if (!menu) {
        console.error('Could not find #menu');
        return;
    }
    var URL = getAPIBaseURL() + '/1.0/menuHTML'
    fetch(URL, {method: 'get'})
    .then(function(response) {
        var element = document.getElementById('menu');
        console.log(response)
        element.innerHTML = response;
        }
    );
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