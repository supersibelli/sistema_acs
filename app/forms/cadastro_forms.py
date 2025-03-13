from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, EmailField, BooleanField
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