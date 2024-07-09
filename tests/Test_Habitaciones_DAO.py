from impl.HabitacionDAOImpl import HabitacionDAOImpl
from dto.HabitacionDTO import HabitacionDTO

def test_get_all_habitaciones():
    dao = HabitacionDAOImpl()
    habitaciones = dao.get_all_habitaciones()
    print("Listando todas las habitaciones:")
    for habitacion in habitaciones:
        print(habitacion)

def test_buscar_habitacion():
    dao = HabitacionDAOImpl()
    id_habitacion = 1  # Asume que existe una habitación con ID 1
    habitacion = dao.buscar_habitacion(id_habitacion)
    print(f"Buscando habitación con ID {id_habitacion}:")
    print(habitacion)

def test_crear_habitacion():
    dao = HabitacionDAOImpl()
    nueva_habitacion = HabitacionDTO(None, 101, 2, 1, 1, 1)
    resultado = dao.crear_habitacion(nueva_habitacion)
    print(f"Creación de nueva habitación: {'Exitosa' if resultado else 'Fallida'}")

def test_actualizar_habitacion():
    dao = HabitacionDAOImpl()
    habitacion_actualizada = HabitacionDTO(1, 101, 3, 2, 2, 1)
    resultado = dao.actualizar_habitacion(habitacion_actualizada)
    print(f"Actualización de habitación: {'Exitosa' if resultado else 'Fallida'}")

def test_eliminar_habitacion():
    dao = HabitacionDAOImpl()
    id_habitacion = 1  # Asume que existe una habitación con ID 1
    resultado = dao.eliminar_habitacion(id_habitacion)
    print(f"Eliminación de habitación con ID {id_habitacion}: {'Exitosa' if resultado else 'Fallida'}")

def main():
    test_get_all_habitaciones()
    test_buscar_habitacion()
    test_crear_habitacion()
    test_actualizar_habitacion()
    test_eliminar_habitacion()

if __name__ == "__main__":
    main()