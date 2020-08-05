# -*- coding: utf-8 -*-

import dash
from dash.dependencies import Input, Output
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from pathlib import Path

## Load latest dataframes
from utils import get_latest_data
path_data = Path("./data")

path_antutu = sorted(path_data.glob("*antutu*"))[-1]
path_geekbench = sorted(path_data.glob("*geekbench*"))[-1]
path_gsmarena = sorted(path_data.glob("*gsmarena*"))[-1]
path_passmark = sorted(path_data.glob("*passmark*"))[-1]

df_antutu = pd.read_csv(path_antutu)
df_geekbench = pd.read_csv(path_geekbench)
df_gsmarena = pd.read_csv(path_gsmarena)
df_passmark = pd.read_csv(path_passmark)

## Remove Apple products :)
df_geekbench = df_geekbench[df_geekbench.name.str.find("iPhone")==-1]
df_geekbench = df_geekbench[df_geekbench.name.str.find("iPad")==-1]
df_geekbench = df_geekbench[df_geekbench.name.str.find("iPod")==-1]
df_gsmarena = df_gsmarena[df_gsmarena.name.str.find("Apple")==-1]


def make_table(df, id_="datatable"):
    return dash_table.DataTable(
        id=id_,
        columns=[
            {"name": i, "id": i, "deletable": False, "selectable": False} for i in df.columns
        ],
        data=df.to_dict('records'),
        editable=False,
        filter_action="native",
        sort_action="native",
        sort_mode="multi",
        row_selectable="multi",
        row_deletable=False,
        selected_columns=[],
        selected_rows=[],
        page_action="native",
        page_current= 0,
        page_size= 1400,
    )

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div(
        [make_table(df_passmark, id_="dt-passmark")],
        style={
            "display": "inline-block",
            "width": "26%",
            "margin": f"0.5%"
        }
    ),
    html.Div(
        [make_table(df_antutu, id_="dt-antutu")],
        style={
            "display": "inline-block",
            "width": "29%",
            "margin": f"0.5%"
        }
    ),
    html.Div(
        [make_table(df_geekbench, id_="dt-geekbench")],
        style={
            "display": "inline-block",
            "width": "19%",
            "margin": f"0.5%"
        }
    ),
    html.Div(
        [make_table(df_gsmarena, id_="dt-gsmarena")],
        style={
            "display": "inline-block",
            "width": "22%",
            "margin": f"0.5%"
        }
    ),
],
style={
    "place-items": "center"
})



if __name__ == '__main__':
    app.run_server(
        host="0.0.0.0",
        debug=True
    )