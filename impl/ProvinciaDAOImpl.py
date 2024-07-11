from typing import List
import json
from DatabaseSingleton import DatabaseSingleton
from dto.ProvinciaDTO import Provincia
from dao.ProvinciaDAO import ProvinciaDAO

class ProvinciaDAOImpl (ProvinciaDAO):
    def __init__(self) -> None:
        self.db = DatabaseSingleton()
        self.queries= self.load_queries()
    
    
    def load_queries(self):
        with open('C:\\cursos\\reserva_hotel\\queries.json', 'r') as file:
            return json.load(file)
        


    def get_all_provincias(self) -> List[Provincia]:
        ListaProvncias= []

        conection = self.db.get_connection()
        cursor = conection.cursor(dictionary=True)
        sql = self.queries['listar_provincias']

        cursor.execute(sql)
        rows = cursor.fetchall()

        for row in rows:
            try:
                lista = Provincia(
                    idProvincia		=int(row['ID_PROVINCIA']),
                    idRegion		=int(row['ID_REGION']),
                    nomProvincia	=str(row['NOMBRE_PROVINCIA']),
                    descProvincia	=str(row['DESCRIPCION_PROVINCIA'])
                )
                ListaProvncias.append(lista)
                
            except Exception as e:
                print(f"Error al crear ListaHabitaciones con row: {row}")
                print(f"Error: {e}")

        cursor.close()
        return ListaProvncias