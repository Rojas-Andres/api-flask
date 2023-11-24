from db.db import session
from sqlalchemy import select
from db.models import Perfiles
from flask import Blueprint, jsonify, request 
from sqlalchemy.orm import Session

def generic_post(data):
    try:
        session.add(data)
        session.commit()
        session.refresh(data)
    except Exception as e:
       
        session.rollback()
        return jsonify({"errors": e.errors()}), 400
        # raise Exception("Error al crear el registro")
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

def create_perfil(data):
    perfil = Perfiles(**data)
    perfil_db = generic_post(perfil)
    return perfil_db

def validate_perfil(id_perfil: int):
    perfil = (
        session.query(Perfiles).filter(Perfiles.id_perfil == id_perfil).first()
    )
    return perfil

def format_perfil(perfil):
    perfil = perfil.__dict__
    perfil.pop("_sa_instance_state")
    perfil["id_perfil"] = int(perfil["id_perfil"]) 
    return perfil