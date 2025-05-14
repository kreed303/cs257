window.addEventListener("load", initialize);

function initialize() {
    var element = document.getElementById('helpButton');
    if (element) {
        element.onclick = clickHelpButton;
    }
}

function clickHelpButton() {
    var url = '/help';

    fethch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(help) {
        var helpText = help;

        var element = document.getElementById('helpText');

        if (helpText) {
            element.innerHTML = helpText;
        }
    })

    .catch(function(error) {
        console.log(error);
    });
}