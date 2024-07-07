from impl.ReservaDAOImpl import ReservaDAOImpl

def main():
    dao = ReservaDAOImpl()
    
    listas = dao.get_all_reserva()

    for lista in listas:
        print(f"idReserva={lista.idReserva},fecReserva={lista.fecReserva},fecLlegada={lista.fecLlegada},fecSalida={lista.fecSalida},cantPasajeros={lista.cantPasajeros},montoTotal={lista.montoTotal},idEstadoReserva={lista.idEstadoReserva},penalizacion={lista.penalizacion},idHabitacion={lista.idHabitacion}")

if __name__ == "__main__":
    main()