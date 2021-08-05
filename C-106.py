import plotly.express as px
import csv
with open ("Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv")as csvfile:
    df=csv.DictReader(csvfile)
    fig=px.scatter(df,x="Temperature",y="Ice-cream Sales")
    fig.show()
