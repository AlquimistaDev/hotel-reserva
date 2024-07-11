from dataclasses import dataclass

@dataclass
class Orientacion:

    idOrientacion : int
    descOrientacion : str


    def __str__(self) -> str:
        return f"Orientacion(idOrientacion={self.idOrientacion}, descOrientacion={self.descOrientacion})"