# Choices para Identificação
SEXO_CHOICES = [
    (1, 'Masculino'),
    (2, 'Feminino')
]

# Opções para raça/cor
RACA_COR_CHOICES = [
    (1, 'Branca'),
    (2, 'Preta'),
    (3, 'Parda'),
    (4, 'Amarela'),
    (5, 'Indígena')
]

# Opções para peso auto-referido
PESO_CHOICES = [
    ('ABAIXO', 'Abaixo do Peso'),
    ('ADEQUADO', 'Peso Adequado'),
    ('ACIMA', 'Acima do Peso')
]

# Opções para doenças respiratórias
DOENCA_RESPIRATORIA_CHOICES = [
    ('ASMA', 'Asma'),
    ('DPOC', 'DPOC/Enfisema'),
    ('OUTRA', 'Outra'),
    ('NAO_SABE', 'Não Sabe')
]

# Opções para doenças cardíacas
DOENCA_CARDIACA_CHOICES = [
    ('INSUFICIENCIA', 'Insuficiência Cardíaca'),
    ('OUTRA', 'Outra'),
    ('NAO_SABE', 'Não Sabe')
]

# Opções para problemas renais
PROBLEMA_RINS_CHOICES = [
    ('INSUFICIENCIA', 'Insuficiência Renal'),
    ('OUTRO', 'Outro'),
    ('NAO_SABE', 'Não Sabe')
]

# Status do formulário
STATUS_CHOICES = [
    ('RASCUNHO', 'Rascunho'),
    ('PENDENTE', 'Pendente'),
    ('CONCLUIDO', 'Concluído')
]

# Nacionalidade
NACIONALIDADE_CHOICES = [
    (1, 'Brasileira'),
    (2, 'Naturalizada'),
    (3, 'Estrangeira')
]

# Orientação Sexual
ORIENTACAO_SEXUAL_CHOICES = [
    (1, 'Heterossexual'),
    (2, 'Gay'),
    (3, 'Lésbica'),
    (4, 'Bissexual'),
    (5, 'Outro')
]

# Identidade de Gênero
IDENTIDADE_GENERO_CHOICES = [
    (1, 'Homem Transexual'),
    (2, 'Mulher Transexual'),
    (3, 'Travesti'),
    (4, 'Outro')
]

# Situação de Mercado de Trabalho
SITUACAO_TRABALHO_CHOICES = [
    (1, 'Empregador'),
    (2, 'Assalariado com carteira'),
    (3, 'Assalariado sem carteira'),
    (4, 'Autônomo com previdência'),
    (5, 'Autônomo sem previdência'),
    (6, 'Aposentado/Pensionista'),
    (7, 'Desempregado'),
    (8, 'Não trabalha'),
    (9, 'Servidor público/Militar')
]

# Curso mais elevado
CURSO_CHOICES = [
    (1, 'Creche'),
    (2, 'Pré-escola'),
    (3, 'Alfabetização'),
    (4, 'Ensino Fundamental 1-4'),
    (5, 'Ensino Fundamental 5-8'),
    (6, 'Ensino Médio'),
    (7, 'Superior'),
    (8, 'Especialização'),
    (9, 'Mestrado'),
    (10, 'Doutorado')
]

# Deficiências
DEFICIENCIA_CHOICES = [
    (1, 'Auditiva'),
    (2, 'Visual'),
    (4, 'Intelectual/Cognitiva'),
    (8, 'Física'),
    (16, 'Outra')
]

# Parentesco com Responsável
PARENTESCO_CHOICES = [
    (1, 'Cônjuge/Companheiro(a)'),
    (2, 'Filho(a)'),
    (3, 'Enteado(a)'),
    (4, 'Pai/Mãe'),
    (5, 'Sogro(a)'),
    (6, 'Irmão/Irmã'),
    (7, 'Genro/Nora'),
    (8, 'Outro')
]

# Tempo em Situação de Rua
TEMPO_RUA_CHOICES = [
    (1, 'Menos de 6 meses'),
    (2, '6 a 12 meses'),
    (3, '1 a 2 anos'),
    (4, '2 a 5 anos'),
    (5, '5 a 10 anos'),
    (6, 'Mais de 10 anos')
]

# Acesso à Higiene
HIGIENE_CHOICES = [
    (1, 'Banho'),
    (2, 'Sanitário'),
    (3, 'Higiene bucal'),
    (4, 'Outros')
]

# Origem da Alimentação
ALIMENTACAO_CHOICES = [
    (1, 'Restaurante popular'),
    (2, 'Doação restaurante'),
    (3, 'Doação grupo religioso'),
    (4, 'Doação popular'),
    (5, 'Outros')
]

# Quantidade de Alimentações
QTDE_ALIMENTACAO_CHOICES = [
    (1, 'Uma vez'),
    (2, 'Duas vezes'),
    (3, 'Três ou mais vezes'),
    (4, 'Não se alimenta todos os dias')
]

# Motivo de Saída do Cadastro
MOTIVO_SAIDA_CHOICES = [
    (1, 'Mudança de território'),
    (2, 'Óbito'),
    (3, 'Outros')
]

# Povo ou Comunidade Tradicional
COMUNIDADE_TRADICIONAL_CHOICES = [
    (1, 'Quilombola'),
    (2, 'Indígena'),
    (3, 'Ribeirinha'),
    (4, 'Cigana'),
    (5, 'Outros')
]

# Choices para Práticas Integrativas
PRATICAS_INTEGRATIVAS_CHOICES = [
    (1, 'Acupuntura'),
    (2, 'Homeopatia'),
    (4, 'Fitoterapia'),
    (8, 'Auriculoterapia'),
    (16, 'Meditação'),
    (32, 'Yoga'),
    (64, 'Outra')
]

# Choices para Motivo de Internação
MOTIVO_INTERNACAO_CHOICES = [
    (1, 'Parto'),
    (2, 'Doença'),
    (3, 'Cirurgia'),
    (4, 'Lesão/Trauma'),
    (5, 'Tratamento psiquiátrico'),
    (6, 'Outro')
]

# Status de Acompanhamento
STATUS_ACOMPANHAMENTO_CHOICES = [
    (1, 'Ativo'),
    (2, 'Inativo')
]

# Tipos de Escola
TIPO_ESCOLA_CHOICES = [
    (1, 'Pública'),
    (2, 'Privada')
]

# Tipos de Moradia
TIPO_MORADIA_CHOICES = [
    (1, 'Própria'),
    (2, 'Alugada'),
    (3, 'Cedida'),
    (4, 'Ocupação'),
    (5, 'Situação de Rua'),
    (6, 'Outra')
]

# Material das Paredes
MATERIAL_PAREDES_CHOICES = [
    (1, 'Alvenaria'),
    (2, 'Madeira'),
    (3, 'Mista'),
    (4, 'Taipa'),
    (5, 'Outro')
]

# Abastecimento de Água
ABASTECIMENTO_AGUA_CHOICES = [
    (1, 'Rede Pública'),
    (2, 'Poço/Nascente'),
    (3, 'Cisterna'),
    (4, 'Outro')
]

# Material do Piso
MATERIAL_PISO_CHOICES = [
    (1, 'Cerâmica/Lajota'),
    (2, 'Cimento'),
    (3, 'Terra batida'),
    (4, 'Madeira'),
    (5, 'Outro')
]

# Tratamento de Água
TRATAMENTO_AGUA_CHOICES = [
    (1, 'Filtração'),
    (2, 'Fervura'),
    (3, 'Cloração'),
    (4, 'Sem tratamento')
]

# Escoamento Sanitário
ESCOAMENTO_SANITARIO_CHOICES = [
    (1, 'Rede coletora'),
    (2, 'Fossa séptica'),
    (3, 'Fossa rudimentar'),
    (4, 'Céu aberto'),
    (5, 'Outro')
]

# Destino do Lixo
DESTINO_LIXO_CHOICES = [
    (1, 'Coletado'),
    (2, 'Queimado/Enterrado'),
    (3, 'Céu aberto'),
    (4, 'Outro')
]

# Tipo de Logradouro
TIPO_LOGRADOURO_CHOICES = [
    (1, 'Rua'),
    (2, 'Avenida'),
    (3, 'Travessa'),
    (4, 'Praça'),
    (5, 'Alameda'),
    (6, 'Estrada'),
    (7, 'Outro')
]

# Fonte Principal de Renda
FONTE_RENDA_CHOICES = [
    (1, 'Trabalho formal'),
    (2, 'Trabalho informal'),
    (3, 'Aposentadoria'),
    (4, 'Pensão'),
    (5, 'Benefício social'),
    (6, 'Doação'),
    (7, 'Outro')
]

# Benefícios Sociais
BENEFICIOS_SOCIAIS_CHOICES = [
    (1, 'Bolsa Família'),
    (2, 'BPC'),
    (4, 'Aposentadoria'),
    (8, 'Pensão'),
    (16, 'Auxílio Doença'),
    (32, 'Outro')
]

# Status de Saúde Mental
SAUDE_MENTAL_CHOICES = [
    (1, 'Depressão'),
    (2, 'Ansiedade'),
    (4, 'Esquizofrenia'),
    (8, 'Transtorno Bipolar'),
    (16, 'Outro')
]

# Tipos de Cirurgia
TIPO_CIRURGIA_CHOICES = [
    (1, 'Parto cesáreo'),
    (2, 'Apendicite'),
    (4, 'Vesícula'),
    (8, 'Hérnia'),
    (16, 'Ortopédica'),
    (32, 'Cardíaca'),
    (64, 'Outra')
]

# Tipos de IST
TIPO_IST_CHOICES = [
    (1, 'HIV'),
    (2, 'Sífilis'),
    (4, 'Hepatite B'),
    (8, 'Hepatite C'),
    (16, 'Outra')
]

# Tipos de Dieta
TIPO_DIETA_CHOICES = [
    (1, 'Hipossódica'),
    (2, 'Hipoglicêmica'),
    (4, 'Hipolipídica'),
    (8, 'Sem glúten'),
    (16, 'Sem lactose'),
    (32, 'Outra')
]

# Tipos de Medicamentos
TIPO_MEDICAMENTO_CHOICES = [
    (1, 'Anti-hipertensivo'),
    (2, 'Hipoglicemiante'),
    (4, 'Antidepressivo'),
    (8, 'Ansiolítico'),
    (16, 'Anticonvulsivante'),
    (32, 'Outro')
]

# Grupos Comunitários
GRUPO_COMUNITARIO_CHOICES = [
    (1, 'Religioso'),
    (2, 'Cultural'),
    (4, 'Esportivo'),
    (8, 'Associação de moradores'),
    (16, 'Outro')
]

# Estado Civil
ESTADO_CIVIL_CHOICES = [
    (1, 'Solteiro(a)'),
    (2, 'Casado(a)'),
    (3, 'União estável'),
    (4, 'Viúvo(a)'),
    (5, 'Divorciado(a)/Separado(a)')
]

# Relação de Parentesco
RELACAO_PARENTESCO_CHOICES = [
    (1, 'Responsável'),
    (2, 'Cônjuge/Companheiro(a)'),
    (3, 'Filho(a)'),
    (4, 'Enteado(a)'),
    (5, 'Neto(a)'),
    (6, 'Pai/Mãe'),
    (7, 'Sogro(a)'),
    (8, 'Irmão/Irmã'),
    (9, 'Genro/Nora'),
    (10, 'Outro')
]

# Frequência de Visita Familiar
FREQUENCIA_VISITA_CHOICES = [
    (1, 'Diária'),
    (2, 'Semanal'),
    (3, 'Quinzenal'),
    (4, 'Mensal'),
    (5, 'Trimestral'),
    (6, 'Semestral'),
    (7, 'Anual'),
    (8, 'Não recebe visitas')
]

# Motivo de Saída do Território
MOTIVO_SAIDA_TERRITORIO_CHOICES = [
    (1, 'Mudança de território'),
    (2, 'Óbito'),
    (3, 'Mudança de município'),
    (4, 'Mudança de estado'),
    (5, 'Mudança de país')
]

# Grau de Escolaridade
ESCOLARIDADE_CHOICES = [
    (1, 'Não sabe ler/escrever'),
    (2, 'Alfabetizado'),
    (3, 'Fundamental incompleto'),
    (4, 'Fundamental completo'),
    (5, 'Médio incompleto'),
    (6, 'Médio completo'),
    (7, 'Superior incompleto'),
    (8, 'Superior completo'),
    (9, 'Pós-graduação')
]

# Ocupação Principal
OCUPACAO_CHOICES = [
    (1, 'Empregado(a) com carteira'),
    (2, 'Empregado(a) sem carteira'),
    (3, 'Autônomo(a)'),
    (4, 'Aposentado(a)/Pensionista'),
    (5, 'Desempregado(a)'),
    (6, 'Dona(o) de casa'),
    (7, 'Estudante'),
    (8, 'Outro')
]

# Tipo de Transporte
TIPO_TRANSPORTE_CHOICES = [
    (1, 'Próprio'),
    (2, 'Público'),
    (3, 'Ambulância'),
    (4, 'Animal'),
    (5, 'A pé'),
    (6, 'Outro')
]

# Condições de Saúde/Doenças
CONDICOES_SAUDE_CHOICES = [
    (1, 'Diabetes'),
    (2, 'Hipertensão'),
    (4, 'Tuberculose'),
    (8, 'Hanseníase'),
    (16, 'Câncer'),
    (32, 'Problemas mentais'),
    (64, 'Problemas respiratórios'),
    (128, 'DST/AIDS'),
    (256, 'Alcoolismo'),
    (512, 'Drogas'),
    (1024, 'Deficiência'),
    (2048, 'Outra')
]

# Práticas Integrativas Complementares
PRATICAS_INTEGRATIVAS_DETALHADAS_CHOICES = [
    (1, 'Medicina Tradicional Chinesa'),
    (2, 'Antroposofia'),
    (4, 'Homeopatia'),
    (8, 'Fitoterapia'),
    (16, 'Termalismo/Crenoterapia'),
    (32, 'Reiki'),
    (64, 'Medicina Ayurveda'),
    (128, 'Outra')
]

# Situação Vacinal
SITUACAO_VACINAL_CHOICES = [
    (1, 'Em dia'),
    (2, 'Não está em dia'),
    (3, 'Não sabe informar')
]

# Plano de Saúde
PLANO_SAUDE_CHOICES = [
    (1, 'Não possui'),
    (2, 'Particular'),
    (3, 'Por convênio'),
    (4, 'Outro')
]

# Tipo de Atendimento
TIPO_ATENDIMENTO_CHOICES = [
    (1, 'Consulta agendada'),
    (2, 'Demanda espontânea'),
    (3, 'Cuidado continuado'),
    (4, 'Urgência'),
    (5, 'Outro')
]

# Local de Atendimento
LOCAL_ATENDIMENTO_CHOICES = [
    (1, 'UBS'),
    (2, 'Unidade móvel'),
    (3, 'Rua'),
    (4, 'Domicílio'),
    (5, 'Escola'),
    (6, 'Outros')
]

# Modalidade
MODALIDADE_CHOICES = [
    (1, 'Individual'),
    (2, 'Coletiva')
]

# Tipo de Acompanhamento
TIPO_ACOMPANHAMENTO_CHOICES = [
    (1, 'Puericultura'),
    (2, 'Pré-natal'),
    (3, 'Puerpério'),
    (4, 'Hipertensão'),
    (5, 'Diabetes'),
    (6, 'Asma'),
    (7, 'Saúde mental'),
    (8, 'Outro')
] 