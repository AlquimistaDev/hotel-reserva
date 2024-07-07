
from impl.ComunaDaoImpl import ComunaDaoImpl

def main():
    dao = ComunaDaoImpl()
    
    listas = dao.get_all_comunas()

    for lista in listas:
        print(f"id_comuna={lista.id_comuna}, id_Pro={lista.id_Pro}, nom_Com={lista.nom_Com}, des_Com={lista.des_Com}")

   

if __name__ == "__main__":
    main()
    