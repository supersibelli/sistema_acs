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
    
    nacionalidade = SelectField('Nacionalidade',
                              choices=[('', 'Selecione...'),
                                      ('brasileira', 'Brasileira'),
                                      ('naturalizado', 'Naturalizado'),
                                      ('estrangeiro', 'Estrangeiro')],
                              validators=[DataRequired(message="Nacionalidade é obrigatória")])
    
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
                                 validators=[Optional(),
                                           Regexp(r'^\d{11}$',
                                                  message="Digite apenas os números, 11 dígitos")])
    
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
    frequenta_escola = BooleanField('Frequenta Escola ou Creche?')

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
    deficiencias = SelectMultipleField('Deficiências',
        choices=[
            ('auditiva', 'Auditiva'),
            ('intelectual', 'Intelectual/Cognitiva'),
            ('visual', 'Visual'),
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
        if self.nacionalidade.data in ['naturalizado', 'estrangeiro'] and not field.data:
            raise ValidationError('País de nascimento é obrigatório para naturalizados e estrangeiros')

    def validate_data_naturalizacao(self, field):
        if self.nacionalidade.data == 'naturalizado' and not field.data:
            raise ValidationError('Data de naturalização é obrigatória para naturalizados')

    def validate_portaria_naturalizacao(self, field):
        if self.nacionalidade.data == 'naturalizado' and not field.data:
            raise ValidationError('Portaria de naturalização é obrigatória para naturalizados')

    def validate_data_entrada_brasil(self, field):
        if self.nacionalidade.data == 'estrangeiro' and not field.data:
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