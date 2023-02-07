import datetime as dt

import numpy as np
import pandas as pd
import plotly.express as px


def back_str_hour(date_str):
    try:
        return f"{date_str[:11]}{str(int(date_str[11:13]) - 1).zfill(2)}{date_str[13:]}"
    # one line is formatted as datetime and not string
    except TypeError:
        return str(date_str - dt.timedelta(hours=1))


df = pd.read_excel("Native_Load_2022.xlsx")

df["Hour Ending"] = df["Hour Ending"].apply(back_str_hour)

# df["Hour Ending"] = pd.to_datetime(df["Hour Ending"]) + dt.timedelta(hours=1)

fig = px.line(df, x="Hour Ending", y=df.columns.to_list()[1:])

# fig.show()

# subtract hour from string
# Convert datetime
# subtract hour from datetime
