from typing import List
import json
from DatabaseSingleton import DatabaseSingleton
from dao.ComunaDAO import ComunaDao
from dto.ComunaDTO import Comuna

class ComunaDaoImpl(ComunaDao):
    
    def __init__(self) -> None:
        self.db = DatabaseSingleton()
        self.queries= self.load_queries()
        
    def load_queries(self):
        with open('C:\\cursos\\reserva_hotel\\queries.json', 'r') as file:
            return json.load(file)
        

    def get_all_comunas(self) -> List[Comuna]:
        ListaComunas= []

        conection = self.db.get_connection()
        cursor = conection.cursor(dictionary=True)
        sql = self.queries['listar_comunas']
        cursor.execute(sql)
        rows = cursor.fetchall()
        
        for row in rows:
            try:
                lista = Comuna(
                    id_comuna	= int (row['ID_COMUNA']),
                    id_Pro	    = int (row['ID_PROVINCIA']),
                    nom_Com     = str (row['NOMBRE_COMUNA']),
                    des_Com	    = str (row['DESCRIPCION_COMUNA'])
                )
                ListaComunas.append(lista)
                
            except Exception as e:
                print(f"Error al crear ListaComunas con row: {row}")
                print(f"Error: {e}")

        cursor.close()
        return ListaComunas
