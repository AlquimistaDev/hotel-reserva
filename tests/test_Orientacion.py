from impl.OrientacionDAOImpl import OrientacionDAOImpl

def main():
    dao = OrientacionDAOImpl()
    
    listas = dao.get_all_orientacion()

    for lista in listas:
        print(f"idOrientacion={lista.idOrientacion}, descOrientacion={lista.descOrientacion}")

if __name__ == "__main__":
    main()