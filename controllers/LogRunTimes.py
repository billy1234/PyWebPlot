from pyodbc import Cursor
from models import LogRunTimeModel as model
from views import LogRunTimeView as view


def display_table(curs : Cursor, page=0, page_size=50):
    cols, table = model.get_table(curs,page,page_size)
    return view.render_table(
        cols, 
        table, 
        page, 
        model.get_max_pages(curs, page_size)
    )
