from abc import ABC, abstractmethod
from typing import List
from dto.TipoCamaDTO import TipoCama

class TipoCamaDAO(ABC):
    
    @abstractmethod
    def get_all_tipoCama(self) -> List[TipoCama]:
        pass
    
