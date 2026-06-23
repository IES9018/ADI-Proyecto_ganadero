from dataclasses import dataclass

@dataclass(frozen=True)
class CodigoIdentificacion:
    valor: str

    def __post_init__(self):
        if not self.valor:
            raise ValueError("El código de identificación no puede estar vacío")

        if len(self.valor) < 3:
            raise ValueError("El código de identificación es demasiado corto")