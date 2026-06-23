from infraestructura.persistencia.database import SessionLocal
from infraestructura.persistencia.models.insumo_stock_model import InsumoStockModel


class InsumoStockRepository:

    def obtener_todos(self):
        session = SessionLocal()

        try:
            return session.query(InsumoStockModel).all()

        finally:
            session.close()

    def guardar(self, insumo):
        session = SessionLocal()

        try:
            session.add(insumo)
            session.commit()

        finally:
            session.close()