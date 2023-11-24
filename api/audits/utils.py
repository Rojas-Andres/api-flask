from db.db import session
from sqlalchemy import select
from db.models import Auditoria
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


def get_auditoria():
    query = session.query(
        Auditoria.id_auditoria,
        Auditoria.id_usuario,
        Auditoria.modulo,
        Auditoria.link,
        Auditoria.icono,
        Auditoria.fecha_creacion,
    ).all()
    data_audits = []
    for i in query:
        data = dict(i)
        data["id_auditoria"] = int(data["id_auditoria"])
        data["id_usuario"] = int(data["id_usuario"])
        data_audits.append(data)
    return data_audits


def create_auditoria(data):
    auditoria = Auditoria(**data)
    auditoria_db = generic_post(auditoria)
    return auditoria_db


def validate_auditoria(id_auditoria: int):
    auditoria = (
        session.query(Auditoria).filter(Auditoria.id_auditoria == id_auditoria).first()
    )
    return auditoria


def format_auditoria(audit):
    aud = audit.__dict__
    aud.pop("_sa_instance_state")
    aud["id_auditoria"] = int(aud["id_auditoria"])
    aud["id_usuario"] = int(aud["id_usuario"])
    return aud
