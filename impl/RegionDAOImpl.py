from typing import List
import json
from DatabaseSingleton import DatabaseSingleton
from dto.RegionDTO import Region
from dao.RegionDAO import RegionDAO

class RegionDAOImpl(RegionDAO):
    def __init__(self) -> None:
        self.db = DatabaseSingleton()
        self.queries= self.load_queries()
    
    
    def load_queries(self):
        with open('C:\\cursos\\reserva_hotel\\queries.json', 'r') as file:
            return json.load(file)
        


    def get_all_regiones(self) -> List[Region]:
        ListaRegiones= []

        conection = self.db.get_connection()
        cursor = conection.cursor(dictionary=True)
        sql = self.queries['listar_regiones']       
        
        cursor.execute(sql)
        rows = cursor.fetchall()

        for row in rows:
            try:
                lista = Region(
                    idRegion	= int(row['ID_REGION']), 
                    nomRegion	= str(row['NOMBRE_REGION']),
                    descRegion	= str(row['DESCRIPCION_REGION'])
                )
                ListaRegiones.append(lista)
                
            except Exception as e:
                print(f"Error al crear ListaRegiones con row: {row}")
                print(f"Error: {e}")

        cursor.close()
        return ListaRegiones