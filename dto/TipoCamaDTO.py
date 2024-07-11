from dataclasses import dataclass

@dataclass
class TipoCama:

    idTipoCama:int 
    tipoCama: str

    def __str__(self) -> str:
        return f"TipoCama(idtipoCama={self.idTipoCama}, tipoCama={self.tipoCama})"
    
    
        