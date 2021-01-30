from Src.regionCountry import regionCountry
from Src.dataBase import dataBase
from Vista.Table import Table
import pandas
import json

class Api:
    def __init__(self):
        self.RC = regionCountry() 
        self.Conexion = dataBase()
        self.Ventana = Table()

    def run(self):
        regions = self.RC.regions()
        countrys = self.RC.countrys(regions)

        dataFrame = pandas.DataFrame(countrys)

        TTotal= "%.5f" %dataFrame['time'].sum()
        TPromedio= "%.5f" %dataFrame['time'].mean()
        TMinimo = "%.5f" %dataFrame['time'].min()
        TMaximo = "%.5f" %dataFrame['time'].max()

        statistics = "Tiempo Total: "+TTotal
        statistics += "\nTiempo Promedio: "+TPromedio
        statistics += "\nTiempo Minimo: "+TMinimo
        statistics += "\nTiempo Maximo: "+TMaximo

        print(dataFrame)
        print(statistics)

        self.Conexion.create_table()
        self.Conexion.insert_table(countrys)

        dataFrame.to_json("data.json")

        self.Ventana.show_Table(countrys, TTotal, TPromedio, TMinimo, TMaximo)

if __name__ == "__main__":
    api = Api()
    api.run()

    
    

