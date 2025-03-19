from faker import Faker
from datetime import datetime, timedelta
import random
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app, db
from app.models.cadastro_individual import CadastroIndividual
from app.models.user import User

fake = Faker('pt_BR')

def gerar_cadastro(admin_user):
    # Generar datos básicos
    sexo = random.choice(['M', 'F'])
    raca = random.choice(['branca', 'preta', 'parda', 'amarela', 'indigena'])
    
    # Generar datos para campos condicionales primero
    membro_comunidade = random.choice([True, False])
    informa_orientacao = random.choice([True, False])
    informa_identidade = random.choice([True, False])
    tem_deficiencia = random.choice([True, False])
    
    dados = {
        # Identificação
        'nome_completo': fake.name(),
        'nome_social': fake.name() if random.random() < 0.1 else None,  # 10% tienen nombre social
        'data_nascimento': fake.date_of_birth(minimum_age=1, maximum_age=90),
        'sexo': sexo,
        'raca_cor': raca,
        'etnia': fake.word() if raca == 'indigena' else None,
        'numero_nis': ''.join([str(random.randint(0, 9)) for _ in range(11)]) if random.random() < 0.3 else None,
        
        # Documentos
        'cns_cidadao': ''.join([str(random.randint(0, 9)) for _ in range(15)]),
        'cpf_cidadao': ''.join([str(random.randint(0, 9)) for _ in range(11)]) if random.random() < 0.8 else None,
        
        # Contato
        'telefone_celular': fake.phone_number(),
        'email': fake.email() if random.random() < 0.4 else None,
        
        # Filiação
        'nome_mae': fake.name_female() if random.random() < 0.9 else None,
        'mae_desconhecida': random.random() < 0.1,
        'nome_pai': fake.name_male() if random.random() < 0.7 else None,
        'pai_desconhecido': random.random() < 0.3,
        
        # Nacionalidade
        'nacionalidade': random.choice(['brasileira'] * 95 + ['naturalizado'] * 3 + ['estrangeiro'] * 2),
        'municipio_nascimento': fake.city() if random.random() < 0.95 else None,
        'uf_nascimento': random.choice(['SP', 'RJ', 'MG', 'RS', 'PR', 'BA']),
        
        # Dados Sociodemográficos
        'frequenta_escola': random.random() < 0.3,
        'curso_frequenta': random.choice(['fundamental_1_4', 'fundamental_5_8', 'medio', 'superior', 'nenhum']),
        'situacao_trabalho': random.choice(['empregador', 'assalariado_com_carteira', 'autonomo_com_previdencia', 'desempregado']),
        'ocupacao': fake.job() if random.random() < 0.7 else None,
        
        # Condições de Saúde
        'esta_gestante': random.random() < 0.1 and sexo == 'F',
        'hipertensao_arterial': random.random() < 0.2,
        'diabetes': random.random() < 0.1,
        'teve_avc': random.random() < 0.05,
        'teve_infarto': random.random() < 0.05,
        'tem_doenca_cardiaca': random.random() < 0.1,
        'tem_problema_rins': random.random() < 0.1,
        
        # Hábitos
        'fumante': random.random() < 0.15,
        'uso_alcool': random.random() < 0.2,
        'uso_drogas': random.random() < 0.05,
        
        # Datos del administrador/profesional
        'digitado_por': admin_user.nome_completo,
        'data_digitacao': datetime.now(),
        'cns_profissional': admin_user.cns,
        'cbo': admin_user.cbo,
        'cnes': admin_user.cnes,
        'ine': admin_user.ine,
        'microarea': 'FA' if random.random() < 0.1 else admin_user.microarea,
        'data_cadastro': datetime.now(),
        
        # Responsável Familiar
        'responsavel_familiar': random.random() < 0.3,  # 30% son responsables familiares
        'parentesco_responsavel': random.choice([
            'conjuge', 'filho', 'enteado', 'neto', 'pai', 
            'sogro', 'irmao', 'genro', 'outro_parente', 'nao_parente'
        ]),
        'cns_responsavel': ''.join([str(random.randint(0, 9)) for _ in range(15)]) if random.random() < 0.7 else None,
        'cpf_responsavel': ''.join([str(random.randint(0, 9)) for _ in range(11)]) if random.random() < 0.7 else None,
        
        # Situação de Rua
        'situacao_rua': random.random() < 0.05,  # 5% en situación de calle
        'tempo_rua': random.choice(['menos_6', '6_12', '1_5', 'mais_5']) if random.random() < 0.05 else None,
        
        # Alimentação
        'quantidade_alimentacao': str(random.randint(1, 5)),
        'origem_alimentacao': random.choice([
            'restaurante_popular', 'doacao_restaurante', 
            'doacao_religiosa', 'doacao_popular', 'outras'
        ]),
        
        # TRIA (campos obligatorios)
        'tria_alimentos_acabaram': random.choice([True, False]),
        'tria_comeu_alguns': random.choice([True, False]),
        
        # Campos de salud (obligatorios)
        'consideracao_peso': random.choice(['abaixo', 'adequado', 'acima']),
        'tem_doenca_respiratoria': random.choice([True, False]),
        'tipo_doenca_respiratoria': random.choice(['asma', 'dpoc', 'outra', 'nao_sabe']) if random.random() < 0.2 else None,
        
        # Campos booleanos obligatorios
        'frequenta_cuidador': random.choice([True, False]),
        'participa_grupo': random.choice([True, False]),
        'possui_plano_saude': random.choice([True, False]),
        'membro_comunidade': membro_comunidade,
        'informa_orientacao': informa_orientacao,
        'informa_identidade': informa_identidade,
        'tem_deficiencia': tem_deficiencia,
        'esta_gestante': random.choice([True, False]) if sexo == 'F' else False,
        'hipertensao_arterial': random.choice([True, False]),
        'diabetes': random.choice([True, False]),
        'teve_avc': random.choice([True, False]),
        'teve_infarto': random.choice([True, False]),
        'tem_doenca_cardiaca': random.choice([True, False]),
        'tem_problema_rins': random.choice([True, False]),
        'hanseniase': random.choice([True, False]),
        'tuberculose': random.choice([True, False]),
        'cancer': random.choice([True, False]),
        'internacao_12_meses': random.choice([True, False]),
        'problema_saude_mental': random.choice([True, False]),
        'acamado': random.choice([True, False]),
        'domiciliado': random.choice([True, False]),
        'usa_plantas_medicinais': random.choice([True, False]),
        'usa_praticas_integrativas': random.choice([True, False]),
        'situacao_rua': random.choice([True, False]),
        'acompanhado_instituicao': random.choice([True, False]),
        'recebe_beneficio': random.choice([True, False]),
        'possui_referencia_familiar': random.choice([True, False]),
        'visita_familiar': random.choice([True, False]),
        'acesso_higiene': random.choice([True, False]),

        # Campos condicionales
        'qual_comunidade': fake.word() if membro_comunidade else None,
        'orientacao_sexual': random.choice(['heterossexual', 'homossexual', 'bissexual']) if informa_orientacao else None,
        'identidade_genero': random.choice(['homem', 'mulher', 'outro']) if informa_identidade else None,
        'deficiencias': 'visual,auditiva,fisica' if tem_deficiencia else None,
        'maternidade_referencia': fake.company() if random.random() < 0.2 else None,
        'tipo_doenca_cardiaca': random.choice(['insuficiencia', 'outra', 'nao_sabe']) if random.random() < 0.2 else None,
        'tipo_problema_rins': random.choice(['insuficiencia', 'outro', 'nao_sabe']) if random.random() < 0.2 else None,
        'outras_condicoes': 'condição1,condição2' if random.random() < 0.2 else None,
        'qual_instituicao': fake.company() if random.random() < 0.2 else None,
        'qual_beneficio': 'Bolsa Família' if random.random() < 0.2 else None,
        'grau_parentesco': random.choice(['pai', 'mae', 'irmao']) if random.random() < 0.2 else None,
        'frequencia_visitas': random.choice(['1_vez', '2_3_vezes', 'mais_3']) if random.random() < 0.2 else None,
        'tipos_higiene': 'banho,sanitario' if random.random() < 0.2 else None,
    }
    
    return dados

def criar_cadastros(quantidade=100):
    app = create_app()
    with app.app_context():
        # Primero actualizamos los datos del admin
        admin = User.query.filter_by(username='admin').first()
        if not admin:
            print("Error: Usuario administrador no encontrado")
            return
        
        # Actualizar datos del admin como ACS
        admin.nome_completo = "Administrador do Sistema"
        admin.cns = "123456789012345"  # CNS de 15 dígitos
        admin.cbo = "515105"  # Código CBO para ACS
        admin.cnes = "1234567"  # CNES de 7 dígitos
        admin.ine = "1234567890"  # INE de 10 dígitos
        admin.microarea = "01"  # Microárea del ACS
        db.session.commit()
        
        # Luego generamos los cadastros
        for i in range(quantidade):
            dados = gerar_cadastro(admin)
            cadastro = CadastroIndividual(**dados)
            db.session.add(cadastro)
            if (i + 1) % 10 == 0:
                print(f'Generados {i + 1} cadastros...')
        
        db.session.commit()
        print(f'{quantidade} cadastros gerados com sucesso!')

def gerar_cadastros_teste(quantidade=10):
    app = create_app()
    with app.app_context():
        # Generar cadastros de prueba...
        for i in range(quantidade):
            cadastro = CadastroIndividual(
                nome_completo=f"Pessoa Teste {i+1}",
                data_nascimento=datetime.now() - timedelta(days=365*random.randint(1,80)),
                # ... otros campos
            )
            db.session.add(cadastro)
        db.session.commit()

if __name__ == '__main__':
    criar_cadastros(quantidade=100) 