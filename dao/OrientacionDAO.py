from abc import ABC, abstractmethod
from typing import List
from dto.OrientacionDTO import Orientacion

class OrientacionDAO(ABC):
    
    @abstractmethod
    def get_all_orientacion(self) -> List[Orientacion]:
        pass
    
