from datetime import date
from dominio.entidades.animal import Animal


class GestionarAnimal:

    def crear_animal(self, repo, codigo, especie, raza, edad, estado):
        animal = Animal(
            id_animal=None,
            codigo_identificacion=codigo,
            especie=especie,
            raza=raza,
            edad_aproximada=edad,
            estado_sanitario=estado,
            fecha_registro=date.today()
        )

        return repo.guardar(animal)

    def listar_animales(self, repo):
        return repo.listar()

    def obtener_animal(self, repo, id_animal):
        return repo.obtener_por_id(id_animal)