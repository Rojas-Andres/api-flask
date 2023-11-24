from db.db import session
from sqlalchemy import select
from db.models import Perfiles
from sqlalchemy.orm import Session

def generic_post(data):
    try:
        session.add(data)
        session.commit()
        session.refresh(data)
    except:
        session.rollback()
        raise Exception("Error al crear el registro")
    return data

def get_perfiles():
    query = session.query(
        Perfiles.id_perfil, 
        Perfiles.nombre_perfil, 
        Perfiles.fecha_creacion,
    ).all()
    data_perfiles = []
    for i in query:
        data = dict(i)
        data["id_perfil"] = int(data["id_perfil"]) 
        data_perfiles.append(data)
    return data_perfiles


def validate_perfil(id_funcionalidad: int):
    id_perfil = (
        session.query(Perfiles).filter(Perfiles.id_perfil == id_perfil).first()
    )
    return id_perfil

def create_perfil(data):
    perfil = Perfiles(**data)
    perfil_db = generic_post(perfil)
    return perfil_db