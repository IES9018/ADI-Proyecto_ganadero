from src.aplicacion.casos_de_uso.gestionar_animal import GestionarAnimal

def test_crear_animal():

    service = GestionarAnimal()

    animal = service.crear_animal(
        "BOV002",
        "Bovino",
        "Angus",
        2,
        "sano"
    )

    assert animal.codigo_identificacion == "BOV002"