from impl.UsuarioAdminDAOImpl import UsuarioAdminDAOImpl

def main():
    dao = UsuarioAdminDAOImpl()
    
    listas = dao.get_all_usuarioAdmin()

    for lista in listas:
        print(f"idUsuarioAdmin={lista.idUsuarioAdmin}, idUsuario={lista.idUsuario}")

if __name__ == "__main__":
    main()