from app import db
from datetime import datetime

class Citizen(db.Model):
    __tablename__ = 'citizens'
    
    id = db.Column(db.Integer, primary_key=True)
    # Datos básicos obligatorios
    nome_completo = db.Column(db.String(100), nullable=False)
    nome_social = db.Column(db.String(100))
    data_nascimento = db.Column(db.Date, nullable=False)
    sexo = db.Column(db.String(20), nullable=False)
    raca_cor = db.Column(db.String(20), nullable=False)
    etnia = db.Column(db.String(50))
    numero_nis = db.Column(db.String(11))
    nome_mae = db.Column(db.String(100), nullable=False)
    nome_pai = db.Column(db.String(100), nullable=False)
    nacionalidade = db.Column(db.String(50), nullable=False)
    
    # Datos de contacto
    telefone = db.Column(db.String(15))
    email = db.Column(db.String(100))
    
    # Datos de registro
    created_by_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Datos profesionales del ACS
    cns_profissional = db.Column(db.String(15), nullable=False)
    cbo = db.Column(db.String(6), nullable=False)
    cnes = db.Column(db.String(7), nullable=False)
    ine = db.Column(db.String(10), nullable=False)
    microarea = db.Column(db.String(10), nullable=False)
    
    # Documentos del ciudadano
    cns_cidadao = db.Column(db.String(15))
    cpf_cidadao = db.Column(db.String(11))
    
    # Relaciones
    created_by = db.relationship('User', backref='citizens')
    health_conditions = db.relationship('HealthCondition', backref='citizen', lazy=True)
    social_info = db.relationship('SocialInformation', backref='citizen', uselist=False, lazy=True)
    homeless_info = db.relationship('HomelessInformation', backref='citizen', uselist=False, lazy=True)

    def __repr__(self):
        return f'<Citizen {self.nome_completo}>' 