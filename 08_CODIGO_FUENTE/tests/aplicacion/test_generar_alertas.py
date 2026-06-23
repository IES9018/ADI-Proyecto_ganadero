from src.aplicacion.casos_de_uso.generar_alertas import GenerarAlertas


def test_generar_alerta():

    servicio = GenerarAlertas()

    alertas = servicio.generar()

    assert isinstance(alertas, list)