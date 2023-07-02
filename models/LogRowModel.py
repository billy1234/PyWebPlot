from pyodbc import Cursor
from models import LogRunTimeModel as model
from views import LogRunTimeView as view


def get_log(curs : Cursor, log_id : str) -> tuple[list[str],list]:                                              
    curs.execute('SELECT * FROM LOGS.RUN_TIMES WHERE  ID = (?)', log_id)

    return [e[0] for e in curs.description], curs.fetchone()
