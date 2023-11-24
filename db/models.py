from sqlalchemy import (
    Column,
    String,
    Date,
    Integer,
)
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Auditoria(Base):
    __tablename__ = "tb_seg_auditoria"

    id_auditoria = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, nullable=False)
    modulo = Column(String(100))
    link = Column(String(100))
    icono = Column(String(100))
    fecha_creacion = Column(Date)


class Funcionalidad(Base):
    __tablename__ = "tb_seg_funcionalidad"

    id_funcionalidad = Column(Integer, primary_key=True)
    nombre_funcionalidad = Column(String(100))
    link = Column(String(100))
    icono = Column(String(100))
    fecha_creacion = Column(Date)


class Perfiles(Base):
    __tablename__ = "tb_seg_perfiles"

    id_perfil = Column(Integer, primary_key=True)
    nombre_perfil = Column(String(100)) 
    fecha_creacion = Column(Date)

