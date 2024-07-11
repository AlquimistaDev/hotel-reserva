from dataclasses import dataclass

@dataclass
# Definimos la clase Comuna que representa una entidad Comuna con sus atributos.
class Comuna:
    id_comuna: int
    id_Pro: int
    nom_Com: str
    des_Com: str

    def __str__(self) -> str:
        return f"Comuna(id_comuna={self.id_comuna}, id_Pro={self.id_Pro}, nom_Com='{self.nom_Com}', des_Com='{self.des_Com}')"