from src.aplicacion.casos_de_uso.consultar_trazabilidad import ConsultarTrazabilidad


def test_consultar_trazabilidad():

    servicio = ConsultarTrazabilidad()

    historial = servicio.consultar(1)

    assert historial is not None