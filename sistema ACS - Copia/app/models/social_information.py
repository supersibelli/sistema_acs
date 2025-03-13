from app import db
from datetime import datetime

class SocialInformation(db.Model):
    __tablename__ = 'informacoes_sociais'
    
    id = db.Column(db.Integer, primary_key=True)
    cidadao_id = db.Column(db.Integer, db.ForeignKey('citizens.id'), nullable=False)
    
    # Informações Sociodemográficas
    parentesco_responsavel = db.Column(db.String(50))
    frequenta_escola = db.Column(db.Boolean, nullable=False)
    curso_mais_elevado = db.Column(db.String(100))
    situacao_trabalho = db.Column(db.String(50))
    ocupacao = db.Column(db.String(100))
    
    # Crianças de 0 a 9 anos
    crianca_cuidador = db.Column(db.String(50))
    
    # Outros dados sociais
    frequenta_cuidador = db.Column(db.Boolean, default=False)
    participa_grupo = db.Column(db.Boolean, default=False)
    possui_plano_saude = db.Column(db.Boolean, default=False)
    membro_comunidade = db.Column(db.Boolean, default=False)
    tipo_comunidade = db.Column(db.String(100))
    
    # Orientação Sexual e Identidade de Gênero
    orientacao_sexual = db.Column(db.String(50))
    identidade_genero = db.Column(db.String(50))
    
    # Deficiência
    tem_deficiencia = db.Column(db.Boolean, nullable=False)
    tipo_deficiencia = db.Column(db.String(100))
    
    # Dados de registro
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<InformacaoSocial {self.id} - Cidadão {self.cidadao_id}>' 