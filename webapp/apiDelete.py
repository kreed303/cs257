"""
Sam believes these are a bunch of functions that we do not need because they are redudant or not useful anymore. Saving them here for now just in case we need them in the future. 
"""

#
# API END POINTS 
#
@api.route('/1.0/artists/<artistName>/<albumName>')
def getSongsFromAlbumThroughArist(artistName, albumName, shuffle=None):
    '''
    This allows the user to get a list of all available songs in a specific album by an artist
    INPUT: the name of the artist and the album
    RETURN: all names of songs and their associated information based on the provided data
    '''
    return getSongsFromAlbum(albumName, shuffle = shuffle)


@api.route('1.0/displayArtists')
def getArtistsHTML():
    return flask.render_template('artists.html')

@api.route('1.0/displayHome')
def getHomeHTML():
    return flask.render_template('home.html')

@api.route('1.0/displaySongs')
def getSongsHTML():
    return flask.render_template('songs.html')

@api.route('1.0/displayAlbums')
def getAlbumsHTML():
    return flask.render_template('.html')
