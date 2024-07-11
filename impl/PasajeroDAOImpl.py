from typing import List
import json
from dao.PasajeroDAO import PasajeroDAO
from dto.PasajeroDTO import PasajeroDTO
from .DatabaseSingleton import DatabaseSingleton
import mysql.connector

class PasajeroDAOImpl(PasajeroDAO):
    def __init__(self):
        self.db = DatabaseSingleton()
        self.queries = self.load_queries()

    def load_queries(self):
        with open('C:\\cursos\\reserva_hotel\\queries.json', 'r') as file:
            return json.load(file)

    def get_all_pasajeros(self) -> List[PasajeroDTO]:
        pasajeros = []
        connection = self.db.get_connection()
        try:
            with connection.cursor(dictionary=True) as cursor:
                cursor.execute(self.queries['listar_pasajeros'])
                for row in cursor.fetchall():
                    pasajeros.append(PasajeroDTO(ID_PASAJERO=row['ID_PASAJERO'],
                            NOMBRE_PASAJERO=row['NOMBRE_PASAJERO'],
                            APELLIDO_PASAJERO=row['APELLIDO_PASAJERO'],
                            FEC_NAC_PASAJERO=row['FEC_NAC_PASAJERO'],
                            USER_EMAIL_PASAJERO=row['USER_EMAIL_PASAJERO'],
                            DIRE_PASAJERO=row['DIRE_PASAJERO'],
                            ID_REGION=row['ID_REGION'],
                            ID_PROVINCIA=row['ID_PROVINCIA'],
                            ID_COMUNA=row['ID_COMUNA']))
        except Exception as e:
            print(f"Error al obtener pasajeros: {e}")
        finally:
            connection.close()
        return pasajeros

    def buscar_pasajero(self, id_pasajero: int) -> PasajeroDTO:
        connection = self.db.get_connection()
        try:
            with connection.cursor(dictionary=True) as cursor:
                cursor.execute(self.queries['buscar_pasajero'], {'id': id_pasajero})
                row = cursor.fetchone()
                if row:
                    return PasajeroDTO(
                    ID_PASAJERO=row['ID_PASAJERO'],
                    NOMBRE_PASAJERO=row['NOMBRE_PASAJERO'],
                    APELLIDO_PASAJERO=row['APELLIDO_PASAJERO'],
                    FEC_NAC_PASAJERO=row['FEC_NAC_PASAJERO'],
                    USER_EMAIL_PASAJERO=row['USER_EMAIL_PASAJERO'],
                    DIRE_PASAJERO=row['DIRE_PASAJERO'],
                    ID_REGION=row['ID_REGION'],
                    ID_PROVINCIA=row['ID_PROVINCIA'],
                    ID_COMUNA=row['ID_COMUNA']
                )
        except Exception as e:
            print(f"Error al buscar pasajero: {e}")
        finally:
            connection.close()
        return None

    def crear_pasajero(self, pasajero: PasajeroDTO) -> bool:
        connection = self.db.get_connection()
        try:
            # Verificar que los campos obligatorios no estén vacíos
            if not pasajero.NOMBRE_PASAJERO or not pasajero.APELLIDO_PASAJERO or not pasajero.USER_EMAIL_PASAJERO or not pasajero.DIRE_PASAJERO:
                raise ValueError("Todos los campos obligatorios deben ser llenados.")

            # Verificar que los valores de las claves foráneas sean válidos
            with connection.cursor() as cursor:
                cursor.execute("SELECT COUNT(*) FROM TBL_REGION WHERE ID_REGION = %s", (pasajero.ID_REGION,))
                if cursor.fetchone()[0] == 0:
                    raise ValueError(f"La región con ID {pasajero.ID_REGION} no existe.")
                cursor.execute("SELECT COUNT(*) FROM TBL_PROVINCIAS WHERE ID_PROVINCIA = %s", (pasajero.ID_PROVINCIA,))
                if cursor.fetchone()[0] == 0:
                    raise ValueError(f"La provincia con ID {pasajero.ID_PROVINCIA} no existe.")
                cursor.execute("SELECT COUNT(*) FROM TBL_COMUNAS WHERE ID_COMUNA = %s", (pasajero.ID_COMUNA,))
                if cursor.fetchone()[0] == 0:
                    raise ValueError(f"La comuna con ID {pasajero.ID_COMUNA} no existe.")

            with connection.cursor() as cursor:
                sql = self.queries['crear_pasajero']
                cursor.execute(sql, (
                    pasajero.NOMBRE_PASAJERO,
                    pasajero.APELLIDO_PASAJERO,
                    pasajero.FEC_NAC_PASAJERO,
                    pasajero.USER_EMAIL_PASAJERO,
                    pasajero.DIRE_PASAJERO,
                    pasajero.ID_REGION,
                    pasajero.ID_PROVINCIA,
                    pasajero.ID_COMUNA
                ))
            connection.commit()
            return True
        except Exception as e:
            print(f"Error al crear pasajero: {e}")
            connection.rollback()
            return False
        finally:
            connection.close()

    def actualizar_pasajero(self, pasajero: PasajeroDTO) -> bool:
        print('DENTRO DEL DAO:::',pasajero)
        connection = self.db.get_connection()
        try:
            with connection.cursor() as cursor:
                sql = self.queries['actualizar_pasajero']
                cursor.execute(sql, (
                    pasajero.NOMBRE_PASAJERO,
                    pasajero.APELLIDO_PASAJERO,
                    pasajero.FEC_NAC_PASAJERO,
                    pasajero.USER_EMAIL_PASAJERO,
                    pasajero.DIRE_PASAJERO,
                    pasajero.ID_REGION,
                    pasajero.ID_PROVINCIA,
                    pasajero.ID_COMUNA,
                    pasajero.ID_PASAJERO
                ))
                connection.commit()
                return True
        except Exception as e:
            print(f"Error al actualizar pasajero: {e}")
            connection.rollback()
            return False
        finally:
            connection.close()

    def eliminar_pasajero(self, id_pasajero: int) -> bool:
        connection = self.db.get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute(self.queries['eliminar_pasajero'], (id_pasajero,))
                connection.commit()
                return True
        except Exception as e:
            print(f"Error al eliminar pasajero: {e}")
            connection.rollback()
            return False
        finally:
            connection.close()