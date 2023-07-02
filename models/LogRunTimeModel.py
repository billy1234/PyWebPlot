from pyodbc import Cursor

def get_table(curs : Cursor, page : int = 0, page_size : int=50):
    curs.execute(f"""
SELECT
* 
FROM LOGS.RUN_TIMES
ORDER BY JOB_START
OFFSET (?) ROWS
FETCH NEXT (?) ROWS ONLY
""", 
page * page_size,
page_size)
    res = curs.fetchall()
    return [e[0] for e in curs.description], res


def get_max_pages(curs : Cursor, page_size : int) -> int:
    curs.execute("SELECT COUNT(1) FROM LOGS.RUN_TIMES")

    n = curs.fetchval()

    return n // page_size