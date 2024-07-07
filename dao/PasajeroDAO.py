from abc import ABC, abstractmethod
from typing import List
from dto.PasajeroDTO import PasajeroDTO

class PasajeroDAO(ABC):
    
    @abstractmethod
    def get_all_pasajeros(self) -> List[PasajeroDTO]:
        pass
    
    @abstractmethod
    def buscar_pasajero(self, id_pasajero: int) -> PasajeroDTO:
        pass
    
    @abstractmethod
    def crear_pasajero(self, pasajero: PasajeroDTO) -> bool:
        pass
    
    @abstractmethod
    def actualizar_pasajero(self, pasajero: PasajeroDTO) -> bool:
        pass
    
    @abstractmethod
    def eliminar_pasajero(self, id_pasajero: int) -> bool:
        pass