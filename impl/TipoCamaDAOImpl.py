from typing import List
import json
from DatabaseSingleton import DatabaseSingleton
from dto.TipoCamaDTO import TipoCama
from dao.TipoCamaDAO import TipoCamaDAO

class TipoCamaDAOImpl(TipoCamaDAO):

    def __init__(self) -> None:
        self.db = DatabaseSingleton()
        self.queries= self.load_queries()
    
    
    def load_queries(self):
        with open('C:\\cursos\\reserva_hotel\\queries.json', 'r') as file:
            return json.load(file)
        


    def get_all_tipoCama(self) -> List[TipoCama]:
        ListaTipoCama= []

        conection = self.db.get_connection()
        cursor = conection.cursor(dictionary=True)
        sql = self.queries['listar_tipo_cama']

        cursor.execute(sql)
        rows = cursor.fetchall()

        for row in rows:
            try:
                lista = TipoCama(
                    idTipoCama	=int (row['ID_TIPO_CAMA']),
                    tipoCama	=str (row['TIPO_CAMA'])
                )
                ListaTipoCama.append(lista)
                
            except Exception as e:
                print(f"Error al crear ListaTipoCama con row: {row}")
                print(f"Error: {e}")

        cursor.close()
        return ListaTipoCama
    
    