from impl.PasajeroDAOImpl import PasajeroDAOImpl

def main():
    dao = PasajeroDAOImpl()
    
    listas = dao.get_all_pasajero()

    for lista in listas:
        print(f"idPasajero={lista.idPasajero},nomPasajero={lista.nomPasajero},apellidoPasajero={lista.apellidoPasajero},fecNacPasajero={lista.fecNacPasajero},userMailPasajero={lista.userMailPasajero},direPasajero={lista.direPasajero},idRegion={lista.idRegion},idProvincia={lista.idProvincia},idComuna={lista.idComuna}")

if __name__ == "__main__":
    main()