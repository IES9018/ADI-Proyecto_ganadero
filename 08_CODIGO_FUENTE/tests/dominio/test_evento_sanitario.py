from datetime import date
from src.dominio.entidades.evento_sanitario import EventoSanitario


def test_creacion_evento():

    evento = EventoSanitario(
        id_evento=1,
        id_animal=1,
        tipo_evento="vacunacion",
        fecha=date.today(),
        descripcion="Vacuna antiaftosa"
    )

    assert evento.id_animal == 1
    assert evento.tipo_evento == "vacunacion"