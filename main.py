from flask import Flask
import pyodbc
from dotenv import load_dotenv
import os
from waitress import serve

load_dotenv()



if __name__ == "__main__":
    db_user = os.environ["DB_USER"]
    db_pass = os.environ["DB_PASS"]
    db_conn = os.environ["DB_CONN"]

    conn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};" + f"Server={db_conn};Database=app;Uid={db_user};Pwd={db_pass};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")
   
    app = Flask(__name__)

    @app.route('/')
    def index():
        return "Hello world"

    serve(app,host='0.0.0.0',port=80)
