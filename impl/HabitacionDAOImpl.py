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

        self.tipos_cama = {
            1: "Individual",
            2: "Doble",
            3: "Queen",
            4: "King"
        }
        self.orientaciones = {
            1: "Vista al mar",
            2: "Vista a la montaña",
            3: "Vista a la ciudad",
            4: "Vista al jardín"
        }
        self.estados_habitacion = {
            1: "Ocupada",
            2: "Vacante",
            3: "En mantenimiento",
            4: "Reservada"
        }

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

    def solicitar_datos_habitacion(self) -> HabitacionDTO:
        print("Crear nueva habitación:")
        numero_habitacion = int(input("Número de habitación: "))
        capacidad = int(input("Capacidad: "))

        print("\nTipos de cama disponibles:")
        for id_tipo, tipo in self.tipos_cama.items():
            print(f"{id_tipo}. {tipo}")
        id_tipo_cama = int(input("ID del tipo de cama: "))

        print("\nOrientaciones disponibles:")
        for id_orientacion, orientacion in self.orientaciones.items():
            print(f"{id_orientacion}. {orientacion}")
        id_orientacion = int(input("ID de orientación: "))

        print("\nEstados de habitación disponibles:")
        for id_estado, estado in self.estados_habitacion.items():
            print(f"{id_estado}. {estado}")
        id_estado_hab = int(input("ID del estado de habitación: "))

        return HabitacionDTO(
            id_habitacion=None,
            numero_habitacion=numero_habitacion,
            capacidad=capacidad,
            id_tipo_cama=id_tipo_cama,
            id_orientacion=id_orientacion,
            id_estado_hab=id_estado_hab
        )
    def crear_habitacion(self) -> bool:
        try:
            nueva_habitacion = self.solicitar_datos_habitacion()
            if self.insertar_habitacion_en_db(nueva_habitacion):
                print("Habitación creada exitosamente.")
                return True
            else:
                print("No se pudo crear la habitación.")
                return False
        except Exception as e:
            print(f"Error al crear habitación: {e}")
            return False

    
    def insertar_habitacion_en_db(self, habitacion: HabitacionDTO) -> bool:
        connection = self.db.get_connection()
        try:
            with connection.cursor() as cursor:
                # Validar que el número de habitación y la capacidad sean enteros positivos
                if habitacion.numero_habitacion <= 0 or habitacion.capacidad <= 0:
                    raise ValueError("El número de habitación y la capacidad deben ser enteros positivos.")

                # Validar que los valores de las claves foráneas sean válidos
                if habitacion.id_tipo_cama not in [1, 2, 3, 4]:
                    raise ValueError(f"El ID de tipo de cama {habitacion.id_tipo_cama} no es válido.")
                if habitacion.id_orientacion not in [1, 2, 3, 4]:
                    raise ValueError(f"El ID de orientación {habitacion.id_orientacion} no es válido.")
                if habitacion.id_estado_hab not in [1, 2, 3, 4]:
                    raise ValueError(f"El ID de estado de habitación {habitacion.id_estado_hab} no es válido.")

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

    def validar_datos_habitacion(self, habitacion):
        tipos_de_cama = ["individual", "doble", "queen", "king"]
        orientaciones_validas = ["Vista al mar", "Vista a la montaña", "Vista a la ciudad", "Vista al jardín"]
        estados_validos = ["Ocupada", "Vacante", "En mantenimiento", "Reservada"]

        if habitacion["tipo_cama"] not in tipos_de_cama:
            raise ValueError(f"Tipo de cama inválido: {habitacion['tipo_cama']}. Debe ser uno de: {', '.join(tipos_de_cama)}.")

        if habitacion["orientacion"] not in orientaciones_validas:
            raise ValueError(f"Orientación inválida: {habitacion['orientacion']}. Debe ser una de: {', '.join(orientaciones_validas)}.")

        if habitacion["estado"] not in estados_validos:
            raise ValueError(f"Estado inválido: {habitacion['estado']}. Debe ser uno de: {', '.join(estados_validos)}.")
        

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