from dataclasses import dataclass
from datetime import date

@dataclass
class ReservaDTO:
    id_reserva: int
    fec_reserva: date
    fec_llegada: date
    fec_salida: date
    cant_pasajeros: int
    monto_total: float
    id_estado_reserva: int
    penalizacion: float
    id_habitacion: int