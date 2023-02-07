import datetime as dt
import sqlite3

import numpy as np
import pandas as pd
import plotly.express as px

from data import import_files

df = import_files()

# pd.to_sql("data/main.db", conn)

# fig = px.line(df, x="Hour Ending", y=df.columns.to_list()[1:])

# fig.show()
