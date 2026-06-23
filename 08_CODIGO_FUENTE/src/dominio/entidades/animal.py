from dataclasses import dataclass
from datetime import date
from typing import List, Optional

from .evento_sanitario import EventoSanitario


@dataclass
class Animal:
    id_animal: int
    codigo_identificacion: str
    especie: str
    raza: str
    edad_aproximada: int
    estado_sanitario: str
    fecha_registro: date
    eventos: List[EventoSanitario]

    def agregar_evento(self, evento: EventoSanitario) -> None:
        if self.eventos is None:
            self.eventos = []
        self.eventos.append(evento)

    def actualizar_estado_sanitario(self, nuevo_estado: str) -> None:
        self.estado_sanitario = nuevo_estado