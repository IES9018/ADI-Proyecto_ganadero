from datetime import date
from src.dominio.entidades.animal import Animal

def test_animal():
    animal = Animal(
        1,
        "BOV001",
        "Bovino",
        "Angus",
        3,
        "sano",
        date.today()
    )

    assert animal.codigo_identificacion == "BOV001"