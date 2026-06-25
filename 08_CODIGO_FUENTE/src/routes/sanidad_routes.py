from fastapi import APIRouter
from src.services.sanidad_service import SanidadService

router = APIRouter()
service = SanidadService()


@router.post("/animales/{animal_id}/sanidad")
def crear_evento(animal_id: int, data: dict):
    return service.crear_evento(animal_id, data)


@router.get("/animales/{animal_id}/sanidad")
def listar_eventos(animal_id: int):
    return service.listar_eventos(animal_id)


@router.delete("/sanidad/{evento_id}")
def eliminar_evento(evento_id: int):
    return service.eliminar_evento(evento_id)