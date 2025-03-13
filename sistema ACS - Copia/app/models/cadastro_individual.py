from app import db
from datetime import datetime
from app.models.constants import *

class CadastroIndividual(db.Model):
    __tablename__ = 'cadastros_individuais'
    
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(44), unique=True)
    ficha_atualizada = db.Column(db.Boolean, default=False)
    uuid_ficha_originadora = db.Column(db.String(44))
    status_termo_recusa = db.Column(db.Boolean, default=False)
    
    # Identificação do Cidadão
    nome_completo = db.Column(db.String(70), nullable=False)
    nome_social = db.Column(db.String(70))
    data_nascimento = db.Column(db.Date, nullable=False)
    sexo = db.Column(db.String(1), nullable=False)
    raca_cor = db.Column(db.String(20), nullable=False)
    etnia = db.Column(db.String(50))
    nacionalidade = db.Column(db.Integer, nullable=False)
    
    # Documentos
    cns = db.Column(db.String(15))
    cpf = db.Column(db.String(11))
    numero_nis = db.Column(db.String(11))
    
    # Filiação
    nome_mae = db.Column(db.String(70))
    desconhece_nome_mae = db.Column(db.Boolean, default=False)
    nome_pai = db.Column(db.String(70))
    desconhece_nome_pai = db.Column(db.Boolean, default=False)
    
    # Naturalização (se estrangeiro)
    data_naturalizacao = db.Column(db.Date)
    portaria_naturalizacao = db.Column(db.String(16))
    data_entrada_brasil = db.Column(db.Date)
    pais_nascimento = db.Column(db.Integer)
    
    # Contato
    email = db.Column(db.String(100))
    telefone = db.Column(db.String(11))
    
    # Localização
    municipio_nascimento = db.Column(db.String(7))  # Código IBGE
    microarea = db.Column(db.String(2))
    st_fora_area = db.Column(db.Boolean, default=False)
    
    # Responsável Familiar
    status_eh_responsavel = db.Column(db.Boolean, default=False)
    cns_responsavel = db.Column(db.String(15))
    cpf_responsavel = db.Column(db.String(11))
    
    # Dados de registro
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)
    atualizado_em = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    criado_por_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    # Relacionamentos
    criado_por = db.relationship('User', backref='cadastros')
    info_sociodemografica = db.relationship('InfoSociodemografica', backref='cadastro', uselist=False)
    condicoes_saude = db.relationship('CondicoesSaude', backref='cadastro', uselist=False)
    situacao_rua = db.relationship('SituacaoRua', backref='cadastro', uselist=False)
    saida_cadastro = db.relationship('SaidaCadastro', backref='cadastro', uselist=False)

    def __repr__(self):
        return f'<CadastroIndividual {self.nome_completo}>' 