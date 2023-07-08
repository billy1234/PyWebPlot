import webplots as plots
import seaborn as sns
import pandas as pd
from matplotlib.pyplot import figure
import webplots as plots


@plots.register('LogRunTimes')
def render_LogRunTimes(c):
    fig = figure(figsize=(4.5, 6))
    ax = fig.subplots()
    #Note: It is important each plot function generates its own figure/axis
    #Otherwise graphs will share the same plot and draw ontop of eachother
    
    c.execute("""
SELECT
	ID,
	DATEDIFF(millisecond,JOB_START, JOB_END) TIME_MS
FROM LOGS.RUN_TIMES
""")
    data = pd.DataFrame.from_records(c.fetchall(),columns =[e[0] for e in c.description])
    return sns.histplot(data=data,x='TIME_MS',ax=ax).get_figure()

@plots.register('LogRunTimesPerItem')
def render_LogRunTimesPerItem(c):
    fig = figure(figsize=(4.5, 6))
    ax = fig.subplots()
    #Note: It is important each plot function generates its own figure/axis
    #Otherwise graphs will share the same plot and draw ontop of eachother
    
    c.execute("""
SELECT
	ID,
	DATEDIFF(millisecond,JOB_START, JOB_END)  / CAST(WORK_ITEMS as float) TIME_PER_ITEM
FROM LOGS.RUN_TIMES
""")
    data = pd.DataFrame.from_records(c.fetchall(),columns =[e[0] for e in c.description])
    return sns.histplot(data=data,x='TIME_PER_ITEM',ax=ax).get_figure()