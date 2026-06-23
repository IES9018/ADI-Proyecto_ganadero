from src.dominio.entidades.animal import Animal
from src.infraestructura.repositorios.repositorio_animal import RepositorioAnimal
from datetime import date

repo = RepositorioAnimal()

class GestionarAnimal:

    def crear_animal(self, codigo, especie, raza, edad, estado):

        animal = Animal(
            id_animal=len(repo.listar()) + 1,
            codigo_identificacion=codigo,
            especie=especie,
            raza=raza,
            edad_aproximada=edad,
            estado_sanitario=estado,
            fecha_registro=date.today()
        )

        return repo.guardar(animal)

    def listar_animales(self):
        return repo.listar()