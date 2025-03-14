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
    microarea = db.Column(db.String(2), nullable=False)
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
    situacao_trabalho = db.Column(db.String(30), nullable=False)
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
    tem_deficiencia = db.Column(db.Boolean, nullable=False)
    deficiencias = db.Column(db.String(100))  # Lista separada por comas si tem_deficiencia es True
    
    # Saída do Cadastro
    motivo_saida = db.Column(db.String(20))
    data_obito = db.Column(db.Date)
    numero_do = db.Column(db.String(20))  # Número da D.O.
    
    # TRIA
    tria_alimentos_acabaram = db.Column(db.Boolean, nullable=False)
    tria_comeu_alguns = db.Column(db.Boolean, nullable=False)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow) 