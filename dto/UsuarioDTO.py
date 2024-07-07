from dataclasses import dataclass

@dataclass
class Usuario:
    ID_USUARIO: int
    USER_NOMBRE: str
    USER_APELLIDO: str
    USER_EMAIL: str
    CONTRASENA: str
    ES_ADMINISTRADOR: bool

    def __str__(self) -> str:
        return f"Usuario(ID_USUARIO={self.ID_USUARIO}, USER_NOMBRE={self.USER_NOMBRE}, USER_APELLIDO={self.USER_APELLIDO}, USER_EMAIL={self.USER_EMAIL}, CONTRASENA={self.CONTRASENA}, ES_ADMINISTRADOR={self.ES_ADMINISTRADOR})"