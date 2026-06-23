from datetime import date
from src.dominio.entidades.animal import Animal


def test_creacion_animal():

    animal = Animal(
        id_animal=1,
        codigo_identificacion="BOV001",
        especie="Bovino",
        raza="Aberdeen Angus",
        edad_aproximada=3,
        estado_sanitario="sano",
        fecha_registro=date.today()
    )

    assert animal.codigo_identificacion == "BOV001"
    assert animal.especie == "Bovino"
    assert animal.estado_sanitario == "sano"