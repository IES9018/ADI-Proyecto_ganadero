from infraestructura.persistencia.database import SessionLocal
from infraestructura.persistencia.models.animal_model import AnimalModel


class AnimalRepository:

    def obtener_todos(self):
        session = SessionLocal()

        try:
            return session.query(AnimalModel).all()

        finally:
            session.close()

    def obtener_por_id(self, id_animal):
        session = SessionLocal()

        try:
            return (
                session.query(AnimalModel)
                .filter(AnimalModel.id_animal == id_animal)
                .first()
            )

        finally:
            session.close()

    def guardar(self, animal):
        session = SessionLocal()

        try:
            session.add(animal)
            session.commit()

        finally:
            session.close()