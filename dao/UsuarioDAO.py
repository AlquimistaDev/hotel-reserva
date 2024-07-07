# Importamos las bibliotecas necesarias y el DTO para el usuario
from abc import ABC, abstractmethod
from typing import List
from dto.UsuarioDTO import Usuario  # Asegúrate de que este import sea correcto

class UsuarioDAO(ABC):
    """
    Clase abstracta que define la interfaz de acceso a datos para los usuarios.
    """

    @abstractmethod
    def get_all_usuario(self) -> List[Usuario]:
        """
        Obtiene todos los usuarios.

        :return: Una lista de objetos Usuario que representan todos los usuarios.
        """
        pass
    
    @abstractmethod
    def buscar_usuario(self, idUsuario: int) -> Usuario:
        """
        Busca un usuario por su ID.

        :param idUsuario: ID del usuario a buscar.
        :return: Un objeto Usuario que representa el usuario encontrado.
        """
        pass
