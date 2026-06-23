from src.aplicacion.casos_de_uso.gestionar_animal import GestionarAnimal


def test_crear_animal():

    servicio = GestionarAnimal()

    animal = servicio.crear_animal(
        "BOV001",
        "Bovino",
        "Angus",
        3,
        "sano"
    )

    assert animal.codigo_identificacion == "BOV001"