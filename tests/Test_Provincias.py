from impl.ProvinciaDAOImpl import ProvinciaDAOImpl

def main():
    dao = ProvinciaDAOImpl()
    
    listas = dao.get_all_provincias()

    for lista in listas:
        print(f"idProvincia={lista.idProvincia}, idRegion={lista.idRegion}, nomProvincia={lista.nomProvincia}, descProvincia={lista.descProvincia}")

if __name__ == "__main__":
    main()