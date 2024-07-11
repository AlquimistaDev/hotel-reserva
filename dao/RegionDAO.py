from abc import ABC, abstractmethod
from typing import List
from dto.RegionDTO import Region

class RegionDAO(ABC):
    
    @abstractmethod
    def get_all_regiones(self) -> List[Region]:
        pass
    
