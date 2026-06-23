from infraestructura.persistencia.database import SessionLocal
from infraestructura.persistencia.models.evento_sanitario_model import EventoSanitarioModel


class EventoSanitarioRepository:

    def obtener_por_animal(self, id_animal):
        session = SessionLocal()

        try:
            return (
                session.query(EventoSanitarioModel)
                .filter(
                    EventoSanitarioModel.id_animal == id_animal
                )
                .all()
            )

        finally:
            session.close()

    def guardar(self, evento):
        session = SessionLocal()

        try:
            session.add(evento)
            session.commit()

        finally:
            session.close()