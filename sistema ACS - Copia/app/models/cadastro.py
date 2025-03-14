from app import db
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
import uuid

class CadastroIndividual(db.Model):
    __tablename__ = 'cadastros_individuais'

    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True)
    
    # Identificação
    nome_completo = db.Column(db.String(70), nullable=False)
    nome_social = db.Column(db.String(70))
    data_nascimento = db.Column(db.Date, nullable=False)
    sexo = db.Column(db.Integer, nullable=False)
    raca_cor = db.Column(db.Integer, nullable=False)
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
    
    # Naturalização
    data_naturalizacao = db.Column(db.Date)
    portaria_naturalizacao = db.Column(db.String(16))
    data_entrada_brasil = db.Column(db.Date)
    pais_nascimento = db.Column(db.String(3))
    
    # Contato
    email = db.Column(db.String(100))
    telefone = db.Column(db.String(11))
    
    # Localização
    municipio_nascimento = db.Column(db.String(7))
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
    criado_por = db.relationship('User', backref='cadastros_criados')
    info_sociodemografica = db.relationship('InfoSociodemografica', 
                                          backref='cadastro_individual', 
                                          uselist=False)
    condicoes_saude = db.relationship('CondicoesSaude', 
                                     backref='cadastro_individual', 
                                     uselist=False)
    situacao_rua = db.relationship('SituacaoRua', 
                                  backref='cadastro_individual', 
                                  uselist=False)
    saida = db.relationship('SaidaCadastro', 
                           backref='cadastro_individual', 
                           uselist=False)

    # Campos adicionales para Identificação
    nome_completo_mae = db.Column(db.String(70))
    nome_completo_pai = db.Column(db.String(70))
    ocupacao = db.Column(db.String(100))
    
    # Endereço
    tipo_logradouro = db.Column(db.String(20))
    logradouro = db.Column(db.String(100))
    numero = db.Column(db.String(10))
    complemento = db.Column(db.String(100))
    bairro = db.Column(db.String(100))
    cep = db.Column(db.String(8))
    municipio = db.Column(db.String(7))
    uf = db.Column(db.String(2))
    
    # Comunidade Tradicional
    status_comunidade_tradicional = db.Column(db.Boolean, default=False)
    tipo_comunidade_tradicional = db.Column(db.Integer)
    
    # Plano de Saúde
    status_plano_saude_privado = db.Column(db.Boolean, default=False)
    nome_plano_saude = db.Column(db.String(100))
    
    # Referência Familiar
    grau_parentesco = db.Column(db.Integer)
    status_frequenta_benzedeira = db.Column(db.Boolean, default=False)
    status_participa_grupo_comunitario = db.Column(db.Boolean, default=False)
    grupos_comunitarios = db.Column(db.String(200))
    status_possui_referencia_familiar = db.Column(db.Boolean, default=False)
    nome_referencia_familiar = db.Column(db.String(70))
    
    # Status do Cadastro
    status = db.Column(db.Integer, default=1)  # 1=Ativo, 2=Inativo

class InfoSociodemografica(db.Model):
    __tablename__ = 'info_sociodemografica'
    
    id = db.Column(db.Integer, primary_key=True)
    cadastro_id = db.Column(db.Integer, db.ForeignKey('cadastros_individuais.id'), nullable=False)
    
    # Educação e Trabalho
    frequenta_escola = db.Column(db.Boolean, default=False)
    curso_mais_elevado = db.Column(db.Integer)
    situacao_trabalho = db.Column(db.Integer)
    ocupacao_codigo_cbo2002 = db.Column(db.String(6))
    
    # Orientação Sexual e Identidade de Gênero
    status_deseja_informar_orientacao_sexual = db.Column(db.Boolean, default=False)
    orientacao_sexual = db.Column(db.Integer)
    status_deseja_informar_identidade_genero = db.Column(db.Boolean, default=False)
    identidade_genero = db.Column(db.Integer)

    # Educação
    status_frequenta_escola = db.Column(db.Boolean, default=False)
    tipo_escola = db.Column(db.Integer)  # 1=Pública, 2=Privada
    grau_escolaridade = db.Column(db.Integer)
    status_alfabetizado = db.Column(db.Boolean, default=False)
    
    # Trabalho e Renda
    status_trabalha = db.Column(db.Boolean, default=False)
    ocupacao_atual = db.Column(db.String(100))
    principal_fonte_renda = db.Column(db.Integer)
    renda_familiar = db.Column(db.Float)
    numero_membros_familia = db.Column(db.Integer)
    
    # Benefícios Sociais
    status_recebe_beneficio = db.Column(db.Boolean, default=False)
    beneficios_sociais = db.Column(db.Integer)  # Usar bits para múltiplos benefícios
    valor_total_beneficios = db.Column(db.Float)
    
    # Condições de Moradia
    tipo_moradia = db.Column(db.Integer)
    material_paredes = db.Column(db.Integer)
    material_piso = db.Column(db.Integer)
    numero_comodos = db.Column(db.Integer)
    tipo_abastecimento_agua = db.Column(db.Integer)
    tipo_tratamento_agua = db.Column(db.Integer)
    tipo_escoamento_sanitario = db.Column(db.Integer)
    destino_lixo = db.Column(db.Integer)
    disponibilidade_energia_eletrica = db.Column(db.Boolean, default=False)
    
    # Animais no Domicílio
    status_possui_animais = db.Column(db.Boolean, default=False)
    numero_gatos = db.Column(db.Integer, default=0)
    numero_caes = db.Column(db.Integer, default=0)
    numero_aves = db.Column(db.Integer, default=0)
    numero_outros_animais = db.Column(db.Integer, default=0)

class CondicoesSaude(db.Model):
    __tablename__ = 'condicoes_saude'
    
    id = db.Column(db.Integer, primary_key=True)
    cadastro_id = db.Column(db.Integer, db.ForeignKey('cadastros_individuais.id'), nullable=False)
    
    # Condições Gerais
    status_eh_gestante = db.Column(db.Boolean, default=False)
    data_prevista_parto = db.Column(db.Date)
    maternidade_referencia = db.Column(db.String(100))
    
    # Doenças Crônicas
    status_tem_hipertensao = db.Column(db.Boolean, default=False)
    status_tem_diabetes = db.Column(db.Boolean, default=False)
    status_teve_avc = db.Column(db.Boolean, default=False)
    status_teve_infarto = db.Column(db.Boolean, default=False)
    status_tem_doenca_cardiaca = db.Column(db.Boolean, default=False)
    doenca_cardiaca_qual = db.Column(db.String(100))
    status_tem_problemas_rins = db.Column(db.Boolean, default=False)
    problema_rins_qual = db.Column(db.String(100))
    status_tem_asma = db.Column(db.Boolean, default=False)
    status_tem_dpoc = db.Column(db.Boolean, default=False)
    status_tem_cancer = db.Column(db.Boolean, default=False)
    cancer_qual = db.Column(db.String(100))
    
    # Problemas Mentais
    status_teve_problema_mental = db.Column(db.Boolean, default=False)
    problema_mental_qual = db.Column(db.String(100))
    
    # Internações e Cirurgias
    status_teve_internacao_12meses = db.Column(db.Boolean, default=False)
    motivo_internacao = db.Column(db.String(100))
    status_fez_cirurgia = db.Column(db.Boolean, default=False)
    cirurgia_qual = db.Column(db.String(100))
    
    # Deficiência
    status_tem_deficiencia = db.Column(db.Boolean, default=False)
    deficiencias = db.Column(db.Integer)  # Usar bits para múltiplas deficiências
    
    # Doenças Transmissíveis
    status_esta_com_hanseniase = db.Column(db.Boolean, default=False)
    status_esta_com_tuberculose = db.Column(db.Boolean, default=False)
    status_esta_com_dengue = db.Column(db.Boolean, default=False)
    status_esta_com_ist = db.Column(db.Boolean, default=False)
    ist_qual = db.Column(db.String(100))
    
    # Situação de Peso
    status_esta_acamado = db.Column(db.Boolean, default=False)
    status_esta_domiciliado = db.Column(db.Boolean, default=False)
    peso = db.Column(db.Float)
    altura = db.Column(db.Float)
    status_requer_dieta_especial = db.Column(db.Boolean, default=False)
    dieta_especial_qual = db.Column(db.String(100))
    
    # Medicamentos
    status_usa_medicamentos = db.Column(db.Boolean, default=False)
    medicamentos_quais = db.Column(db.String(200))
    status_precisa_medicamentos = db.Column(db.Boolean, default=False)
    medicamentos_necessarios = db.Column(db.String(200))
    
    # Reações Adversas
    status_tem_alergia_medicamento = db.Column(db.Boolean, default=False)
    alergia_medicamento_qual = db.Column(db.String(200))
    status_tem_outras_alergias = db.Column(db.Boolean, default=False)
    outras_alergias_quais = db.Column(db.String(200))
    
    # Práticas Integrativas e Complementares
    status_usa_plantas_medicinais = db.Column(db.Boolean, default=False)
    plantas_medicinais_usadas = db.Column(db.String(200))
    status_usa_praticas_integrativas = db.Column(db.Boolean, default=False)
    praticas_integrativas = db.Column(db.Integer)  # Usar bits para múltiplas práticas
    
    # Outras Condições
    outras_condicoes_saude = db.Column(db.String(200))

class SituacaoRua(db.Model):
    __tablename__ = 'situacao_rua'
    
    id = db.Column(db.Integer, primary_key=True)
    cadastro_id = db.Column(db.Integer, db.ForeignKey('cadastros_individuais.id'), nullable=False)
    
    status_situacao_rua = db.Column(db.Boolean, default=False)
    tempo_rua = db.Column(db.Integer)

    # Campos adicionais
    tempo_situacao_rua = db.Column(db.Integer)
    origem_alimentacao = db.Column(db.Integer)  # Usar bits para múltiplas origens
    quantidade_refeicoes_dia = db.Column(db.Integer)
    local_dormir = db.Column(db.String(100))
    acesso_higiene_pessoal = db.Column(db.Integer)  # Usar bits para múltiplos acessos
    status_recebe_beneficio = db.Column(db.Boolean, default=False)
    beneficios_recebidos = db.Column(db.Integer)  # Usar bits para múltiplos benefícios
    referencias_familiares = db.Column(db.String(200))
    status_possui_referencia_familiar = db.Column(db.Boolean, default=False)
    status_visita_familiar = db.Column(db.Boolean, default=False)
    tempo_sem_visitar_familia = db.Column(db.Integer)

class SaidaCadastro(db.Model):
    __tablename__ = 'saidas_cadastro'
    
    id = db.Column(db.Integer, primary_key=True)
    cadastro_id = db.Column(db.Integer, db.ForeignKey('cadastros_individuais.id'), nullable=False)
    
    motivo = db.Column(db.Integer, nullable=False)
    data_saida = db.Column(db.Date, nullable=False)
    observacao = db.Column(db.Text)
    
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)
    criado_por_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    criado_por = db.relationship('User', backref='saidas_registradas') 