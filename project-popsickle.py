import datetime as dt

import numpy as np
import pandas as pd
import plotly.express as px


def back_str_hour(date_str):
    try:
        # don't go to end of string to cut out DST
        return (
            f"{date_str[:11]}{str(int(date_str[11:13]) - 1).zfill(2)}{date_str[13:16]}"
        )
    # one line is formatted as datetime and not string
    except TypeError:
        return str(date_str - dt.timedelta(hours=1))


def clean_df(df):
    df["Hour Ending"] = df["Hour Ending"].apply(back_str_hour)
    df["Hour Ending"] = pd.to_datetime(df["Hour Ending"]) + dt.timedelta(hours=1)


rename_dict = {
    "HourEnding": "Hour Ending",
    "Hour_End": "Hour Ending",
    "FAR_WEST": "FWEST",
    "NORTH_C": "NCENT",
    "SOUTHERN": "SOUTH",
    "SOUTH_C": "SCENT",
    "SOUTH_C": "SCENT",
}

file_list = ["Native_Load_2022.xlsx", "Native_Load_2021.xlsx"]


# df_2022 = pd.read_excel("Native_Load_2022.xlsx")
# df_2021 = pd.read_excel("Native_Load_2021.xlsx")
# df_2020 = pd.read_excel("Native_Load_2020.xlsx").rename(columns=rename_dict)
# df_2019 = pd.read_excel("Native_Load_2019.xlsx").rename(columns=rename_dict)
# df_2018 = pd.read_excel("Native_Load_2018.xlsx").rename(columns=rename_dict)
# df_2017 = pd.read_excel("native_Load_2017.xlsx").rename(columns=rename_dict)
# df_2016 = pd.read_excel("native_Load_2016.xlsx").rename(columns=rename_dict)
# df_2015 = pd.read_excel("native_load_2015.xls").rename(columns=rename_dict)
# df_2014 = pd.read_excel("2014_ercot_hourly_load_data.xls").rename(columns=rename_dict)
# df_2013 = pd.read_excel("2013_ercot_hourly_load_data.xls").rename(columns=rename_dict)
# df_2012 = pd.read_excel("2012_ercot_hourly_load_data.xls").rename(columns=rename_dict)
# df_2011 = pd.read_excel("2011_ercot_hourly_load_data.xls").rename(columns=rename_dict)
# df_2010 = pd.read_excel("2010_ercot_hourly_load_data.xls").rename(columns=rename_dict)
# df_2009 = pd.read_excel("2009_ercot_hourly_load_data.xls").rename(columns=rename_dict)
# df_2008 = pd.read_excel("2008_ercot_hourly_load_data.xls").rename(columns=rename_dict)
# df_2007 = pd.read_excel("2007_ercot_hourly_load_data.xls").rename(columns=rename_dict)
# df_2006 = pd.read_excel("2006_ercot_hourly_load_data.xls").rename(columns=rename_dict)
# df_2005 = pd.read_excel("2005_ercot_hourly_load_data.xls").rename(columns=rename_dict)
# df_2004 = pd.read_excel("2004_ercot_hourly_load_data.xls").rename(columns=rename_dict)
# df_2003 = pd.read_excel("2003_ercot_hourly_load_data.xls").rename(columns=rename_dict)


for idx, file_name in enumerate(file_list):
    if idx == 0:
        df = pd.read_excel(file_list[0]).rename(columns=rename_dict)
    else:
        tmp_df = pd.read_excel(file_name).rename(columns=rename_dict)
        print(df)
        print(tmp_df)
        df = pd.concat([df, tmp_df])

# fig = px.line(df, x="Hour Ending", y=df.columns.to_list()[1:])

# fig.show()
