from infraestructura.persistencia.database import SessionLocal
from infraestructura.persistencia.models.personal_campo_model import PersonalCampoModel


class PersonalCampoRepository:

    def obtener_todos(self):
        session = SessionLocal()

        try:
            return session.query(PersonalCampoModel).all()

        finally:
            session.close()

    def guardar(self, personal):
        session = SessionLocal()

        try:
            session.add(personal)
            session.commit()

        finally:
            session.close()