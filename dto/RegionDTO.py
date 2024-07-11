from dataclasses import dataclass

@dataclass
class Region:
    idRegion: int 
    nomRegion: str
    descRegion: str

    def __str__(self) -> str:
        return f"Region(idRegion={self.idRegion}, nomRegion={self.nomRegion}, descRegion={self.descRegion})"
        