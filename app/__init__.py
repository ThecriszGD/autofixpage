from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # Instancia de SQLAlchemy se crea aquí, pero NO se inicializa

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'tu_clave_secreta'  # ¡CAMBIA ESTO POR UNA CLAVE REAL!
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///autofix.db'

    db.init_app(app)  # Se inicializa la base de datos

    # Importante: se importan blueprints DESPUÉS de la inicialización
    from .routes import main  # Importa el blueprint 'main' desde routes.py
    app.register_blueprint(main)  # Registra el blueprint

    with app.app_context():
        db.create_all()

    return app

app = create_app()  # Se crea la aplicación