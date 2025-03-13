from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    
    # Dados do ACS
    nome_completo = db.Column(db.String(70), nullable=False)
    cns = db.Column(db.String(15), nullable=False)
    cbo = db.Column(db.String(6), nullable=False)
    cnes = db.Column(db.String(7), nullable=False)
    ine = db.Column(db.String(10), nullable=False)
    microarea = db.Column(db.String(2), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    
    # Dados de registro
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)
    atualizado_em = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>' 