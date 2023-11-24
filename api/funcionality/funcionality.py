from flask import Blueprint, jsonify, request

from api.funcionality.validate_funcionality import FuncionalidadCreate
from api.funcionality.utils import create_funcionalidad, get_funcionalitys, validate_funcionalidad, format_funcionalidad

api_funcionality = Blueprint("Api Controller", __name__, url_prefix="/api/funcionality")


@api_funcionality.route("/", methods=["GET"])
def get_funcionality():
    """
    Get all funcionality
    """
    funcionality = get_funcionalitys()
    return {
        "funcionality": funcionality,
    }


@api_funcionality.route("/", methods=["POST"])
def create_funcionality():
    """
    Create funcionality
    """
    try:
        funcionality_validate = FuncionalidadCreate(**request.json)
    except Exception as e:
        return jsonify({"errors": e.errors()}), 400
    funcionalidad = validate_funcionalidad(funcionality_validate.id_funcionalidad)
    if funcionalidad:
        return jsonify({"errors": "Ya existe un registro con este id"}), 400
    funcionalidad_db = create_funcionalidad(funcionality_validate.dict(exclude_unset=True))
    return {
        "id_funcionalidad": int(funcionalidad_db.id_funcionalidad),
        "message": "Auditoria creada exitosamente",
    }

@api_funcionality.route("/<int:id_funcionalidad>", methods=["GET"])
def get_only_funcionality(id_funcionalidad: str):
    """
    Create audits
    """
    funcionalidad = validate_funcionalidad(id_funcionalidad)
    if not funcionalidad:
        return jsonify({"errors": "No existe un registro con este id"}), 400
    return format_funcionalidad(funcionalidad)

