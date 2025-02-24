from flask import render_template, request, redirect, url_for, Blueprint
from app import db
from models import Reparacion

main = Blueprint('main', __name__)

@main.route("/")
def index():
    reparaciones = Reparacion.query.all()
    return render_template("index.html", reparaciones=reparaciones)

@main.route("/agregar", methods=["GET", "POST"])
def agregar():
    if request.method == "POST":
        nueva_reparacion = Reparacion(
            cliente=request.form.get("cliente"),
            vehiculo=request.form.get("vehiculo"),
            servicio=request.form.get("servicio")
        )
        db.session.add(nueva_reparacion)
        db.session.commit()
        return redirect(url_for("main.index"))  # Correcto
    return render_template("agregar.html")  

@main.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    reparacion = Reparacion.query.get_or_404(id)
    if request.method == "POST":
        reparacion.estado = request.form.get("estado")
        db.session.commit()
        return redirect(url_for("main.index"))  # Correcto
    return render_template("editar.html", reparacion=reparacion)

@main.route("/eliminar/<int:id>")
def eliminar(id):
    reparacion = Reparacion.query.get_or_404(id)
    db.session.delete(reparacion)
    db.session.commit()
    return redirect(url_for("main.index"))  # Correcto

# El código fuera del blueprint fue eliminado para evitar conflictos

