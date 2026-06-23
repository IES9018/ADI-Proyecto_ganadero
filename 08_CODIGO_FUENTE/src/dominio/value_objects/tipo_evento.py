from enum import Enum

class TipoEvento(Enum):
    VACUNACION = "vacunacion"
    TRATAMIENTO = "tratamiento"
    MOVIMIENTO = "movimiento"
    CONTROL = "control"