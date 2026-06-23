from src.dominio.entidades.insumo_stock import InsumoStock


def test_creacion_insumo():

    insumo = InsumoStock(
        id_insumo=1,
        nombre="Balanceado",
        tipo="alimento",
        cantidad_actual=100,
        unidad_medida="kg",
        umbral_minimo=20
    )

    assert insumo.nombre == "Balanceado"
    assert insumo.cantidad_actual == 100