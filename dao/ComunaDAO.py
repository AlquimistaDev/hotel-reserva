# Importamos ABC y abstractmethod del módulo abc. ABC es la clase base para todas las clases abstractas,
# y abstractmethod es un decorador que se usa para definir métodos abstractos.
from abc import ABC, abstractmethod

# Importamos List del módulo typing para especificar que el método get_all_comunas
# devolverá una lista de objetos de tipo Comuna.
from typing import List

# Importamos la clase Comuna desde el módulo ComunaDTO. Esto asume que ComunaDTO es un módulo
# que contiene la definición de la clase Comuna.
from dto.ComunaDTO import Comuna

# Definimos la clase ComunaDao que hereda de ABC, lo que la convierte en una clase abstracta.
class ComunaDao(ABC):
    
    # Usamos el decorador @abstractmethod para indicar que get_all_comunas es un método abstracto.
    # Esto significa que cualquier subclase de ComunaDao debe proporcionar una implementación de este método.
    @abstractmethod
    def get_all_comunas(self) -> List[Comuna]:
        # La palabra clave 'pass' se usa aquí porque no proporcionamos una implementación en la clase abstracta.
        # Las subclases deben sobrescribir este método con una implementación concreta.
        pass