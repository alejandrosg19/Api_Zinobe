import  sqlite3
from sqlite3 import Error

class dataBase:
    def __init__(self):
        try:
            self.conexion = sqlite3.connect("Persistencia/database.db")
            self.objCursor = self.conexion.cursor()
            print("Conexion establecida")
        except Error:
            print("Ya hay una base de datos creada")
    
    def create_table(self):
        try:
            query = "CREATE TABLE regionCountry(Region text, Country text PRIMARY KEY, Language text, Time real)"
            self.objCursor.execute(query)
            self.conexion.commit()
        except Error:
            print("Ya hay una tabla creada con el mismo nombre")

    def insert_table(self, countrys):
        for i in countrys:
            try:
                self.objCursor.execute('INSERT INTO regionCountry VALUES(?, ?, ?, ?)', (i['region'], i['country'], i['language'], i['time']))
                self.conexion.commit()
            except Error:
                print("Ya hay un dato con la misma primary key")