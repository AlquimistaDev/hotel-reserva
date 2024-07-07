from impl.TipoCamaDAOImpl import TipoCamaDAOImpl

def main():
    dao = TipoCamaDAOImpl()
    
    listas = dao.get_all_tipoCama()

    for lista in listas:
        print(f"idtipoCama={lista.idTipoCama}, tipoCama={lista.tipoCama}")

if __name__ == "__main__":
    main()