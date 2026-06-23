from src.dominio.entidades.animal import Animal

class RepositorioAnimal:

    _instance = None
    _data = []

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def guardar(self, animal: Animal):
        self._data.append(animal)
        return animal

    def listar(self):
        return self._data