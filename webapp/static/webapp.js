window.addEventListener("load", initialize);

function initialize() {
    var element = document.getElementById('helpButton');
    if (element) {
        element.onclick = clickHelpButton;
    }
}

function getAPIBaseURL() {
    var baseURL = window.location.protocol
                    + '//' + window.location.hostname
                    + ':' + window.location.port;
    return baseURL;
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