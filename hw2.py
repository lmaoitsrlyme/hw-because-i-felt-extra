import pandas as pd
import plotly.express as px

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
df = pd.read_csv("Copy+of+data+-+data.csv")
fig = px.line(df, x = "date", y = "cases", color = "country")
fig.show()
