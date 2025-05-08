# Music Library API
# Katelyn Reed & Sam Reiter


import os
import argparse
import flask # type: ignore
import json
import csv
import sys
import psycopg2
import config

app = flask.Flask(__name__)

@app.route('api/1.0')
def home():
    conn = getConnection()
    curs = conn.cursor()

    curs.execute("SELECT tablename FROM pg_tables;" \
                "WHERE tableowner = 'reedk2'")
    tables = curs.fetchall()
    pages = {"tableName" : i[0] for i in tables}
    
    conn.close()
    curs.close()

    return json.dumps(pages)




def getConnection():
    try:
        return psycopg2.connect(database=config.database,
                                user=config.user,
                                password=config.password)
    except Exception as e:
        print(e, file=sys.stderr)
        exit()
    


# From Jeff's API code
if __name__ == '__main__':
    parser = argparse.ArgumentParser('A sample Flask application/API')
    parser.add_argument('host', help='the host on which this application is running')
    parser.add_argument('port', type=int, help='the port on which this application is listening')
    arguments = parser.parse_args()
    app.run(host=arguments.host, port=arguments.port, debug=True)