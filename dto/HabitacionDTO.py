from dataclasses import dataclass

@dataclass
class HabitacionDTO:
    id_habitacion: int
    numero_habitacion: int
    capacidad: int
    id_tipo_cama: int
    id_orientacion: int
    id_estado_hab: int

    def __str__(self) -> str:
        return f"Habitacion(id_habitacion={self.id_habitacion}, numero_habitacion={self.numero_habitacion}, capacidad={self.capacidad}, id_tipo_cama={self.id_tipo_cama}, id_orientacion={self.id_orientacion}, id_estado_hab={self.id_estado_hab})"