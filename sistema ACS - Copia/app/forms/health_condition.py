from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Optional, Length
from app.models.constants import (PESO_CHOICES, DOENCA_RESPIRATORIA_CHOICES,
                                DOENCA_CARDIACA_CHOICES, PROBLEMA_RINS_CHOICES)

class HealthConditionForm(FlaskForm):
    # Gestação
    gestante = BooleanField('Está Gestante?')
    maternidade_referencia = StringField('Qual é a Maternidade de Referência?',
                                       validators=[Optional(), Length(max=100)])
    
    # Peso
    peso_auto_referido = SelectField('Sobre seu peso, você se considera?',
                                    choices=PESO_CHOICES,
                                    validators=[DataRequired()])
    
    # Doenças e Condições
    doenca_respiratoria = BooleanField('Tem doença respiratória/no pulmão?')
    tipo_doenca_respiratoria = SelectField('Se sim, qual?',
                                         choices=DOENCA_RESPIRATORIA_CHOICES,
                                         validators=[Optional()])
    
    fumante = BooleanField('Está fumante?')
    uso_alcool = BooleanField('Faz uso de álcool?')
    uso_outras_drogas = BooleanField('Faz uso de outras drogas?')
    
    hipertensao_arterial = BooleanField('Tem hipertensão arterial?')
    diabetes = BooleanField('Tem diabetes?')
    teve_avc = BooleanField('Teve AVC/Derrame?')
    teve_infarto = BooleanField('Teve infarto?')
    
    doenca_cardiaca = BooleanField('Tem doença cardíaca/do coração?')
    tipo_doenca_cardiaca = SelectField('Se sim, qual?',
                                     choices=DOENCA_CARDIACA_CHOICES,
                                     validators=[Optional()])
    
    problema_rins = BooleanField('Tem ou teve problemas nos rins?')
    tipo_problema_rins = SelectField('Se sim, qual?',
                                   choices=PROBLEMA_RINS_CHOICES,
                                   validators=[Optional()])
    
    hanseniase = BooleanField('Está com hanseníase?')
    tuberculose = BooleanField('Está com tuberculose?')
    cancer = BooleanField('Tem ou teve câncer?')
    
    internacao_12_meses = BooleanField('Teve alguma internação nos últimos 12 meses?')
    problema_saude_mental = BooleanField('Teve diagnóstico de algum problema de saúde mental por profissional de saúde?')
    acamado = BooleanField('Está acamado?')
    domiciliado = BooleanField('Está domiciliado?')
    
    plantas_medicinais = BooleanField('Usa plantas medicinais?')
    praticas_integrativas = BooleanField('Usa outras práticas integrativas e complementares?')
    
    outras_condicoes = TextAreaField('Outras condições de saúde',
                                   validators=[Optional(), Length(max=300)]) 