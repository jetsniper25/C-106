import plotly.express as px
import csv
with open ("cups of coffee vs hours of sleep.csv")as csvfile:
    df=csv.DictReader(csvfile)
    fig=px.scatter(df,x="Coffee in ml",y="sleep in hours")
    fig.show()

