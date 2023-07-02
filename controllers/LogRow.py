from pyodbc import Cursor
from models import LogRowModel as model
from views import LogRowView as view


def display_log(curs : Cursor, log_id : str) -> str:                                              
    cols,row = model.get_log(curs,log_id)
    return view.render_log(cols,row,log_id)