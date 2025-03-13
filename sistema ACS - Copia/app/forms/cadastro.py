from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, DateField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, Optional, Email, ValidationError
from app.models.constants import *

class CadastroIndividualForm(FlaskForm):
    # Identificação do Cidadão
    nome_completo = StringField('Nome Completo', validators=[DataRequired(), Length(min=3, max=70)])
    nome_social = StringField('Nome Social', validators=[Optional(), Length(max=70)])
    data_nascimento = DateField('Data de Nascimento', validators=[DataRequired()])
    sexo = SelectField('Sexo', choices=SEXO_CHOICES, validators=[DataRequired()])
    raca_cor = SelectField('Raça/Cor', choices=RACA_COR_CHOICES, validators=[DataRequired()])
    etnia = StringField('Etnia', validators=[Optional(), Length(max=50)])
    nacionalidade = SelectField('Nacionalidade', choices=NACIONALIDADE_CHOICES, validators=[DataRequired()])
    
    # Documentos
    cns = StringField('CNS', validators=[Optional(), Length(15)])
    cpf = StringField('CPF', validators=[Optional(), Length(11)])
    numero_nis = StringField('NIS/PIS/PASEP', validators=[Optional(), Length(11)])
    
    # Filiação
    nome_mae = StringField('Nome da Mãe', validators=[Optional(), Length(max=70)])
    desconhece_nome_mae = BooleanField('Não Sei o Nome da Mãe')
    nome_pai = StringField('Nome do Pai', validators=[Optional(), Length(max=70)])
    desconhece_nome_pai = BooleanField('Não Sei o Nome do Pai')
    
    # Naturalização
    data_naturalizacao = DateField('Data de Naturalização', validators=[Optional()])
    portaria_naturalizacao = StringField('Portaria de Naturalização', validators=[Optional(), Length(max=16)])
    data_entrada_brasil = DateField('Data de Entrada no Brasil', validators=[Optional()])
    pais_nascimento = SelectField('País de Nascimento', validators=[Optional()])
    
    # Contato
    email = StringField('Email', validators=[Optional(), Email(), Length(max=100)])
    telefone = StringField('Telefone', validators=[Optional(), Length(min=10, max=11)])
    
    # Localização
    municipio_nascimento = StringField('Município de Nascimento', validators=[Optional(), Length(7)])
    microarea = StringField('Microárea', validators=[Optional(), Length(2)])
    st_fora_area = BooleanField('Fora de Área')
    
    # Responsável Familiar
    status_eh_responsavel = BooleanField('É Responsável Familiar')
    cns_responsavel = StringField('CNS do Responsável', validators=[Optional(), Length(15)])
    cpf_responsavel = StringField('CPF do Responsável', validators=[Optional(), Length(11)])

    # Informações Sociodemográficas
    frequenta_escola = BooleanField('Frequenta Escola')
    curso_mais_elevado = SelectField('Curso Mais Elevado', choices=CURSO_CHOICES)
    situacao_trabalho = SelectField('Situação de Trabalho', choices=SITUACAO_TRABALHO_CHOICES)
    ocupacao_codigo_cbo2002 = StringField('CBO', validators=[Optional(), Length(6)])
    
    # Orientação Sexual e Identidade de Gênero
    status_deseja_informar_orientacao_sexual = BooleanField('Deseja Informar Orientação Sexual')
    orientacao_sexual = SelectField('Orientação Sexual', choices=ORIENTACAO_SEXUAL_CHOICES)
    status_deseja_informar_identidade_genero = BooleanField('Deseja Informar Identidade de Gênero')
    identidade_genero = SelectField('Identidade de Gênero', choices=IDENTIDADE_GENERO_CHOICES)
    
    # Deficiência
    status_tem_deficiencia = BooleanField('Possui Deficiência')
    deficiencias = SelectField('Tipo de Deficiência', choices=DEFICIENCIA_CHOICES)
    
    # Condições de Saúde
    status_eh_gestante = BooleanField('É Gestante')
    maternidade_referencia = StringField('Maternidade de Referência', validators=[Optional(), Length(max=100)])
    status_tem_hipertensao = BooleanField('Tem Hipertensão')
    status_tem_diabetes = BooleanField('Tem Diabetes')
    
    # Situação de Rua
    status_situacao_rua = BooleanField('Em Situação de Rua')
    tempo_rua = SelectField('Tempo em Situação de Rua', choices=TEMPO_RUA_CHOICES)
    
    submit = SubmitField('Salvar')

    def validate_cpf(self, field):
        if field.data and not self.cns.data:
            # Aqui iría la validación del CPF
            pass

    def validate_cns(self, field):
        if field.data and not self.cpf.data:
            # Aqui iría la validación del CNS
            pass 