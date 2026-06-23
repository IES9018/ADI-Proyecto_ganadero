from dataclasses import dataclass

@dataclass(frozen=True)
class Cantidad:
    valor: float

    def __post_init__(self):
        if self.valor < 0:
            raise ValueError("La cantidad no puede ser negativa")

    def es_bajo_stock(self, umbral: float) -> bool:
        return self.valor < umbral