from src.aplicacion.casos_de_uso.gestionar_stock import GestionarStock


def test_actualizar_stock():

    servicio = GestionarStock()

    resultado = servicio.actualizar_stock(
        1,
        50
    )

    assert resultado is True