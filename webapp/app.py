import argparse
import flask
import api

app = flask.Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def home():
    '''
    This is the home page!!!

    input: none
    output: a simple message saying hi!
    
    '''

    return flask.render_template('home.html')

@app.route('/artists')
def temp():
    '''
    This is the home page!!!

    input: none
    output: a simple message saying hi!
    
    '''

    return flask.render_template('artists.html')

@app.route('/help')
def help():
    return flask.render_template('help.html')


if __name__ == '__main__':
    parser = argparse.ArgumentParser('A sample Flask application/API')
    parser.add_argument('host', help='the host on which this application is running')
    parser.add_argument('port', type=int, help='the port on which this application is listening')
    arguments = parser.parse_args()
    app.run(host=arguments.host, port=arguments.port, debug=True)
