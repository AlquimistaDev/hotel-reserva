from impl.EstadoHabitacionDaoImpl import EstadoHabitacionDaoImpl

def main():
    dao = EstadoHabitacionDaoImpl()
    estados = dao.get_all_estadoHabitacion()
    for estado in estados:
        print(f"ID: {estado.idEstadoHab}, Descripción: {estado.descEstadoHab}")

if __name__ == "__main__":
    main()