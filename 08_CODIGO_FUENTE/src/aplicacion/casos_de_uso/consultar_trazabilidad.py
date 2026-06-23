class ConsultarTrazabilidad:

    def ejecutar(self, repo_eventos, id_animal):

        eventos = repo_eventos.obtener_por_animal(id_animal)

        return {
            "id_animal": id_animal,
            "historial": eventos
        }