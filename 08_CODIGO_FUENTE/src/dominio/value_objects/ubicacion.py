from dataclasses import dataclass

@dataclass(frozen=True)
class Ubicacion:
    descripcion: str

    def __post_init__(self):
        if not self.descripcion:
            raise ValueError("La ubicación no puede estar vacía")