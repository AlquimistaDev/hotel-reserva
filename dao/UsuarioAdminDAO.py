from abc import ABC, abstractmethod
from typing import List
from dto.UsuarioAdminDTO import UsuarioAdmin

class UsuarioAdminDAO(ABC):
    
    @abstractmethod
    def get_all_usuarioAdmin(self) -> List[UsuarioAdmin]:
        pass
    
