from typing import List
import json
from .DatabaseSingleton import DatabaseSingleton
from dto.UsuarioDTO import Usuario
from dao.UsuarioDAO import UsuarioDAO

class UsuarioDAOImpl(UsuarioDAO):
    def __init__(self) -> None:
        self.db = DatabaseSingleton()
        self.queries = self.load_queries()

    def crear_usuario(self, usuario: Usuario) -> bool:
        connection = self.db.get_connection()
        try:
            with connection.cursor() as cursor:
                sql = self.queries['crear_usuario']
                cursor.execute(sql,(
                    usuario.USER_NOMBRE,
                    usuario.USER_APELLIDO,
                    usuario.USER_EMAIL,
                    usuario.CONTRASENA,
                    usuario.ES_ADMINISTRADOR
                ))
                connection.commit()
                return True
        except Exception as e:
            print(f"Error al crear usuario: {e}")
            connection.rollback()

    
    def actualizar_usuario(self, usuario: Usuario) -> bool:
        connection = self.db.get_connection()
        try:
            with connection.cursor() as cursor:
                sql = self.queries['actualizar_usuario']
                cursor.execute(sql,(
                    usuario.USER_NOMBRE,
                    usuario.USER_APELLIDO,
                    usuario.USER_EMAIL,
                    usuario.CONTRASENA,
                    usuario.ES_ADMINISTRADOR,
                    usuario.ID_USUARIO
                ))
                connection.commit()
                return cursor.rowcount >0
        except Exception as e:
            print(f"Error al actualizar usuario: {e}")
            connection.rollback()
            return False
        
    def eliminar_usuario(self, id_usuario: int) -> bool:
        connection = self.db.get_connection()
        try:
            with connection.cursor() as cursor:
                sql = self.queries['eliminar_usuario']
                cursor.execute(sql,(id_usuario,))
                connection.commit()
                return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar usuario: {e}")
            connection.rollback()
            return False
                

    
    def load_queries(self):
        with open('queries.json', 'r') as file:
            return json.load(file)
        
    def get_all_usuario(self) -> List[Usuario]:
        ListaUsuarios = []
        connection = self.db.get_connection()
        try: 
            with connection.cursor(dictionary=True) as cursor:       
                sql = self.queries['listar_usuarios']
                cursor.execute(sql)
                rows = cursor.fetchall()

                for row in rows:
                    try:
                        usuario = Usuario(
                            ID_USUARIO=row['ID_USUARIO'],
                            USER_NOMBRE=row['USER_NOMBRE'],
                            USER_APELLIDO=row['USER_APELLIDO'],
                            USER_EMAIL=row['USER_EMAIL'],
                            CONTRASENA=row['CONTRASENA'],
                            ES_ADMINISTRADOR=bool(row['ES_ADMINISTRADOR'])
                        )
                        ListaUsuarios.append(usuario)
                    except Exception as e:
                        print(f"Error al listar con row: {row}")
                        print(f"Error: {e}")
        except Exception as e:
            print(f"Error al obtener usuarios: {e}")
        
        return ListaUsuarios
    
    def buscar_usuario(self, idUsuario: int) -> Usuario:
        usuario_encontrado = None
        connection = self.db.get_connection()
        try:
            with connection.cursor(dictionary=True) as cursor:
                sql = self.queries['buscar_usuario']
                cursor.execute(sql, (idUsuario,))
                row = cursor.fetchone()
                
                if row:
                    usuario = Usuario(
                            ID_USUARIO=row['ID_USUARIO'],
                            USER_NOMBRE=row['USER_NOMBRE'],
                            USER_APELLIDO=row['USER_APELLIDO'],
                            USER_EMAIL=row['USER_EMAIL'],
                            CONTRASENA=row['CONTRASENA'],
                            ES_ADMINISTRADOR=bool(row['ES_ADMINISTRADOR'])
                    )
                    usuario_encontrado = usuario
        except Exception as e:
            print(f"Error al buscar el usuario: {e}")
        finally:
            connection.close()
        return usuario_encontrado