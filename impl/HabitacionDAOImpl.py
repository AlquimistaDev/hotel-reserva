from typing import List
import json
from dao.HabitacionDAO import HabitacionDAO
from dto.HabitacionDTO import HabitacionDTO
from .DatabaseSingleton import DatabaseSingleton
import mysql.connector

class HabitacionDAOImpl(HabitacionDAO):
    def __init__(self):
        self.db = DatabaseSingleton()
        self.queries = self.load_queries()

    def load_queries(self):
        with open('queries.json', 'r') as file:
            return json.load(file)

    def get_all_habitaciones(self) -> List[HabitacionDTO]:
        habitaciones = []
        connection = self.db.get_connection()
        try:
            with connection.cursor(dictionary=True) as cursor:
                cursor.execute(self.queries['listar_habitaciones'])
                for row in cursor.fetchall():
                    habitaciones.append(HabitacionDTO(
                        id_habitacion=row['ID_HABITACION'],
                        numero_habitacion=row['NUMERO_HABITACION'],
                        capacidad=row['CAPACIDAD'],
                        id_tipo_cama=row['ID_TIPO_CAMA'],
                        id_orientacion=row['ID_ORIENTACION'],
                        id_estado_hab=row['ID_ESTADO_HAB']
                    ))
        except Exception as e:
            print(f"Error al obtener habitaciones: {e}")
        finally:
            connection.close()
        return habitaciones

    def buscar_habitacion(self, id_habitacion: int) -> HabitacionDTO:
        connection = self.db.get_connection()
        try:
            with connection.cursor(dictionary=True) as cursor:
                cursor.execute(self.queries['buscar_habitacion'], {'id': id_habitacion})
                row = cursor.fetchone()
                if row:
                    return HabitacionDTO(
                        id_habitacion=row['ID_HABITACION'],
                        numero_habitacion=row['NUMERO_HABITACION'],
                        capacidad=row['CAPACIDAD'],
                        id_tipo_cama=row['ID_TIPO_CAMA'],
                        id_orientacion=row['ID_ORIENTACION'],
                        id_estado_hab=row['ID_ESTADO_HAB']
                    )
        except Exception as e:
            print(f"Error al buscar habitación: {e}")
        finally:
            connection.close()
        return None

    def crear_habitacion(self, habitacion: HabitacionDTO) -> bool:
        connection = self.db.get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute(self.queries['crear_habitacion'], {
                    'numero': habitacion.numero_habitacion,
                    'capacidad': habitacion.capacidad,
                    'tipo_cama': habitacion.id_tipo_cama,
                    'orientacion': habitacion.id_orientacion,
                    'estado': habitacion.id_estado_hab
                })
                connection.commit()
                return True
        except Exception as e:
            print(f"Error al crear habitación: {e}")
            connection.rollback()
            return False
        finally:
            connection.close()

    def actualizar_habitacion(self, habitacion: HabitacionDTO) -> bool:
        connection = self.db.get_connection()
        try:
            with connection.cursor() as cursor:
                cursor.execute(self.queries['actualizar_habitacion'], {
                    'id': habitacion.id_habitacion,
                    'numero': habitacion.numero_habitacion,
                    'capacidad': habitacion.capacidad,
                    'tipo_cama': habitacion.id_tipo_cama,
                    'orientacion': habitacion.id_orientacion,
                    'estado': habitacion.id_estado_hab
                })
                connection.commit()
                return True
        except Exception as e:
            print(f"Error al actualizar habitación: {e}")
            connection.rollback()
            return False
        finally:
            connection.close()

    def eliminar_habitacion(self, id_habitacion: int) -> bool:
        connection = self.db.get_connection()
        try:
            with connection.cursor() as cursor:
                 # Primero, verifica si hay reservas asociadas
                cursor.execute("SELECT COUNT(*) as count FROM hotel_mpc.tbl_reserva WHERE ID_HABITACION = %s", (id_habitacion,))
                count = cursor.fetchone()[0] # accedemos al primer elemento de la tupla
                

            if count > 0:
                # Si hay reservas, desactivamos la habitación en lugar de eliminarla
                with connection.cursor() as  cursor:
                    cursor.execute("UPDATE hotel_mpc.tbl_habitacion SET activo = FALSE WHERE ID_HABITACION = %s", (id_habitacion,))
                    connection.commit()
                print(f"La habitación tiene {count} reserva(s) asociada(s). Se ha marcado como inactiva.")
                return True
            else:
                with connection.cursor() as cursor:
                # Si no hay reservas, procedemos con la eliminación física
                    cursor.execute(self.queries['eliminar_habitacion'], {'id': id_habitacion})
                    connection.commit()
                print("Habitación eliminada exitosamente.")
                return True
        except mysql.connector.Error as e:
            print(f"Error en MySQL al eliminar habitaciones: {e}")
            connection.rollback()
            return False
        except Exception as e:
            print(f"Error al eliminar habitación: {e}")
            connection.rollback()
            return False
        finally:
            connection.close()