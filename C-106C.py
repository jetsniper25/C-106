import plotly.express as px
import csv
import numpy as np

def getDatasource(dataPath):
    iceCreamSales=[]
    temperature=[]

    with open(dataPath)as csvFile:
        csvReader=csv.DictReader(csvFile)
        
        for row in csvReader:
            iceCreamSales.append(float(row["Ice-cream Sales"]))
            temperature.append(float(row["Temperature"]))

    return {"x":iceCreamSales,"y":temperature}

def findCorelation(datasource):
    Corelation=np.corrcoef(datasource["x"], datasource["y"])
    print("Corelation between Temperature vs Ice-cream sales is", Corelation[0,1])    

def setup():
    dataPath="Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv"
    datasource=getDatasource(dataPath)
    findCorelation(datasource)

setup()
