from impl.UsuarioDAOImpl import UsuarioDAOImpl

def main():
    dao = UsuarioDAOImpl()
    
    listas = dao.get_all_usuario()

    for lista in listas:
        print(f"idUsuario={lista.idUsuario}, userNombre={lista.userNombre}, userApellido={lista.userApellido}, userMail={lista.userMail}, userPass={lista.userPass}, esAdmin={lista.esAdmin}")

   
   
   # Prompt : Usuario a Buscar
    idUsuario = int(input("Enter the user ID to search: "))
    # Utilice el método de instancia para buscar un usuario
    usuario = dao.buscar_usuario(idUsuario)
    if usuario:
        print(f"Usuario Encontrado: idUsuario={usuario.idUsuario}, userNombre={usuario.userNombre}, userApellido={usuario.userApellido}, userMail={usuario.userMail}, esAdmin={usuario.esAdmin}")
    else:
        print(f"Usuario No encontrado con ID {idUsuario}")



if __name__ == "__main__":
    main()