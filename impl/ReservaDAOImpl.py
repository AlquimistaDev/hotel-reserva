from typing import List
import json
from .DatabaseSingleton import DatabaseSingleton
from dto.ReservaDTO import ReservaDTO
from dao.ReservaDAO import ReservaDAO
import mysql.connector

class ReservaDAOImpl(ReservaDAO):
    def __init__(self) -> None:
        self.db = DatabaseSingleton()
        self.queries = self.load_queries()

    def load_queries(self):
        with open('C:\\cursos\\reserva_hotel\\queries.json', 'r') as file:
            return json.load(file)

    def get_all_reservas(self) -> List[ReservaDTO]:
        lista_reservas = []
        connection = self.db.get_connection()
        try:
            with connection.cursor(dictionary=True) as cursor:
                cursor.execute(self.queries['listar_reservas'])
                rows = cursor.fetchall()
                for row in rows:
                    reserva = ReservaDTO(
                        id_reserva=row['ID_RESERVA'],
                        fec_reserva=row['FEC_RESERVA'],
                        fec_llegada=row['FEC_LLEGADA'],
                        fec_salida=row['FEC_SALIDA'],
                        cant_pasajeros=row['CANT_PASAJEROS'],
                        monto_total=row['MONTO_TOTAL'],
                        id_estado_reserva=row['ID_ESTADO_RESERVA'],
                        penalizacion=row['PENALIZACION'],
                        id_habitacion=row['ID_HABITACION']
                        )
                    lista_reservas.append(reserva)
        except Exception as e:
            print(f"Error al obtener reservas: {e}")
        finally:
            connection.close()
        return  lista_reservas

    def buscar_reserva(self, id_reserva: int) -> ReservaDTO:
        connection = self.db.get_connection()
        try:
            with connection.cursor(dictionary=True) as cursor:
                sql = self.queries['buscar_reserva']
                #print(f"SQL query: {sql}") #depuracion de codigo
                #print(f"ID_RESERVA: {id_reserva}") #depuracion de codigo
                cursor.execute(sql, {'id': id_reserva},)
                row = cursor.fetchone()
                if row:
                    return ReservaDTO(
                    id_reserva=row['ID_RESERVA'],
                    fec_reserva=row['FEC_RESERVA'],
                    fec_llegada=row['FEC_LLEGADA'],
                    fec_salida=row['FEC_SALIDA'],
                    cant_pasajeros=row['CANT_PASAJEROS'],
                    monto_total=row['MONTO_TOTAL'],
                    id_estado_reserva=row['ID_ESTADO_RESERVA'],
                    penalizacion=row['PENALIZACION'],
                    id_habitacion=row['ID_HABITACION']
                    )
        except mysql.connector.Error as e:
            print(f"Error  de MySQL al buscar reserva: {e}")
            print(f"Tipo de error: {type(e)}") # informacion sobre el error
        except Exception as e:
            print(f"Error inesperado al buscar reserva: {e}")
            print(f"Tipo de error: {type(e)}")
        finally:
            connection.close()
        return None

    def crear_reserva(self, reserva: ReservaDTO) -> bool:
        connection = self.db.get_connection()
        try:
            with connection.cursor() as cursor:
                sql = self.queries['crear_reserva']
                cursor.execute(sql, (
                    reserva.fec_reserva, 
                    reserva.fec_llegada, 
                    reserva.fec_salida, 
                    reserva.cant_pasajeros, 
                    reserva.monto_total, 
                    reserva.id_estado_reserva,
                    reserva.penalizacion,
                    reserva.id_habitacion
                ))
                connection.commit()
                return True
        except Exception as e:
            print(f"Error al crear reserva: {e}")
            connection.rollback()
        finally:
            connection.close()
        return False

    def actualizar_reserva(self, reserva: ReservaDTO) -> bool:
        connection = self.db.get_connection()
        try:
            with connection.cursor() as cursor:
                sql = self.queries['actualizar_reserva']
                cursor.execute(sql, (
                    reserva.fec_reserva, 
                    reserva.fec_llegada, 
                    reserva.fec_salida, 
                    reserva.cant_pasajeros, 
                    reserva.monto_total, 
                    reserva.id_estado_reserva,
                    reserva.penalizacion,
                    reserva.id_habitacion,
                    reserva.id_reserva
                ))
                connection.commit()
                return True
        except Exception as e:
            print(f"Error al actualizar reserva: {e}")
            connection.rollback()
        finally:
            connection.close()
        return False

    def eliminar_reserva(self, id_reserva: int) -> bool:
        connection = self.db.get_connection()
        try:
            with connection.cursor() as cursor:
                sql = self.queries['eliminar_reserva']
                cursor.execute(sql, (id_reserva,))
                connection.commit()
                return True
        except Exception as e:
            print(f"Error al eliminar reserva: {e}")
            connection.rollback()
        finally:
            connection.close()
        return False