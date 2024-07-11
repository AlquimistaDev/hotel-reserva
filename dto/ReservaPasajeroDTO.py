from dataclasses import dataclass

@dataclass
class ReservaPasajero:

    idReservaPasajero: int
    idReserva:  int
    idPasajero: int
    costoPasajero: float


    def __str__(self) -> str:
        return f"ReservaPasajero(idReservaPasajero={self.idReservaPasajero}, idReserva={self.idReserva}, idPasajero={self.idPasajero}, costoPasajero={self.costoPasajero})"
    
    