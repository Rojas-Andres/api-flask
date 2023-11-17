from sqlalchemy import (
    Column,
    String,
    Date,
    Integer,
)
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Auditoria(Base):
    __tablename__ = "tb_auditoria"

    id_auditoria = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, nullable=False)
    modulo = Column(String(100))
    link = Column(String(100))
    icono = Column(String(100))
    fecha_creacion = Column(Date)
