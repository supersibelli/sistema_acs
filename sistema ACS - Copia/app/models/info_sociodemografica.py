from app import db
from datetime import datetime
from app.models.constants import *

class InfoSociodemografica(db.Model):
    __tablename__ = 'informacoes_sociodemograficas'
    
    id = db.Column(db.Integer, primary_key=True)
    cadastro_id = db.Column(db.Integer, db.ForeignKey('cadastros_individuais.id'), nullable=False)
    
    # Escolaridade e Trabalho
    frequenta_escola = db.Column(db.Boolean, nullable=False)
    curso_mais_elevado = db.Column(db.Integer, nullable=False)  # CURSO_CHOICES
    situacao_trabalho = db.Column(db.Integer, nullable=False)   # SITUACAO_TRABALHO_CHOICES
    ocupacao_codigo_cbo2002 = db.Column(db.String(6), nullable=False)
    
    # Orientação Sexual e Identidade de Gênero
    status_deseja_informar_orientacao_sexual = db.Column(db.Boolean, nullable=False)
    orientacao_sexual = db.Column(db.Integer, nullable=False)  # ORIENTACAO_SEXUAL_CHOICES
    status_deseja_informar_identidade_genero = db.Column(db.Boolean, nullable=False)
    identidade_genero = db.Column(db.Integer, nullable=False)  # IDENTIDADE_GENERO_CHOICES
    
    # Deficiência
    status_tem_deficiencia = db.Column(db.Boolean, nullable=False)
    deficiencias = db.Column(db.String(100), nullable=False)  # Lista de DEFICIENCIA_CHOICES separados por vírgula
    
    # Parentesco (obrigatório se não for responsável)
    relacao_parentesco = db.Column(db.Integer, nullable=False)  # PARENTESCO_CHOICES
    
    # Comunidade Tradicional
    status_comunidade_tradicional = db.Column(db.Boolean, nullable=False)
    tipo_comunidade_tradicional = db.Column(db.Integer, nullable=False)  # COMUNIDADE_TRADICIONAL_CHOICES
    
    # Outros dados sociais (todos obrigatórios)
    status_frequenta_cuidador = db.Column(db.Boolean, nullable=False)
    status_participa_grupo = db.Column(db.Boolean, nullable=False)
    status_possui_plano_saude = db.Column(db.Boolean, nullable=False)
    
    # Responsável por criança (0-9 anos)
    responsavel_crianca = db.Column(db.String(100), nullable=False)  # Lista de responsáveis separados por vírgula
    
    # Dados de registro
    criado_em = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    atualizado_em = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<InfoSociodemografica {self.id} - Cadastro {self.cadastro_id}>'

    def to_dict(self):
        return {
            'id': self.id,
            'cadastro_id': self.cadastro_id,
            'frequenta_escola': self.frequenta_escola,
            'curso_mais_elevado': self.curso_mais_elevado,
            'situacao_trabalho': self.situacao_trabalho,
            'ocupacao_codigo_cbo2002': self.ocupacao_codigo_cbo2002,
            'status_deseja_informar_orientacao_sexual': self.status_deseja_informar_orientacao_sexual,
            'orientacao_sexual': self.orientacao_sexual,
            'status_deseja_informar_identidade_genero': self.status_deseja_informar_identidade_genero,
            'identidade_genero': self.identidade_genero,
            'status_tem_deficiencia': self.status_tem_deficiencia,
            'deficiencias': self.deficiencias,
            'relacao_parentesco': self.relacao_parentesco,
            'status_comunidade_tradicional': self.status_comunidade_tradicional,
            'tipo_comunidade_tradicional': self.tipo_comunidade_tradicional,
            'status_frequenta_cuidador': self.status_frequenta_cuidador,
            'status_participa_grupo': self.status_participa_grupo,
            'status_possui_plano_saude': self.status_possui_plano_saude,
            'responsavel_crianca': self.responsavel_crianca,
            'criado_em': self.criado_em.isoformat(),
            'atualizado_em': self.atualizado_em.isoformat()
        } 