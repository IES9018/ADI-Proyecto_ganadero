from infraestructura.persistencia.database import SessionLocal
from infraestructura.persistencia.models.productor_model import ProductorModel


class ProductorRepository:

    def obtener_todos(self):
        session = SessionLocal()

        try:
            return session.query(ProductorModel).all()

        finally:
            session.close()

    def guardar(self, productor):
        session = SessionLocal()

        try:
            session.add(productor)
            session.commit()

        finally:
            session.close()