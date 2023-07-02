from flask import render_template

def render_log(
        column_names : list[str],
        row : list,
        log_name : str
    ) -> str:
        return render_template('row.html',items=zip(column_names, row),name=f"Log: {log_name}") 
    