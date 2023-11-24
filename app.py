from flask import Flask, render_template, session
from db.db import Session
from core.config import settings
from flask_sqlalchemy import SQLAlchemy

# from api.controllers import bp_api
# from api.funcionalidades import bp_api_2
# from api.audits.audits import api_audits
# from api.funcionality.funcionality import api_funcionality
from api.perfiles.perfiles import api_perfiles

app = Flask(__name__)
app.config["SECRET_KEY"] = "Th1s1ss3cr3t"

# BD
app.config["SQLALCHEMY_DATABASE_URI"] = settings.DATABASE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
session_bd = Session()

# app.register_blueprint(api_audits)
# app.register_blueprint(api_funcionality)
app.register_blueprint(api_perfiles)

@app.route("/", methods=["GET"])
def index():
    return {"respuesta": "Bienvenido a la API"}


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8005)
