from dataclasses import dataclass
from datetime import date

@dataclass
class PasajeroDTO:
    ID_PASAJERO: int
    NOMBRE_PASAJERO: str
    APELLIDO_PASAJERO: str
    FEC_NAC_PASAJERO: date
    USER_EMAIL_PASAJERO: str
    DIRE_PASAJERO: str
    ID_REGION: int
    ID_PROVINCIA: int
    ID_COMUNA: int

    def __str__(self) -> str:
        return f"Pasajero(ID_PASAJERO={self.ID_PASAJERO}, NOMBRE_PASAJERO={self.NOMBRE_PASAJERO}, APELLIDO_PASAJERO={self.APELLIDO_PASAJERO}, FEC_NAC_PASAJERO={self.FEC_NAC_PASAJERO}, USER_EMAIL_PASAJERO={self.USER_EMAIL_PASAJERO}, DIRE_PASAJERO={self.DIRE_PASAJERO}, ID_REGION={self.ID_REGION}, ID_PROVINCIA={self.ID_PROVINCIA}, ID_COMUNA={self.ID_COMUNA})"