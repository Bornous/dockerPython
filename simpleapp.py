from flask import Flask
import sys
import optparse
import pyodbc
from datetime import date
import time
app = Flask(__name__)

start = int(round(time.time()))

@app.route("/")
def hello_world():
    try:
        conn = pyodbc.connect(
            r'DRIVER={ODBC Driver 17 for SQL Server};'
            r'SERVER=10.0.2.2,1433;'
            r'DATABASE=dbo_testing;'
            #r'Trusted_Connection=yes;'
            r'UID=pythonapp;'
            r'Pwd=dockerPython17;'
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM dbo.testing")
        my_str =""
        for row in cursor.fetchall():
            my_str= my_str+"<div>"+str(row)+"</div>"
        return "Connected correctly! At: "+str(date.today())+" "+my_str
    except pyodbc.Error:
        return "Connection with sql server failed!!! At: "+str(date.today())+" "

@app.route("/doc_choose")
def doc_choose():
    return "<h1>Wybierz raport:</h1><div><a href=\"/\">Zmiana w pensum</a></div>"

if __name__ == '__main__':
    parser = optparse.OptionParser(usage="python3 simpleapp.py -p ")
    parser.add_option('-p', '--port', action='store', dest='port', help='The port to listen on.')
    (args, _) = parser.parse_args()
    if args.port == None:
        print("Missing required argument: -p/--port")
        sys.exit(1)
    app.run(host='0.0.0.0', port=int(args.port), debug=False)
