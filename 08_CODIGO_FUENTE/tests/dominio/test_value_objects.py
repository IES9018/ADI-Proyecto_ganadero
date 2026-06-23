from src.dominio.value_objects.estado_sanitario import EstadoSanitario


def test_estado_sanitario():

    estado = EstadoSanitario("sano")

    assert estado.valor == "sano"