from app import db
from datetime import datetime

class HealthCondition(db.Model):
    __tablename__ = 'condicoes_saude'
    
    id = db.Column(db.Integer, primary_key=True)
    cidadao_id = db.Column(db.Integer, db.ForeignKey('citizens.id'), nullable=False)
    data_registro = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Gestação
    gestante = db.Column(db.Boolean, nullable=False, default=False)
    maternidade_referencia = db.Column(db.String(100))
    
    # Peso
    peso_auto_referido = db.Column(db.String(20))  # 'Abaixo do Peso', 'Peso Adequado', 'Acima do Peso'
    
    # Doenças e Condições
    doenca_respiratoria = db.Column(db.Boolean, default=False)
    tipo_doenca_respiratoria = db.Column(db.String(20))  # 'Asma', 'DPOC/Enfisema', 'Outra', 'Não Sabe'
    
    fumante = db.Column(db.Boolean, default=False)
    uso_alcool = db.Column(db.Boolean, default=False)
    uso_outras_drogas = db.Column(db.Boolean, default=False)
    
    hipertensao_arterial = db.Column(db.Boolean, default=False)
    diabetes = db.Column(db.Boolean, default=False)
    teve_avc = db.Column(db.Boolean, default=False)
    teve_infarto = db.Column(db.Boolean, default=False)
    
    doenca_cardiaca = db.Column(db.Boolean, default=False)
    tipo_doenca_cardiaca = db.Column(db.String(30))  # 'Insuficiência Cardíaca', 'Outra', 'Não Sabe'
    
    problema_rins = db.Column(db.Boolean, default=False)
    tipo_problema_rins = db.Column(db.String(30))  # 'Insuficiência Renal', 'Outro', 'Não Sabe'
    
    hanseniase = db.Column(db.Boolean, default=False)
    tuberculose = db.Column(db.Boolean, default=False)
    cancer = db.Column(db.Boolean, default=False)
    
    internacao_12_meses = db.Column(db.Boolean, default=False)
    problema_saude_mental = db.Column(db.Boolean, default=False)
    acamado = db.Column(db.Boolean, default=False)
    domiciliado = db.Column(db.Boolean, default=False)
    
    plantas_medicinais = db.Column(db.Boolean, default=False)
    praticas_integrativas = db.Column(db.Boolean, default=False)
    
    # Outras condições (até 3)
    outras_condicoes = db.Column(db.String(300))
    
    def __repr__(self):
        return f'<CondicaoSaude {self.id} - Cidadão {self.cidadao_id}>' 