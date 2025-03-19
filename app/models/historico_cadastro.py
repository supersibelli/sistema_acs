from app import db
from datetime import datetime

class HistoricoCadastro(db.Model):
    __tablename__ = 'historico_cadastro'
    
    id = db.Column(db.Integer, primary_key=True)
    cadastro_id = db.Column(db.Integer, db.ForeignKey('cadastro_individual.id'), nullable=False)
    data_modificacao = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    modificado_por = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    
    # Relación con el cadastro
    cadastro = db.relationship('CadastroIndividual', backref=db.backref('historico', lazy=True)) 