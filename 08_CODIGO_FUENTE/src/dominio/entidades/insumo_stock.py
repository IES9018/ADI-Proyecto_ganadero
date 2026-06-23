from dataclasses import dataclass


@dataclass
class InsumoStock:
    id_insumo: int
    nombre: str
    tipo: str
    cantidad_actual: float
    unidad_medida: str
    umbral_minimo: float

    def reducir_stock(self, cantidad: float) -> None:
        if self.cantidad_actual - cantidad < 0:
            raise ValueError("Stock insuficiente")
        self.cantidad_actual -= cantidad

    def aumentar_stock(self, cantidad: float) -> None:
        self.cantidad_actual += cantidad

    def necesita_reposicion(self) -> bool:
        return self.cantidad_actual < self.umbral_minimo