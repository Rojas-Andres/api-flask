from db.db import session
from sqlalchemy import select
from db.models import Funcionalidad
from sqlalchemy.orm import Session
from flask import Blueprint, jsonify, request


def generic_post(data):
    try:
        session.add(data)
        session.commit()
        session.refresh(data)
    except:
        session.rollback()
        raise Exception("Error al crear el registro")
    return data


def generic_put(id_funcionalidad, data):
    try:
        query = (
            data.update()
            .where(data.id_funcionalidad == id_funcionalidad)
            .values(data)
            .returning(
                data.nombre_funcionalidad,
                data.link,
                data.icono,
                data.fecha_creacion,
            )
        )
        result = session.execute(query)
        session.commit()
        session.close()
    except Exception as e:
        return jsonify({"errors": e.errors()}), 400


def get_funcionalitys():
    query = session.query(
        Funcionalidad.id_funcionalidad,
        Funcionalidad.nombre_funcionalidad,
        Funcionalidad.link,
        Funcionalidad.icono,
        Funcionalidad.fecha_creacion,
    ).all()
    data_funcinonaltys = []
    for i in query:
        data = dict(i)
        data["id_funcionalidad"] = int(data["id_funcionalidad"])
        data_funcinonaltys.append(data)
    return data_funcinonaltys


def update_generic(generic_model, id, data):
    try:
        session.query(generic_model).filter(generic_model.id == id).update(
            data, synchronize_session=True
        )
        session.commit()
    except Exception as e:
        session.rollback()
        raise Exception("Error al actualizar el registro")


def update_funcionalidad(id_funcionality, data):
    try:
        session.query(Funcionalidad).filter(
            Funcionalidad.id_funcionalidad == id_funcionality
        ).update(data)
        session.commit()
    except Exception as e:
        session.rollback()
        raise Exception("Error al actualizar el registro")
    funcionality = validate_funcionalidad(id_funcionality)
    return format_funcionalidad(funcionality)


def create_funcionalidad(data):
    funcionalidad = Funcionalidad(**data)
    funcionalidad_db = generic_post(funcionalidad)
    return funcionalidad_db


def validate_funcionalidad(id_funcionalidad: int):
    funcionalidad = (
        session.query(Funcionalidad)
        .filter(Funcionalidad.id_funcionalidad == id_funcionalidad)
        .first()
    )
    return funcionalidad


def format_funcionalidad(funcionalidad):
    funcionalidad = funcionalidad.__dict__
    funcionalidad.pop("_sa_instance_state")
    funcionalidad["id_funcionalidad"] = int(funcionalidad["id_funcionalidad"])
    return funcionalidad
