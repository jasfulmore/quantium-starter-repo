from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash()

df1 = pd.read_csv('quantium-starter-repo/data/daily_sales_data_0.csv')
df2 = pd.read_csv('quantium-starter-repo/data/daily_sales_data_1.csv')
df3 = pd.read_csv('quantium-starter-repo/data/daily_sales_data_2.csv')

combined = pd.concat([df1, df2, df3], ignore_index=True)


if __name__ == '__main__':
    app.run(debug=True)
