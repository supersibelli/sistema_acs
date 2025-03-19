from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, EmailField, BooleanField, SelectMultipleField
from wtforms.validators import DataRequired, Email, Optional, Length, Regexp, ValidationError
from datetime import datetime

def validate_date(form, field):
    if field.data:
        try:
            # Intenta convertir la fecha al formato correcto
            datetime.strptime(field.data, '%d/%m/%Y')
            return True
        except ValueError:
            raise ValidationError('Data inválida. Use o formato DD/MM/AAAA')

class CadastroIndividualForm(FlaskForm):
    nome_completo = StringField('Nome Completo', 
                              validators=[DataRequired(message="Nome completo é obrigatório")])
    
    nome_social = StringField('Nome Social')
    
    data_nascimento = StringField('Data de Nascimento', 
                               validators=[DataRequired(message="Data de nascimento é obrigatória"),
                                         Regexp(r'^\d{2}/\d{2}/\d{4}$', 
                                               message="Use o formato DD/MM/AAAA"),
                                         validate_date])
    
    sexo = SelectField('Sexo', 
                      choices=[('', 'Selecione...'),
                              ('F', 'Feminino'),
                              ('M', 'Masculino')],
                      validators=[DataRequired(message="Sexo é obrigatório")])
    
    raca_cor = SelectField('Raça/Cor',
                          choices=[('', 'Selecione...'),
                                  ('branca', 'Branca'),
                                  ('preta', 'Preta'),
                                  ('parda', 'Parda'),
                                  ('amarela', 'Amarela'),
                                  ('indigena', 'Indígena')],
                          validators=[DataRequired(message="Raça/Cor é obrigatória")])
    
    etnia = StringField('Etnia')
    
    numero_nis = StringField('Número NIS (PIS/PASEP)', 
                           validators=[Optional(), 
                                     Length(11, 11, message="NIS deve ter 11 dígitos"),
                                     Regexp(r'^\d{11}$', message="NIS deve conter apenas números")])
    
    nome_mae = StringField('Nome Completo da Mãe', 
                          validators=[Optional()])
    mae_desconhecida = BooleanField('Desconhecido')
    
    nome_pai = StringField('Nome Completo do Pai', 
                          validators=[Optional()])
    pai_desconhecido = BooleanField('Desconhecido')
    
    nacionalidade = SelectField('Nacionalidade *',
        choices=[
            ('', 'Selecione...'),
            ('brasileira', 'Brasileira'),
            ('estrangeira', 'Estrangeira'),
            ('naturalizada', 'Naturalizada')
        ],
        validators=[DataRequired(message='Por favor, selecione a nacionalidade')])
    
    pais_nascimento = StringField('País de Nascimento')
    data_naturalizacao = StringField('Data de Naturalização', 
                                  validators=[Optional(),
                                            Regexp(r'^\d{2}/\d{2}/\d{4}$', 
                                                  message="Use o formato DD/MM/AAAA"),
                                            validate_date])
    portaria_naturalizacao = StringField('Portaria de Naturalização')
    municipio_nascimento = StringField('Município de Nascimento')
    uf_nascimento = StringField('UF de Nascimento', validators=[Optional(), Length(2, 2)])
    data_entrada_brasil = StringField('Data de Entrada no Brasil', 
                                   validators=[Optional(),
                                             Regexp(r'^\d{2}/\d{2}/\d{4}$', 
                                                   message="Use o formato DD/MM/AAAA"),
                                             validate_date])
    
    telefone_celular = StringField('Telefone Celular', 
        validators=[
            DataRequired(),
            Regexp(r'^\(\d{2}\) \d{5}-\d{4}$', 
                message='Formato inválido. Use (XX) XXXXX-XXXX')
        ])
    
    email = EmailField('E-mail', 
                      validators=[Optional(),
                                Email(message="Digite um e-mail válido")])

    # Campos del ciudadano
    cns_cidadao = StringField('CNS do Cidadão',
                           validators=[Optional(),
                                     Length(15, 15, message="CNS deve ter 15 dígitos"),
                                     Regexp(r'^\d{15}$', message="CNS deve conter apenas números")])
    
    cpf_cidadao = StringField('CPF do Cidadão',
                           validators=[Optional(),
                                     Length(11, 11, message="CPF deve ter 11 dígitos"),
                                     Regexp(r'^\d{11}$', message="CPF deve conter apenas números")])
    
    responsavel_familiar = BooleanField('Cidadão é o Responsável Familiar?')
    
    cns_responsavel = StringField('CNS do Responsável Familiar',
                               validators=[Optional(),
                                         Length(15, 15, message="CNS deve ter 15 dígitos"),
                                         Regexp(r'^\d{15}$', message="CNS deve conter apenas números")])
    
    cpf_responsavel = StringField('CPF do Responsável Familiar',
                               validators=[Optional(),
                                         Length(11, 11, message="CPF deve ter 11 dígitos"),
                                         Regexp(r'^\d{11}$', message="CPF deve conter apenas números")])

    # Relação de Parentesco
    parentesco_responsavel = SelectField('Relação de Parentesco com o Responsável Familiar',
        choices=[
            ('', 'Selecione...'),
            ('conjuge', 'Cônjuge/Companheiro(a)'),
            ('filho', 'Filho(a)'),
            ('enteado', 'Enteado(a)'),
            ('neto', 'Neto(a)/Bisneto(a)'),
            ('pai', 'Pai/Mãe'),
            ('sogro', 'Sogro(a)'),
            ('irmao', 'Irmão/Irmã'),
            ('genro', 'Genro/Nora'),
            ('outro_parente', 'Outro parente'),
            ('nao_parente', 'Não parente')
        ],
        validators=[DataRequired(message='Relação de parentesco é obrigatória')])

    # Escola/Creche
    frequenta_escola = BooleanField('Frequenta Escola ou Creche? *')
    curso_frequenta = SelectField('Qual é o Curso Mais Elevado que Frequenta ou Frequentou?',
        choices=[
            ('', 'Selecione...'),
            ('creche', 'Creche'),
            ('pre_escola', 'Pré-escola (exceto CA)'),
            ('classe_alfabetizacao', 'Classe de Alfabetização - CA'),
            ('fundamental_1_4', 'Ensino Fundamental 1ª a 4ª séries'),
            ('fundamental_5_8', 'Ensino Fundamental 5ª a 8ª séries'),
            ('fundamental_completo', 'Ensino Fundamental Completo'),
            ('fundamental_especial', 'Ensino Fundamental Especial'),
            ('fundamental_eja_1_4', 'Ensino Fundamental EJA - séries iniciais (Supletivo 1ª a 4ª)'),
            ('fundamental_eja_5_8', 'Ensino Fundamental EJA - séries finais (Supletivo 5ª a 8ª)'),
            ('medio', 'Ensino Médio, Médio 2º Ciclo (Científico, Técnico etc.)'),
            ('medio_especial', 'Ensino Médio Especial'),
            ('medio_eja', 'Ensino Médio EJA (Supletivo)'),
            ('superior', 'Superior, Aperfeiçoamento, Especialização, Mestrado, Doutorado'),
            ('alfabetizacao_adultos', 'Alfabetização para Adultos (Mobral etc.)'),
            ('nenhum', 'Nenhum')
        ])

    # Situação Trabalho
    situacao_trabalho = SelectField('Situação no Mercado de Trabalho',
        choices=[
            ('', 'Selecione...'),
            ('empregador', 'Empregador'),
            ('assalariado_com_carteira', 'Assalariado com carteira de trabalho'),
            ('assalariado_sem_carteira', 'Assalariado sem carteira de trabalho'),
            ('autonomo_com_previdencia', 'Autônomo com previdência social'),
            ('autonomo_sem_previdencia', 'Autônomo sem previdência social'),
            ('aposentado', 'Aposentado/Pensionista'),
            ('desempregado', 'Desempregado'),
            ('nao_trabalha', 'Não trabalha'),
            ('servidor_publico', 'Servidor público/militar'),
            ('outro', 'Outro')
        ],
        validators=[DataRequired(message='Situação no mercado de trabalho é obrigatória')])

    # Ocupação
    ocupacao = StringField('Ocupação',
        validators=[Length(max=100, message='Máximo de 100 caracteres')])

    # Crianças 0-9 anos
    crianca_ficacom = SelectField('Crianças de 0 a 9 anos, com quem fica?',
        choices=[
            ('', 'Selecione...'),
            ('adulto', 'Adulto Responsável'),
            ('crianca', 'Outra(s) Criança(s)'),
            ('adolescente', 'Adolescente'),
            ('sozinha', 'Sozinha'),
            ('creche', 'Creche'),
            ('outro', 'Outro')
        ])

    # Campos Sim/Não simples
    frequenta_cuidador = BooleanField('Frequenta Cuidador Tradicional?')
    participa_grupo = BooleanField('Participa de Algum Grupo Comunitário?')
    possui_plano_saude = BooleanField('Possui Plano de Saúde Privado?')

    # Comunidade Tradicional
    membro_comunidade = BooleanField('É Membro de Povo ou Comunidade Tradicional?')
    qual_comunidade = StringField('Qual?')

    # Orientação Sexual
    informa_orientacao = BooleanField('Deseja Informar Orientação Sexual?')
    orientacao_sexual = SelectField('Orientação Sexual',
        choices=[
            ('', 'Selecione...'),
            ('heterossexual', 'Heterossexual'),
            ('gay', 'Gay'),
            ('lesbica', 'Lésbica'),
            ('bissexual', 'Bissexual'),
            ('assexual', 'Assexual'),
            ('pansexual', 'Pansexual'),
            ('outro', 'Outro')
        ])

    # Identidade de Gênero
    informa_identidade = BooleanField('Deseja Informar Identidade de Gênero?')
    identidade_genero = SelectField('Identidade de Gênero',
        choices=[
            ('', 'Selecione...'),
            ('homem_cis', 'Homem cisgênero'),
            ('mulher_cis', 'Mulher cisgênero'),
            ('homem_trans', 'Homem transgênero'),
            ('mulher_trans', 'Mulher transgênero'),
            ('travesti', 'Travesti'),
            ('nao_binario', 'Não-Binário'),
            ('outro', 'Outro')
        ])

    # Deficiência
    tem_deficiencia = BooleanField('Tem Alguma Deficiência?')
    deficiencias = SelectField('Deficiências',
        choices=[
            ('', 'Selecione...'),
            ('auditiva', 'Auditiva'),
            ('visual', 'Visual'),
            ('intelectual', 'Intelectual/Cognitiva'),
            ('fisica', 'Física'),
            ('outra', 'Outra')
        ])

    # Saída do Cadastro
    motivo_saida = SelectField('Saída do Cidadão do Cadastro',
        choices=[
            ('', 'Selecione...'),
            ('mudanca', 'Mudança de território'),
            ('obito', 'Óbito')
        ])
    data_obito = StringField('Data do óbito',
        validators=[Optional(),
                   Regexp(r'^\d{2}/\d{2}/\d{4}$', message="Use o formato DD/MM/AAAA"),
                   validate_date])
    numero_do = StringField('Número da D.O.')

    # TRIA
    tria_alimentos_acabaram = BooleanField('Nos últimos três meses, os alimentos acabaram antes que você tivesse dinheiro para comprar mais comida?')
    tria_comeu_alguns = BooleanField('Nos últimos três meses, você comeu apenas alguns alimentos que ainda tinha, porque o dinheiro acabou?')

    # Condições/Situações de Saúde
    esta_gestante = BooleanField('Está Gestante?')
    maternidade_referencia = StringField('Qual é a Maternidade de Referência?')

    consideracao_peso = SelectField('Sobre seu peso, você se considera? *',
        choices=[
            ('', 'Selecione...'),
            ('abaixo', 'Abaixo do Peso'),
            ('adequado', 'Peso Adequado'),
            ('acima', 'Acima do Peso')
        ],
        validators=[DataRequired(message='Por favor, selecione como considera seu peso')])

    # Doença Respiratória
    tem_doenca_respiratoria = BooleanField('Tem Doença Respiratória/No Pulmão?')
    tipo_doenca_respiratoria = SelectField('Se sim, qual?',
        choices=[
            ('', 'Selecione...'),
            ('asma', 'Asma'),
            ('dpoc', 'DPOC/Enfisema'),
            ('outra', 'Outra'),
            ('nao_sabe', 'Não Sabe')
        ])

    # Hábitos
    fumante = BooleanField('Está Fumante?')
    uso_alcool = BooleanField('Faz Uso de Álcool?')
    uso_drogas = BooleanField('Faz Uso de Outras Drogas?')

    # Doenças Crônicas
    hipertensao_arterial = BooleanField('Tem Hipertensão Arterial?')
    diabetes = BooleanField('Tem Diabetes?')
    teve_avc = BooleanField('Teve AVC/Derrame?')
    teve_infarto = BooleanField('Teve Infarto?')

    # Doença Cardíaca
    tem_doenca_cardiaca = BooleanField('Tem Doença Cardíaca/Do Coração?')
    tipo_doenca_cardiaca = SelectField('Se sim, qual?',
        choices=[
            ('', 'Selecione...'),
            ('insuficiencia', 'Insuficiência Cardíaca'),
            ('outra', 'Outra'),
            ('nao_sabe', 'Não Sabe')
        ])

    # Problemas Renais
    tem_problema_rins = BooleanField('Tem ou Teve Problemas nos Rins?')
    tipo_problema_rins = SelectField('Se sim, qual?',
        choices=[
            ('', 'Selecione...'),
            ('insuficiencia', 'Insuficiência Renal'),
            ('outro', 'Outro'),
            ('nao_sabe', 'Não Sabe')
        ])

    # Outras Doenças
    hanseniase = BooleanField('Está com Hanseníase?')
    tuberculose = BooleanField('Está com Tuberculose?')
    cancer = BooleanField('Tem ou Teve Câncer?')

    # Situações de Saúde
    internacao_12_meses = BooleanField('Teve Alguma Internação nos Últimos 12 Meses?')
    problema_saude_mental = BooleanField('Teve Diagnóstico de Algum Problema de Saúde Mental por Profissional de Saúde?')
    acamado = BooleanField('Está Acamado?')
    domiciliado = BooleanField('Está Domiciliado?')

    # Práticas Integrativas
    usa_plantas_medicinais = BooleanField('Usa Plantas Medicinais?')
    usa_praticas_integrativas = BooleanField('Usa Outras Práticas Integrativas e Complementares?')

    # Outras Condições (hasta 3)
    outras_condicoes = StringField('Outras Condições de Saúde',
        validators=[Optional(), Length(max=300, message='Máximo de 300 caracteres')])

    # Situação de Rua
    situacao_rua = BooleanField('Está em Situação de Rua? *')
    
    tempo_rua = SelectField('Tempo em Situação de Rua?',
        choices=[
            ('', 'Selecione...'),
            ('menos_6', '< 6 meses'),
            ('6_12', '6 a 12 meses'),
            ('1_5', '1 a 5 anos'),
            ('mais_5', '> 5 anos')
        ])

    # Acompanhamento institucional
    acompanhado_instituicao = BooleanField('É Acompanhado por Outra Instituição?')
    qual_instituicao = StringField('Se sim, qual(is)?',
        validators=[Length(max=200, message='Máximo de 200 caracteres')])

    # Benefícios
    recebe_beneficio = BooleanField('Recebe Algum Benefício?')
    qual_beneficio = StringField('Se sim, qual(is)?',
        validators=[Length(max=200, message='Máximo de 200 caracteres')])

    # Referência Familiar
    possui_referencia_familiar = BooleanField('Possui Referência Familiar?')
    grau_parentesco = StringField('Se sim, qual é o Grau de Parentesco?',
        validators=[Length(max=100, message='Máximo de 100 caracteres')])

    # Visitas Familiares
    visita_familiar = BooleanField('Visita Algum Familiar com Frequência?')
    frequencia_visitas = SelectField('Se sim, indique qual(is)?',
        choices=[
            ('', 'Selecione...'),
            ('1_vez', '1 vez'),
            ('2_3_vezes', '2 ou 3 vezes'),
            ('mais_3', 'mais de 3 vezes')
        ])

    # Higiene
    acesso_higiene = BooleanField('Tem Acesso à Higiene Pessoal?')
    tipos_higiene = SelectField('Se sim, indique qual(is)?',
        choices=[
            ('', 'Selecione...'),
            ('banho', 'Banho'),
            ('sanitario', 'Sanitário'),
            ('higiene_bucal', 'Higiene Bucal'),
            ('outro', 'Outro')
        ])

    # Alimentação
    quantidade_alimentacao = StringField('Quantas Vezes se Alimenta ao Dia?',
        validators=[DataRequired(message='Informe a quantidade de alimentações diárias')])

    origem_alimentacao = SelectField('Qual a Origem da Alimentação?',
        choices=[
            ('', 'Selecione...'),
            ('restaurante_popular', 'Restaurante Popular'),
            ('doacao_restaurante', 'Doação Restaurante'),
            ('doacao_religiosa', 'Doação Grupo Religioso'),
            ('doacao_popular', 'Doação de Popular'),
            ('outras', 'Outras')
        ],
        validators=[DataRequired(message='Selecione a origem da alimentação')])

    # Campos de control (readonly/disabled)
    digitado_por = StringField('Digitado por')
    data_digitacao = StringField('Data')
    
    # Actualizar el campo microarea para incluir FA
    microarea = StringField('Microárea *', 
        render_kw={'readonly': True})

    # Agregar el campo de checkbox
    fora_area = BooleanField('Fora de Área')

    def validate_nome_mae(self, field):
        if not self.mae_desconhecida.data and not field.data:
            raise ValidationError('Nome da mãe é obrigatório quando não for desconhecido')

    def validate_nome_pai(self, field):
        if not self.pai_desconhecido.data and not field.data:
            raise ValidationError('Nome do pai é obrigatório quando não for desconhecido')

    def validate_municipio_nascimento(self, field):
        if self.nacionalidade.data == 'brasileira' and not field.data:
            raise ValidationError('Município de nascimento é obrigatório para brasileiros')

    def validate_uf_nascimento(self, field):
        if self.nacionalidade.data == 'brasileira' and not field.data:
            raise ValidationError('UF de nascimento é obrigatório para brasileiros')

    def validate_pais_nascimento(self, field):
        if self.nacionalidade.data in ['naturalizada', 'estrangeira'] and not field.data:
            raise ValidationError('País de nascimento é obrigatório para naturalizados e estrangeiros')

    def validate_data_naturalizacao(self, field):
        if self.nacionalidade.data == 'naturalizada' and not field.data:
            raise ValidationError('Data de naturalização é obrigatória para naturalizados')

    def validate_portaria_naturalizacao(self, field):
        if self.nacionalidade.data == 'naturalizada' and not field.data:
            raise ValidationError('Portaria de naturalização é obrigatória para naturalizados')

    def validate_data_entrada_brasil(self, field):
        if self.nacionalidade.data == 'estrangeira' and not field.data:
            raise ValidationError('Data de entrada no Brasil é obrigatória para estrangeiros')

    def validate_cns_cidadao(self, field):
        if not field.data and not self.cpf_cidadao.data:
            raise ValidationError('É necessário informar CNS ou CPF do cidadão')
            
    def validate_cns_responsavel(self, field):
        if not self.responsavel_familiar.data:
            if not field.data and not self.cpf_responsavel.data:
                raise ValidationError('É necessário informar CNS ou CPF do responsável familiar')

    # Validaciones adicionales
    def validate_qual_comunidade(self, field):
        if self.membro_comunidade.data and not field.data:
            raise ValidationError('Informe qual comunidade tradicional')

    def validate_orientacao_sexual(self, field):
        if self.informa_orientacao.data and not field.data:
            raise ValidationError('Selecione a orientação sexual')

    def validate_identidade_genero(self, field):
        if self.informa_identidade.data and not field.data:
            raise ValidationError('Selecione a identidade de gênero')

    def validate_deficiencias(self, field):
        if self.tem_deficiencia.data and not field.data:
            raise ValidationError('Selecione pelo menos uma deficiência')

    def validate_data_obito(self, field):
        if self.motivo_saida.data == 'obito' and not field.data:
            raise ValidationError('Data do óbito é obrigatória')

    def validate_numero_do(self, field):
        if self.motivo_saida.data == 'obito' and not field.data:
            raise ValidationError('Número da D.O. é obrigatório')

    def validate_maternidade_referencia(self, field):
        if self.esta_gestante.data and not field.data:
            raise ValidationError('Informe a maternidade de referência')

    def validate_tipo_doenca_respiratoria(self, field):
        if self.tem_doenca_respiratoria.data and not field.data:
            raise ValidationError('Selecione o tipo de doença respiratória')

    def validate_tipo_doenca_cardiaca(self, field):
        if self.tem_doenca_cardiaca.data and not field.data:
            raise ValidationError('Selecione o tipo de doença cardíaca')

    def validate_tipo_problema_rins(self, field):
        if self.tem_problema_rins.data and not field.data:
            raise ValidationError('Selecione o tipo de problema nos rins')

    def validate_tempo_rua(self, field):
        if self.situacao_rua.data and not field.data:
            raise ValidationError('Informe o tempo em situação de rua')

    def validate_qual_instituicao(self, field):
        if self.acompanhado_instituicao.data and not field.data:
            raise ValidationError('Informe qual(is) instituição(ões)')

    def validate_qual_beneficio(self, field):
        if self.recebe_beneficio.data and not field.data:
            raise ValidationError('Informe qual(is) benefício(s)')

    def validate_grau_parentesco(self, field):
        if self.possui_referencia_familiar.data and not field.data:
            raise ValidationError('Informe o grau de parentesco')

    def validate_frequencia_visitas(self, field):
        if self.visita_familiar.data and not field.data:
            raise ValidationError('Informe a frequência das visitas')

    def validate_tipos_higiene(self, field):
        if self.acesso_higiene.data and not field.data:
            raise ValidationError('Selecione pelo menos um tipo de higiene') 