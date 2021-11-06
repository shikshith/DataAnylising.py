import csv
import pandas as pz
import plotly.graph_objects as pgo

df=pz.read_csv("data.csv")

Info=df.loc[df['student_id']=="TRL_987"]
print(Info.groupby("level")["attempt"].mean())

fig=pgo.Figure(pgo.Scatter(x=Info.groupby("level")["attempt"].mean(),
                     y=["Level 1","Level 2","Level 3","Level 4"],
                     orientation='v'))

fig.show()