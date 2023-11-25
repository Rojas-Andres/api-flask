from flask import Blueprint, jsonify, request

from api.perfiles.utils import get_perfiles, validate_perfil


from api.perfiles.utils import (
    create_perfil,
    get_perfiles,
    get_perfiles,
    validate_perfil,
)

from api.perfiles.validate_perfiles import PerfilesCreate

api_perfiles = Blueprint("Api Perfiles", __name__, url_prefix="/api/perfiles")


@api_perfiles.route("/", methods=["GET"])
def get_perfil():
    """
    Get all perfiles
    """
    perfiles = get_perfiles()
    return {
        "perfiles": perfiles,
    }


@api_perfiles.route("/", methods=["POST"])
def create_perfil():
    """
    Create perfiles
    """
    try:
        perfiles_validate = PerfilesCreate(**request.json)
    except Exception as e:
        return jsonify({"errors": e.errors()}), 400
    perfiles = validate_perfil(perfiles_validate.id_perfil)
    if perfiles:
        return jsonify({"errors": "Ya existe un registro con este id"}), 400
    perfiles_db = create_perfil(perfiles_validate.dict(exclude_unset=True))
    return {
        "auditoria_id": int(perfiles_db.id_perfil),
        "message": "Auditoria creada exitosamente",
    }
