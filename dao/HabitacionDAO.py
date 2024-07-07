from abc import ABC, abstractmethod
from typing import List
from dto.HabitacionDTO import HabitacionDTO

class HabitacionDAO(ABC):
    
    @abstractmethod
    def get_all_habitaciones(self) -> List[HabitacionDTO]:
        pass
    
    @abstractmethod
    def buscar_habitacion(self, id_habitacion: int) -> HabitacionDTO:
        pass
    
    @abstractmethod
    def crear_habitacion(self, habitacion: HabitacionDTO) -> bool:
        pass
    
    @abstractmethod
    def actualizar_habitacion(self, habitacion: HabitacionDTO) -> bool:
        pass
    
    @abstractmethod
    def eliminar_habitacion(self, id_habitacion: int) -> bool:
        pass