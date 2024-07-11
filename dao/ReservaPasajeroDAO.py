from abc import ABC, abstractmethod
from typing import List
from dto.ReservaPasajeroDTO import ReservaPasajero

class ReservaPasajeroDAO(ABC):
    
    @abstractmethod
    def get_all_reservaPasajero(self) -> List[ReservaPasajero]:
        pass
    
