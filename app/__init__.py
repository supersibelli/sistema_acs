from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap5
from config import Config
import os

db = SQLAlchemy()
login_manager = LoginManager()
bootstrap = Bootstrap5()
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(id):
    from app.models import User
    return User.query.get(int(id))

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Crear carpeta instance si no existe
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Inicializar extensiones
    db.init_app(app)
    login_manager.init_app(app)
    bootstrap.init_app(app)

    # Registrar blueprints
    from app.routes import auth, main, cadastro
    app.register_blueprint(auth.bp)
    app.register_blueprint(main.bp)
    app.register_blueprint(cadastro.bp)

    # Crear todas las tablas de la base de datos
    with app.app_context():
        # Importar User aquí dentro del contexto
        from app.models import User
        
        db.create_all()
        
        # Crear usuario admin si no existe
        if not User.query.filter_by(username='admin').first():
            admin = User(
                username='admin',
                nome_completo='Administrador do Sistema',
                cns='000000000000000',
                cbo='000000',
                cnes='0000000',
                ine='0000000000',
                microarea='00',
                is_admin=True
            )
            admin.set_password('admin')
            db.session.add(admin)
            db.session.commit()

    return app 