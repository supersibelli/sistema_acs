from app import db
from datetime import datetime
from app.models.constants import *

class SituacaoRua(db.Model):
    __tablename__ = 'situacao_rua'
    
    id = db.Column(db.Integer, primary_key=True)
    cadastro_id = db.Column(db.Integer, db.ForeignKey('cadastros_individuais.id'), nullable=False)
    
    # Status principal
    status_situacao_rua = db.Column(db.Boolean, nullable=False)
    
    # Tempo em situação de rua
    tempo_rua = db.Column(db.Integer, nullable=False)  # TEMPO_RUA_CHOICES
    
    # Benefícios e acompanhamento
    status_recebe_beneficio = db.Column(db.Boolean, nullable=False)
    beneficios = db.Column(db.String(200))  # Lista de benefícios separados por vírgula
    
    status_acompanhado_instituicao = db.Column(db.Boolean, nullable=False)
    instituicoes = db.Column(db.String(200))  # Lista de instituições separadas por vírgula
    
    # Referência familiar
    status_possui_referencia_familiar = db.Column(db.Boolean, nullable=False)
    grau_parentesco_referencia = db.Column(db.String(50))  # Requerido se possui referência
    
    status_visita_familiar = db.Column(db.Boolean, nullable=False)
    frequencia_visita = db.Column(db.String(20))  # Requerido se visita família
    
    # Alimentação
    quantidade_alimentacoes_dia = db.Column(db.Integer, nullable=False)  # QTDE_ALIMENTACAO_CHOICES
    origem_alimentacao = db.Column(db.String(200), nullable=False)  # Lista de ALIMENTACAO_CHOICES
    
    # Higiene
    status_tem_acesso_higiene = db.Column(db.Boolean, nullable=False)
    tipos_higiene = db.Column(db.String(200))  # Lista de HIGIENE_CHOICES, requerido se tem acesso
    
    # Dados de registro
    criado_em = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    atualizado_em = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<SituacaoRua {self.id} - Cadastro {self.cadastro_id}>'

    def to_dict(self):
        return {
            'id': self.id,
            'cadastro_id': self.cadastro_id,
            'status_situacao_rua': self.status_situacao_rua,
            'tempo_rua': self.tempo_rua,
            'status_recebe_beneficio': self.status_recebe_beneficio,
            'beneficios': self.beneficios,
            'status_acompanhado_instituicao': self.status_acompanhado_instituicao,
            'instituicoes': self.instituicoes,
            'status_possui_referencia_familiar': self.status_possui_referencia_familiar,
            'grau_parentesco_referencia': self.grau_parentesco_referencia,
            'status_visita_familiar': self.status_visita_familiar,
            'frequencia_visita': self.frequencia_visita,
            'quantidade_alimentacoes_dia': self.quantidade_alimentacoes_dia,
            'origem_alimentacao': self.origem_alimentacao,
            'status_tem_acesso_higiene': self.status_tem_acesso_higiene,
            'tipos_higiene': self.tipos_higiene,
            'criado_em': self.criado_em.isoformat(),
            'atualizado_em': self.atualizado_em.isoformat()
        } 