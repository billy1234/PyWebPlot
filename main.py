from flask import Flask, Response, request, render_template
import pyodbc
from dotenv import load_dotenv
import os
from waitress import serve

from plots import *
import webplots as plots

from controllers import LogRow, LogRunTimes
load_dotenv()

app = Flask(__name__)
conn_str = ""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/logs/')
def logs():
    page_num = 0
    page_arg = request.args.get("page")
    if page_arg:
        page_num = int(page_arg)
        if page_num < 0:
            page_num = 0

    with conn.cursor() as c:
        return LogRunTimes.display_table(c, page_num, 50)
    
@app.route('/data/LOGS_RUN_TIMES/<id>')
def log_info(id):
    with conn.cursor() as c:
        return LogRow.display_log(c, id)

@app.route('/plots/<name>.png')
def plot_png(name):
    with get_db_conn(conn_str) as conn:
        #I am using SQL server and muliple cursors on the same connection
        #Throw an error, Creating a new connection for evey graph generation is not idea
        #And some kind of thread pooling should be used
        return Response(plots.getPlot(name, conn), mimetype='image/png')
    

@app.route('/graphs/')
def graphs():
    return render_template('graphs.html')

def get_db_conn(conn_str):
    if len(conn_str) == 0:
        raise "Bad connection string"
    return pyodbc.connect(conn_str)

if __name__ == "__main__":
    db_user = os.environ["DB_USER"]
    db_pass = os.environ["DB_PASS"]
    db_conn = os.environ["DB_CONN"]

    conn_str = "Driver={ODBC Driver 17 for SQL Server};" + f"Server={db_conn};Database=app;Uid={db_user};Pwd={db_pass};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"
    conn = get_db_conn(conn_str)


    serve(app,host='0.0.0.0',port=80)
