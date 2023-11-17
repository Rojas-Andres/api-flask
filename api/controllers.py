from flask import Blueprint, jsonify, request, abort
from flask_restplus import Api, Resource, fields
from api.functions import *
from api.functions import get_auditoria

bp_api = Blueprint("Api", __name__, url_prefix="/api")

api = Api(bp_api, version="1.0", title="Api", description="End Points")
ns_model = api.namespace("Methods", description="Metodos")
ns_model_auditorias = api.namespace("auditorias", description="Auditorias")


class VerificarDatos:
    CrearTbAuditoria = api.model(
        "tb_auditoria",
        {
            "id_auditoria": fields.Integer(
                description="Id auditoria",
                required=True,
            ),
            "id_usuario": fields.Integer(
                description="Id usuario",
                required=True,
            ),
            "modulo": fields.String(
                description="Modulo",
            ),
            "link": fields.String(
                description="link",
            ),
            "icono": fields.String(
                description="icono",
            ),
        },
    )


@ns_model_auditorias.route("/")
@api.doc(description="Auditoria")
class Auditoria(Resource):
    def get(self):
        auditorias = get_auditoria()
        return jsonify(auditorias)

    @ns_model_auditorias.expect(VerificarDatos.CrearTbAuditoria, validate=True)
    def post(self):
        try:
            auditoria_db = create_auditoria(request.json)
        except Exception as e:
            abort(400, str(e))
        return jsonify(
            {
                "auditoria_id": auditoria_db.id_auditoria,
                "message": "Auditoria creada exitosamente",
            }
        )
