from dataclasses import dataclass

@dataclass
class Provincia:

    idProvincia: int
    idRegion:	int
    nomProvincia: str
    descProvincia: str

    def __str__(self) -> str:
        return f"Provincia(idProvincia={self.idProvincia}, idRegion={self.idRegion}, nomProvincia={self.nomProvincia}, descProvincia={self.descProvincia})"