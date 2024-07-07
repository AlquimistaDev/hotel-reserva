from impl.RegionDAOImpl import RegionDAOImpl

def main():
    dao = RegionDAOImpl()
    
    listas = dao.get_all_regiones()

    for lista in listas:
        print(f"idRegion={lista.idRegion}, nomRegion={lista.nomRegion}, descRegion={lista.descRegion}")

if __name__ == "__main__":
    main()