from flask import Flask
import pyodbc
from dotenv import load_dotenv
import os
from waitress import serve
from flask import render_template
from flask import request



from controllers import LogRow, LogRunTimes
load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/logs')
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
        #Vurable to sql injection so i wont commit this



if __name__ == "__main__":
    db_user = os.environ["DB_USER"]
    db_pass = os.environ["DB_PASS"]
    db_conn = os.environ["DB_CONN"]

    conn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};" + f"Server={db_conn};Database=app;Uid={db_user};Pwd={db_pass};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")


    serve(app,host='0.0.0.0',port=80)
