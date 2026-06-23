from enum import Enum

class EstadoSanitario(Enum):
    SANO = "sano"
    EN_TRATAMIENTO = "en_tratamiento"
    EN_OBSERVACION = "en_observacion"
    CRITICO = "critico"