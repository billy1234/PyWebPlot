from flask import render_template


def render_table(
        column_names : list[str], 
        table : list[list], 
        current_page : int,
        max_page : int
    ) -> str:
    return render_template(
        'table.html', 
        columns = column_names, 
        table=table,
        table_name='LOGS_RUN_TIMES',
        row_link=True,
        current_page=current_page,
        max_page=max_page
    )