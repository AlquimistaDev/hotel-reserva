from typing import List
import json
from DatabaseSingleton import DatabaseSingleton
from dto.PasajeroDTO import Pasajero
from dao.PasajeroDAO import PasajeroDAO
from datetime import date

class PasajeroDAOImpl(PasajeroDAO):
    def __init__(self) -> None:
        self.db = DatabaseSingleton()  
        self.queries= self.load_queries()
    
    
    def load_queries(self):
        with open('C:\\cursos\\reserva_hotel\\queries.json', 'r') as file:
            return json.load(file)
        

    def get_all_pasajero(self) -> List[Pasajero]:
        ListaPasajeros= []
        conection = self.db.get_connection()
        cursor = conection.cursor(dictionary=True)
        sql = self.queries['listar_pasajeros']
        
        cursor.execute(sql)
        rows = cursor.fetchall()

        for row in rows:
            try:
                lista = Pasajero(
                    idPasajero			=int (row['ID_PASAJERO']),
                    nomPasajero			=str (row['NOMBRE_PASAJERO']),
                    apellidoPasajero	=str (row['APELLIDO_PASAJERO']),
                    fecNacPasajero		=(row['FEC_NAC_PASAJERO']),
                    userMailPasajero	=str (row['USER_EMAIL_PASAJERO']),
                    direPasajero		=str (row['DIRE_PASAJERO']),
                    idRegion			=int (row['ID_REGION']),
                    idProvincia			=int (row['ID_PROVINCIA']),
                    idComuna			=int (row['ID_COMUNA'])
                )
                ListaPasajeros.append(lista)
                
            except Exception as e:
                print(f"Error al crear ListaPasajeros con row: {row}")
                print(f"Error: {e}")

        cursor.close()

        return ListaPasajeros
