from fastapi import APIRouter
from src.aplicacion.casos_de_uso.gestionar_animal import GestionarAnimal

router = APIRouter()
service = GestionarAnimal()

@router.get("/animales")
def listar_animales():
    return service.listar_animales()

@router.post("/animales")
def crear_animal():
    return service.crear_animal(
        codigo="BOV001",
        especie="Bovino",
        raza="Angus",
        edad=3,
        estado="sano"
    )