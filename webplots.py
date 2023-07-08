import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas


plot_map = {}
    
def register(file_name):
    if file_name in plot_map:
        raise f"Error: {file_name} already registered"
    def _register(plot_fn):
        plot_map[file_name] = plot_fn   

    return _register

def getPlot(name : str, conn):  
    with conn.cursor() as c:
        fig = plot_map[name](c)

    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return output.getvalue()