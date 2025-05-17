window.addEventListener("load", initialize);

function initialize() {
    var element = document.getElementById('helpButton');
    if (element) {
        element.onclick = clickHelpButton;
    }

    var element = document.getElementById('artistsPage');
    if (element){
        element.onclick = clickNewPage;
    }
}

function getAPIBaseURL() {
    var baseURL = window.location.protocol
                    + '//' + window.location.hostname
                    + ':' + window.location.port;
    return baseURL;
}

function clickNewPage() {
    return window.location.href = 'http://localhos