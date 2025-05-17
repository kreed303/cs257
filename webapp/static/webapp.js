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
    return window.location.href = 'http://localhost:5555/help';

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