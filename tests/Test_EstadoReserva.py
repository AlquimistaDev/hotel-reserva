from impl.EstadoReservaDAOImpl import EstadoReservaDAOImpl

def main():
    dao = EstadoReservaDAOImpl()
    
    estados = dao.get_all_estadoReserva()

    for estado in estados:
        print(f"id: {estado.idEstadoReserva}, Descripción: {estado.descEstadoReserva}")

if __name__ == "__main__":
    main()