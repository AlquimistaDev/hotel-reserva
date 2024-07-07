from impl.ReservaPasajeroDAOImpl import ReservaPasajeroDAOImpl

def main():
    dao = ReservaPasajeroDAOImpl()
    
    listas = dao.get_all_reservaPasajero()

    for lista in listas:
        print(f"idReservaPasajero={lista.idReservaPasajero}, idReserva={lista.idReserva}, idPasajero={lista.idPasajero}, costoPasajero={lista.costoPasajero}")

if __name__ == "__main__":
    main()