import argparse
import flask
import api

from helperFunctions import _getAlbumName, _getArtistName

app = flask.Flask(__name__, static_folder='static', template_folder='templates')
app.register_blueprint(api.api, url_prefix='/api')

@app.route('/')
def home():
    '''
    This is the home page!!!

    input: none
    output: a simple message saying hi!
    '''

    return flask.render_template('home.html')

@app.route('/artists')
def artists():
    '''
    Webage for displaying artists
    input: none
    output: webpage for list of artists
    '''

    return flask.render_template('artists.html')

@app.route('/artists/<artistID>')
def artist(artistID) :
    '''
    Webpage for displaying a single artist's music
    input: artistID
    output: a list of albums by the artist
    '''
    artistName = _getArtistName(artistID)
    return flask.render_template('artist.html', artistID = artistID, artistName = artistName)

@app.route('/artists/<artistID>/<albumID>')
def albumThruArtist(artistID, albumID): 
    '''
    Webpage for displaying an album by a single artist's
    input: artistID, albumID
    output: a list of songs on the album by the artist
    '''

    artistName = _getArtistName(artistID)
    albumName = _getAlbumName(albumID)
    return flask.render_template('album.html', albumID = albumID, albumName = albumName)


@app.route('/albums')
def albums():
    '''
    Webage for displaying albums
    input: none
    output: webpage for list of albums by a particular artist
    '''

    return flask.render_template('albums.html')

@app.route('/album/<albumID>')
def album(albumID):
    '''
    Webage for displaying a specific album
    input: album information dictionary
    output: webpage for list of albums by a particular artist
    '''
    albumName = _getAlbumName(albumID)
    return flask.render_template('album.html', albumID = albumID, albumName = albumName)


@app.route('/songs')
def songs():
    '''
    Webage for displaying songs
    input: none
    output: webpage for list of songs
    '''

    return flask.render_template('songs.html')

@app.route('/help')
def help():
    return flask.render_template('help.html')


if __name__ == '__main__':
    parser = argparse.ArgumentParser('A sample Flask application/API')
    parser.add_argument('host', help='the host on which this application is running')
    parser.add_argument('port', type=int, help='the port on which this application is listening')
    arguments = parser.parse_args()
    app.run(host=arguments.host, port=arguments.port, debug=True)
