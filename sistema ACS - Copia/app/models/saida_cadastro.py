from app import db
from datetime import datetime
from app.models.constants import *

class SaidaCadastro(db.Model):
    __tablename__ = 'saida_cadastro'
    
    id = db.Column(db.Integer, primary_key=True)
    cadastro_id = db.Column(db.Integer, db.ForeignKey('cadastros_individuais.id'), nullable=False)
    
    # Motivo da saída
    motivo_saida = db.Column(db.Integer, nullable=False)  # MOTIVO_SAIDA_CHOICES
    
    # Dados de óbito (se aplicável)
    data_obito = db.Column(db.Date)  # Requerido se motivo_saida = 2 (Óbito)
    numero_do = db.Column(db.String(9))  # Número da Declaração de Óbito
    
    # Dados de registro
    criado_em = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    atualizado_em = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    registrado_por_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    # Relacionamentos
    registrado_por = db.relationship('User', backref='saidas_registradas')
    cadastro = db.relationship('CadastroIndividual', backref='saida')

    def __repr__(self):
        return f'<SaidaCadastro {self.id} - Cadastro {self.cadastro_id}>'

    def to_dict(self):
        return {
            'id': self.id,
            'cadastro_id': self.cadastro_id,
            'motivo_saida': self.motivo_saida,
            'data_obito': self.data_obito.isoformat() if self.data_obito else None,
            'numero_do': self.numero_do,
            'criado_em': self.criado_em.isoformat(),
            'atualizado_em': self.atualizado_em.isoformat(),
            'registrado_por_id': self.registrado_por_id
        }

    @property
    def motivo_saida_texto(self):
        return dict(MOTIVO_SAIDA_CHOICES).get(self.motivo_saida, '') 