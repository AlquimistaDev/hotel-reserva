from typing import List
import json
from DatabaseSingleton import DatabaseSingleton
from dto.OrientacionDTO import Orientacion
from dao.OrientacionDAO import OrientacionDAO

class OrientacionDAOImpl(OrientacionDAO):
    def __init__(self):
        self.db = DatabaseSingleton()
        self.queries= self.load_queries()
    
    
    def load_queries(self):
        with open('C:\\cursos\\reserva_hotel\\queries.json', 'r') as file:
            return json.load(file)
        

    def get_all_orientacion(self) -> List[Orientacion]:
        ListaOrientacion =[]
        conection = self.db.get_connection()
        cursor = conection.cursor(dictionary=True)
        sql = self.queries['listar_orientacion']

        cursor.execute(sql)
        rows = cursor.fetchall()

        for row in rows:
            try:
                lista = Orientacion(
                    idOrientacion	=int(row['ID_ORIENTACION']),
                    descOrientacion	=str(row['DESCRIPCION'])
                )
                ListaOrientacion.append(lista)
                
            except Exception as e:
                print(f"Error al crear ListaOrientacion con row: {row}")
                print(f"Error: {e}")

        cursor.close()

        return ListaOrientacion