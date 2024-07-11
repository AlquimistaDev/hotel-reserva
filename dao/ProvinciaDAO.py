from abc import ABC, abstractmethod
from typing import List
from dto.ProvinciaDTO import Provincia

class ProvinciaDAO(ABC):

    @abstractmethod
    def get_all_provincias(self) -> List[Provincia]:
        pass

