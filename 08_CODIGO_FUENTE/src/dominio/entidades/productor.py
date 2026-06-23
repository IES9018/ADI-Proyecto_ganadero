from dataclasses import dataclass


@dataclass
class Productor:
    id_productor: int
    nombre: str
    contacto: str
    ubicacion: str