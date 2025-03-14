from app import db
from datetime import datetime
from app.models.constants import *

class CondicoesSaude(db.Model):
    __tablename__ = 'condicoes_saude'
    
    id = db.Column(db.Integer, primary_key=True)
    cadastro_id = db.Column(db.Integer, db.ForeignKey('cadastros_individuais.id'), nullable=False)
    
    # Gestação e Maternidade
    status_eh_gestante = db.Column(db.Boolean, nullable=False)
    maternidade_referencia = db.Column(db.String(100))  # Requerido se gestante
    
    # Condições de Saúde
    status_tem_hipertensao = db.Column(db.Boolean, nullable=False)
    status_tem_diabetes = db.Column(db.Boolean, nullable=False)
    status_teve_avc = db.Column(db.Boolean, nullable=False)
    status_teve_infarto = db.Column(db.Boolean, nullable=False)
    status_tem_doenca_cardiaca = db.Column(db.Boolean, nullable=False)
    doenca_cardiaca = db.Column(db.String(100))  # Lista de doenças cardíacas
    
    status_tem_doenca_respiratoria = db.Column(db.Boolean, nullable=False)
    doenca_respiratoria = db.Column(db.String(100))  # Lista de doenças respiratórias
    
    status_tem_teve_rins = db.Column(db.Boolean, nullable=False)
    problema_rins = db.Column(db.String(100))  # Lista de problemas renais
    
    status_tem_hanseniase = db.Column(db.Boolean, nullable=False)
    status_tem_tuberculose = db.Column(db.Boolean, nullable=False)
    status_tem_cancer = db.Column(db.Boolean, nullable=False)
    
    # Internações e Problemas Mentais
    status_teve_internado = db.Column(db.Boolean, nullable=False)
    descricao_causa_internacao = db.Column(db.String(100))  # Requerido se internado
    status_tem_problema_mental = db.Column(db.Boolean, nullable=False)
    
    # Condições de Vida
    status_esta_acamado = db.Column(db.Boolean, nullable=False)
    status_esta_domiciliado = db.Column(db.Boolean, nullable=False)
    status_usa_plantas_medicinais = db.Column(db.Boolean, nullable=False)
    descricao_plantas_medicinais = db.Column(db.String(100))  # Requerido se usa plantas
    
    # Práticas Integrativas e Complementares
    status_outras_praticas_integrativas = db.Column(db.Boolean, nullable=False)
    
    # Situação de Peso
    situacao_peso = db.Column(db.String(20), nullable=False)  # PESO_CHOICES
    
    # Dependência Química
    status_fumante = db.Column(db.Boolean, nullable=False)
    status_dependente_alcool = db.Column(db.Boolean, nullable=False)
    status_dependente_drogas = db.Column(db.Boolean, nullable=False)
    
    # Dados de registro
    criado_em = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    atualizado_em = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<CondicoesSaude {self.id} - Cadastro {self.cadastro_id}>'

    def to_dict(self):
        return {
            'id': self.id,
            'cadastro_id': self.cadastro_id,
            'status_eh_gestante': self.status_eh_gestante,
            'maternidade_referencia': self.maternidade_referencia,
            'status_tem_hipertensao': self.status_tem_hipertensao,
            'status_tem_diabetes': self.status_tem_diabetes,
            'status_teve_avc': self.status_teve_avc,
            'status_teve_infarto': self.status_teve_infarto,
            'status_tem_doenca_cardiaca': self.status_tem_doenca_cardiaca,
            'doenca_cardiaca': self.doenca_cardiaca,
            'status_tem_doenca_respiratoria': self.status_tem_doenca_respiratoria,
            'doenca_respiratoria': self.doenca_respiratoria,
            'status_tem_teve_rins': self.status_tem_teve_rins,
            'problema_rins': self.problema_rins,
            'status_tem_hanseniase': self.status_tem_hanseniase,
            'status_tem_tuberculose': self.status_tem_tuberculose,
            'status_tem_cancer': self.status_tem_cancer,
            'status_teve_internado': self.status_teve_internado,
            'descricao_causa_internacao': self.descricao_causa_internacao,
            'status_tem_problema_mental': self.status_tem_problema_mental,
            'status_esta_acamado': self.status_esta_acamado,
            'status_esta_domiciliado': self.status_esta_domiciliado,
            'status_usa_plantas_medicinais': self.status_usa_plantas_medicinais,
            'descricao_plantas_medicinais': self.descricao_plantas_medicinais,
            'status_outras_praticas_integrativas': self.status_outras_praticas_integrativas,
            'situacao_peso': self.situacao_peso,
            'status_fumante': self.status_fumante,
            'status_dependente_alcool': self.status_dependente_alcool,
            'status_dependente_drogas': self.status_dependente_drogas,
            'criado_em': self.criado_em.isoformat(),
            'atualizado_em': self.atualizado_em.isoformat()
        } 