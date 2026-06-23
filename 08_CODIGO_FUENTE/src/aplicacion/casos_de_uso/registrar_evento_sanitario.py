from datetime import date


class RegistrarEventoSanitario:

    def ejecutar(self, repo_eventos, repo_animal, id_animal, tipo, descripcion):

        animal = repo_animal.obtener_por_id(id_animal)

        if not animal:
            raise Exception("Animal no existe")

        evento = {
            "id_animal": id_animal,
            "tipo_evento": tipo,
            "fecha": date.today(),
            "descripcion": descripcion
        }

        return repo_eventos.guardar(evento)