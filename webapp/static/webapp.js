export function getAPIBaseURL() {
    var baseURL = window.location.protocol
                    + '//' + window.location.hostname
                    + ':' + window.location.port
                    + '/api';
                    
    return baseURL;
}




export function createMenu() {
    var menu = document.getElementById('menu');

    if (!menu) {
        console.error('Could not find #menu');
        return;
    }
    var URL = getAPIBaseURL() + '/1.0/menuHTML'
    fetch(URL, {method: 'get'})
    .then((response) => response.text())
    .then(function(response) {
        var element = document.getElementById('menu');
        console.log(response)
        element.innerHTML = response;
        }
    );
}

// not used yet
// maybe will be helpful in the future.
export function clickNewPage(link) {
    return window.location.href = link;

}