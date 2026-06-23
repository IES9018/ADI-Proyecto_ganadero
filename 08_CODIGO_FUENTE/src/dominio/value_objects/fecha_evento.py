from dataclasses import dataclass
from datetime import date

@dataclass(frozen=True)
class FechaEvento:
    valor: date

    def es_futura(self) -> bool:
        return self.valor > date.today()