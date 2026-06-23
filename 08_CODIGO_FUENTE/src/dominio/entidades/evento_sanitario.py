from dataclasses import dataclass
from datetime import date


@dataclass
class EventoSanitario:
    id_evento: int
    tipo_evento: str
    fecha: date
    descripcion: str
    id_animal: int