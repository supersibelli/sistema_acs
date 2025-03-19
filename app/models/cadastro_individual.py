from app import db
from datetime import datetime

class CadastroIndividual(db.Model):
    __tablename__ = 'cadastro_individual'
    
    id = db.Column(db.Integer, primary_key=True)
    
    # Identificação do Usuário/Cidadão
    nome_completo = db.Column(db.String(100), nullable=False)
    nome_social = db.Column(db.String(100))
    data_nascimento = db.Column(db.Date, nullable=False)
    sexo = db.Column(db.String(1), nullable=False)  # 'M' ou 'F'
    raca_cor = db.Column(db.String(10), nullable=False)
    etnia = db.Column(db.String(50))  # Obrigatório se raca_cor == 'indigena'
    numero_nis = db.Column(db.String(11))  # 11 dígitos
    nome_mae = db.Column(db.String(100))
    mae_desconhecida = db.Column(db.Boolean, default=False)
    nome_pai = db.Column(db.String(100))
    pai_desconhecido = db.Column(db.Boolean, default=False)
    nacionalidade = db.Column(db.String(20), nullable=False)  # brasileira, naturalizado, estrangeiro
    pais_nascimento = db.Column(db.String(50))
    data_naturalizacao = db.Column(db.Date)
    portaria_naturalizacao = db.Column(db.String(50))
    municipio_nascimento = db.Column(db.String(100))
    uf_nascimento = db.Column(db.String(2))
    data_entrada_brasil = db.Column(db.Date)
    telefone_celular = db.Column(db.String(15))
    email = db.Column(db.String(100))
    
    # Campos del profesional (autollenados)
    cns_profissional = db.Column(db.String(15), nullable=False)
    cbo = db.Column(db.String(6), nullable=False)
    cnes = db.Column(db.String(7), nullable=False)
    ine = db.Column(db.String(10), nullable=False)
    microarea = db.Column(db.String(10), nullable=False)
    data_cadastro = db.Column(db.DateTime, nullable=False)
    
    # Campos de identificación del ciudadano
    cns_cidadao = db.Column(db.String(15))  # CNS del ciudadano
    cpf_cidadao = db.Column(db.String(11))  # CPF del ciudadano
    responsavel_familiar = db.Column(db.Boolean, default=False)
    cns_responsavel = db.Column(db.String(15))  # CNS del responsable
    cpf_responsavel = db.Column(db.String(11))  # CPF del responsable
    
    # Informações Sociodemográficas
    parentesco_responsavel = db.Column(db.String(20), nullable=False)  # Relação com responsável
    frequenta_escola = db.Column(db.Boolean, nullable=False)
    curso_frequenta = db.Column(db.String(100))
    situacao_trabalho = db.Column(db.String(30), nullable=False)
    ocupacao = db.Column(db.String(100))  # Nuevo campo
    crianca_ficacom = db.Column(db.String(20))  # Solo para niños de 0-9 años
    frequenta_cuidador = db.Column(db.Boolean, nullable=False)
    participa_grupo = db.Column(db.Boolean, nullable=False)
    possui_plano_saude = db.Column(db.Boolean, nullable=False)
    
    # Comunidade Tradicional
    membro_comunidade = db.Column(db.Boolean, nullable=False)
    qual_comunidade = db.Column(db.String(100))  # Obligatorio si membro_comunidade es True
    
    # Orientação Sexual
    informa_orientacao = db.Column(db.Boolean, nullable=False)
    orientacao_sexual = db.Column(db.String(20))  # Obligatorio si informa_orientacao es True
    
    # Identidade de Gênero
    informa_identidade = db.Column(db.Boolean, nullable=False)
    identidade_genero = db.Column(db.String(20))  # Obligatorio si informa_identidade es True
    
    # Deficiência
    tem_deficiencia = db.Column(db.Boolean, default=False)
    deficiencias = db.Column(db.String(500))  # Cambiado de 100 a 500 para permitir más opciones
    
    # Saída do Cadastro
    motivo_saida = db.Column(db.String(20))
    data_obito = db.Column(db.Date)
    numero_do = db.Column(db.String(20))  # Número da D.O.
    
    # TRIA
    tria_alimentos_acabaram = db.Column(db.Boolean, nullable=False)
    tria_comeu_alguns = db.Column(db.Boolean, nullable=False)
    
    # Condições/Situações de Saúde
    esta_gestante = db.Column(db.Boolean, nullable=False)
    maternidade_referencia = db.Column(db.String(100))  # Obligatorio si esta_gestante es True
    
    consideracao_peso = db.Column(db.String(20), nullable=False)  # abaixo, adequado, acima
    
    # Doença Respiratória
    tem_doenca_respiratoria = db.Column(db.Boolean, nullable=False)
    tipo_doenca_respiratoria = db.Column(db.String(20))  # asma, dpoc, outra, nao_sabe
    
    # Hábitos
    fumante = db.Column(db.Boolean, nullable=False)
    uso_alcool = db.Column(db.Boolean, nullable=False)
    uso_drogas = db.Column(db.Boolean, nullable=False)
    
    # Doenças Crônicas
    hipertensao_arterial = db.Column(db.Boolean, nullable=False)
    diabetes = db.Column(db.Boolean, nullable=False)
    teve_avc = db.Column(db.Boolean, nullable=False)
    teve_infarto = db.Column(db.Boolean, nullable=False)
    
    # Doença Cardíaca
    tem_doenca_cardiaca = db.Column(db.Boolean, nullable=False)
    tipo_doenca_cardiaca = db.Column(db.String(30))  # insuficiencia, outra, nao_sabe
    
    # Problemas Renais
    tem_problema_rins = db.Column(db.Boolean, nullable=False)
    tipo_problema_rins = db.Column(db.String(30))  # insuficiencia, outro, nao_sabe
    
    # Outras Doenças
    hanseniase = db.Column(db.Boolean, nullable=False)
    tuberculose = db.Column(db.Boolean, nullable=False)
    cancer = db.Column(db.Boolean, nullable=False)
    
    # Situações de Saúde
    internacao_12_meses = db.Column(db.Boolean, nullable=False)
    problema_saude_mental = db.Column(db.Boolean, nullable=False)
    acamado = db.Column(db.Boolean, nullable=False)
    domiciliado = db.Column(db.Boolean, nullable=False)
    
    # Práticas Integrativas
    usa_plantas_medicinais = db.Column(db.Boolean, nullable=False)
    usa_praticas_integrativas = db.Column(db.Boolean, nullable=False)
    
    # Outras Condições
    outras_condicoes = db.Column(db.String(300))  # Hasta 3 condiciones separadas por coma
    
    # Situação de Rua
    situacao_rua = db.Column(db.Boolean, nullable=False)
    tempo_rua = db.Column(db.String(20))  # Obligatorio si situacao_rua es True
    
    # Acompanhamento institucional
    acompanhado_instituicao = db.Column(db.Boolean, nullable=False)
    qual_instituicao = db.Column(db.String(200))  # Obligatorio si acompanhado_instituicao es True
    
    # Benefícios
    recebe_beneficio = db.Column(db.Boolean, nullable=False)
    qual_beneficio = db.Column(db.String(200))  # Obligatorio si recebe_beneficio es True
    
    # Referência Familiar
    possui_referencia_familiar = db.Column(db.Boolean, nullable=False)
    grau_parentesco = db.Column(db.String(100))  # Obligatorio si possui_referencia_familiar es True
    
    # Visitas Familiares
    visita_familiar = db.Column(db.Boolean, nullable=False)
    frequencia_visitas = db.Column(db.String(20))  # Obligatorio si visita_familiar es True
    
    # Higiene
    acesso_higiene = db.Column(db.Boolean, default=False)
    tipos_higiene = db.Column(db.String(500))  # Cambiado de 100 a 500 para permitir más opciones
    
    # Alimentação
    quantidade_alimentacao = db.Column(db.String(50), nullable=False)
    origem_alimentacao = db.Column(db.String(200), nullable=False)  # Lista separada por comas
    
    # Campos de control
    digitado_por = db.Column(db.String(100), nullable=False)
    data_digitacao = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    # Nuevos campos de timestamp
    data_criacao = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    data_atualizacao = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow) 