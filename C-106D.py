import plotly.express as px
import csv
import numpy as np

def getDatasource(dataPath):
    iceCreamSales=[]
    temperature=[]

    with open(dataPath)as csvFile:
        csvReader=csv.DictReader(csvFile)
        
        for row in csvReader:
            iceCreamSales.append(float(row["Coffee in ml"]))
            temperature.append(float(row["sleep in hours"]))

    return {"x":iceCreamSales,"y":temperature}

def findCorelation(datasource):
    Corelation=np.corrcoef(datasource["x"], datasource["y"])
    print("Corelation between Coffee vs sleep is", Corelation[0,1])    

def setup():
    dataPath="cups of coffee vs hours of sleep.csv"
    datasource=getDatasource(dataPath)
    findCorelation(datasource)

setup()
