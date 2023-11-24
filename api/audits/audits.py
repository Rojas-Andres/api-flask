from flask import Blueprint, jsonify, request
from api.audits.utils import (
    get_auditoria,
    create_auditoria,
    validate_auditoria,
    format_auditoria,
)
from api.audits.validate_audits import AuditsCreate

api_audits = Blueprint("Api Controller", __name__, url_prefix="/api/auditorias")


@api_audits.route("/", methods=["GET"])
def get_audits():
    """
    Get all audits
    """
    audits = get_auditoria()
    return {
        "auditorias": audits,
    }


@api_audits.route("/", methods=["POST"])
def create_audits():
    """
    Create audits
    """
    try:
        audit_validate = AuditsCreate(**request.json)
    except Exception as e:
        return jsonify({"errors": e.errors()}), 400
    audit = validate_auditoria(audit_validate.id_auditoria)
    if audit:
        return jsonify({"errors": "Ya existe un registro con este id"}), 400
    auditoria_db = create_auditoria(audit_validate.dict(exclude_unset=True))
    return {
        "auditoria_id": int(auditoria_db.id_auditoria),
        "message": "Auditoria creada exitosamente",
    }


@api_audits.route("/<int:audit_id>", methods=["GET"])
def get_only_audit(audit_id: str):
    """
    Create audits
    """
    audit = validate_auditoria(audit_id)
    if not audit:
        return jsonify({"errors": "No existe un registro con este id"}), 400
    return format_auditoria(audit)
