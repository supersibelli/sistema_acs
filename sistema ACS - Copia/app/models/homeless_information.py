from app import db
from datetime import datetime

class HomelessInformation(db.Model):
    __tablename__ = 'informacoes_situacao_rua'
    
    id = db.Column(db.Integer, primary_key=True)
    cidadao_id = db.Column(db.Integer, db.ForeignKey('citizens.id'), nullable=False)
    
    # Tempo em situação de rua
    tempo_rua = db.Column(db.String(20))
    
    # Acompanhamento institucional
    acompanhamento_instituicao = db.Column(db.Boolean, default=False)
    instituicoes = db.Column(db.String(200))
    
    # Benefícios
    recebe_beneficio = db.Column(db.Boolean, default=False)
    beneficios = db.Column(db.String(200))
    
    # Referência familiar
    referencia_familiar = db.Column(db.Boolean, default=False)
    grau_parentesco = db.Column(db.String(50))
    visita_familiar = db.Column(db.Boolean, default=False)
    frequencia_visita = db.Column(db.String(20))
    
    # Higiene pessoal
    acesso_higiene = db.Column(db.Boolean, default=False)
    tipos_higiene = db.Column(db.String(200))
    
    # Alimentação
    alimentacao_dia = db.Column(db.Integer)
    origem_alimentacao = db.Column(db.String(200))
    
    # Dados de registro
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<InformacaoSituacaoRua {self.id} - Cidadão {self.cidadao_id}>' 