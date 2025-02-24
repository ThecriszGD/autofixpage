from app import db  # Importa db desde app/__init__.py

class Reparacion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente = db.Column(db.String(100), nullable=False)
    vehiculo = db.Column(db.String(100), nullable=False)
    servicio = db.Column(db.String(100), nullable=False)
    estado = db.Column(db.String(50), default="Pendiente")