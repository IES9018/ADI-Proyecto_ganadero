from src.aplicacion.casos_de_uso.registrar_evento import RegistrarEvento


def test_registrar_evento():

    servicio = RegistrarEvento()

    evento = servicio.registrar(
        1,
        "vacunacion",
        "Vacuna antiaftosa"
    )

    assert evento.id_animal == 1