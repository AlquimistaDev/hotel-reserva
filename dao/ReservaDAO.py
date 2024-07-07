# Importamos las bibliotecas necesarias y el DTO para la reserva
from abc import ABC, abstractmethod
from typing import List
from dto.ReservaDTO import ReservaDTO  # Asegúrate de que este import sea correcto

class ReservaDAO(ABC):
    """
    Clase abstracta que define la interfaz de acceso a datos para las reservas.
    """

    @abstractmethod
    def get_all_reservas(self) -> List[ReservaDTO]:
        """
        Obtiene todas las reservas.

        :return: Una lista de objetos ReservaDTO que representan todas las reservas.
        """
        pass
    
    @abstractmethod
    def buscar_reserva(self, id_reserva: int) -> ReservaDTO:
        """
        Busca una reserva por su ID.

        :param id_reserva: ID de la reserva a buscar.
        :return: Un objeto ReservaDTO que representa la reserva encontrada.
        """
        pass
    
    @abstractmethod
    def crear_reserva(self, reserva: ReservaDTO) -> bool:
        """
        Crea una nueva reserva.

        :param reserva: Un objeto ReservaDTO que representa la nueva reserva.
        :return: True si la reserva fue creada exitosamente, False en caso contrario.
        """
        pass
    
    @abstractmethod
    def actualizar_reserva(self, reserva: ReservaDTO) -> bool:
        """
        Actualiza una reserva existente.

        :param reserva: Un objeto ReservaDTO que representa la reserva con los datos actualizados.
        :return: True si la reserva fue actualizada exitosamente, False en caso contrario.
        """
        pass
    
    @abstractmethod
    def eliminar_reserva(self, id_reserva: int) -> bool:
        """
        Elimina una reserva por su ID.

        :param id_reserva: ID de la reserva a eliminar.
        :return: True si la reserva fue eliminada exitosamente, False en caso contrario.
        """
        pass
