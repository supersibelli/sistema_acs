from flask import Blueprint, render_template, redirect, url_for, flash, request
from app.models.cadastro_individual import CadastroIndividual
from app.forms.cadastro_forms import CadastroIndividualForm
from app import db
from flask_login import login_required, current_user
from datetime import datetime

bp = Blueprint('cadastro', __name__)

@bp.route('/cadastro/novo', methods=['GET', 'POST'])
@login_required
def novo_cadastro():
    form = CadastroIndividualForm()
    
    # Pre-llenar campos
    if request.method == 'GET':
        form.digitado_por.data = current_user.nome_completo
        form.data_digitacao.data = datetime.now().strftime('%d/%m/%Y')
        form.microarea.data = current_user.microarea  # Prellenar con la microárea del ACS
    
    # Pre-llenar datos del profesional desde el usuario logueado
    dados_profissional = {
        'cns_profissional': current_user.cns,
        'cbo': current_user.cbo,
        'cnes': current_user.cnes,
        'ine': current_user.ine,
        'microarea': current_user.microarea,
        'data_cadastro': datetime.now().strftime('%d/%m/%Y')
    }
    
    if form.validate_on_submit():
        try:
            cadastro = CadastroIndividual()
            cadastro.digitado_por = current_user.nome_completo
            cadastro.data_digitacao = datetime.now()
            # Si está marcado fora_area, usar 'FA', sino usar la microárea del ACS
            cadastro.microarea = 'FA' if form.fora_area.data else current_user.microarea
            
            # Manejar campos de fecha
            if form.data_nascimento.data:
                cadastro.data_nascimento = datetime.strptime(form.data_nascimento.data, '%d/%m/%Y').date()
            if form.data_naturalizacao.data:
                cadastro.data_naturalizacao = datetime.strptime(form.data_naturalizacao.data, '%d/%m/%Y').date()
            if form.data_entrada_brasil.data:
                cadastro.data_entrada_brasil = datetime.strptime(form.data_entrada_brasil.data, '%d/%m/%Y').date()
            
            # Manejar campos de padres desconocidos
            if form.mae_desconhecida.data:
                cadastro.nome_mae = 'Desconhecido'
            elif form.nome_mae.data:  # Solo asignar si hay datos
                cadastro.nome_mae = form.nome_mae.data
            else:
                cadastro.nome_mae = None  # Esto debería disparar la validación del formulario

            if form.pai_desconhecido.data:
                cadastro.nome_pai = 'Desconhecido'
            elif form.nome_pai.data:  # Solo asignar si hay datos
                cadastro.nome_pai = form.nome_pai.data
            else:
                cadastro.nome_pai = None

            # Copiar el resto de los campos
            for field in ['nome_completo', 'nome_social', 'sexo', 'raca_cor', 'etnia', 
                         'numero_nis', 'nacionalidade', 'pais_nascimento', 
                         'portaria_naturalizacao', 'municipio_nascimento', 
                         'uf_nascimento', 'telefone_celular', 'email']:
                setattr(cadastro, field, getattr(form, field).data)

            cadastro.mae_desconhecida = form.mae_desconhecida.data
            cadastro.pai_desconhecido = form.pai_desconhecido.data
            
            # Agregar datos del profesional
            cadastro.cns_profissional = current_user.cns
            cadastro.cbo = current_user.cbo
            cadastro.cnes = current_user.cnes
            cadastro.ine = current_user.ine
            cadastro.data_cadastro = datetime.now()
            
            # Agregar campos del ciudadano
            cadastro.cns_cidadao = form.cns_cidadao.data
            cadastro.cpf_cidadao = form.cpf_cidadao.data
            cadastro.responsavel_familiar = form.responsavel_familiar.data
            cadastro.cns_responsavel = form.cns_responsavel.data
            cadastro.cpf_responsavel = form.cpf_responsavel.data
            
            # Agregar campos sociodemográficos
            cadastro.parentesco_responsavel = form.parentesco_responsavel.data
            cadastro.frequenta_escola = form.frequenta_escola.data
            cadastro.curso_frequenta = form.curso_frequenta.data
            cadastro.situacao_trabalho = form.situacao_trabalho.data
            cadastro.ocupacao = form.ocupacao.data
            cadastro.crianca_ficacom = form.crianca_ficacom.data
            cadastro.frequenta_cuidador = form.frequenta_cuidador.data
            cadastro.participa_grupo = form.participa_grupo.data
            cadastro.possui_plano_saude = form.possui_plano_saude.data
            
            # Comunidade Tradicional
            cadastro.membro_comunidade = form.membro_comunidade.data
            cadastro.qual_comunidade = form.qual_comunidade.data if form.membro_comunidade.data else None
            
            # Orientação Sexual
            cadastro.informa_orientacao = form.informa_orientacao.data
            cadastro.orientacao_sexual = form.orientacao_sexual.data if form.informa_orientacao.data else None
            
            # Identidade de Gênero
            cadastro.informa_identidade = form.informa_identidade.data
            cadastro.identidade_genero = form.identidade_genero.data if form.informa_identidade.data else None
            
            # Deficiência
            cadastro.tem_deficiencia = form.tem_deficiencia.data
            if form.tem_deficiencia.data and form.deficiencias.data:
                cadastro.deficiencias = ','.join(form.deficiencias.data)
            else:
                cadastro.deficiencias = None
            
            # Saída do Cadastro
            cadastro.motivo_saida = form.motivo_saida.data
            if form.motivo_saida.data == 'obito':
                cadastro.data_obito = datetime.strptime(form.data_obito.data, '%d/%m/%Y').date()
                cadastro.numero_do = form.numero_do.data
            
            # TRIA
            cadastro.tria_alimentos_acabaram = form.tria_alimentos_acabaram.data
            cadastro.tria_comeu_alguns = form.tria_comeu_alguns.data
            
            # Condições/Situações de Saúde
            cadastro.esta_gestante = form.esta_gestante.data
            cadastro.maternidade_referencia = form.maternidade_referencia.data if form.esta_gestante.data else None
            
            cadastro.consideracao_peso = form.consideracao_peso.data
            
            # Doença Respiratória
            cadastro.tem_doenca_respiratoria = form.tem_doenca_respiratoria.data
            cadastro.tipo_doenca_respiratoria = form.tipo_doenca_respiratoria.data if form.tem_doenca_respiratoria.data else None
            
            # Hábitos
            cadastro.fumante = form.fumante.data
            cadastro.uso_alcool = form.uso_alcool.data
            cadastro.uso_drogas = form.uso_drogas.data
            
            # Doenças Crônicas
            cadastro.hipertensao_arterial = form.hipertensao_arterial.data
            cadastro.diabetes = form.diabetes.data
            cadastro.teve_avc = form.teve_avc.data
            cadastro.teve_infarto = form.teve_infarto.data
            
            # Doença Cardíaca
            cadastro.tem_doenca_cardiaca = form.tem_doenca_cardiaca.data
            cadastro.tipo_doenca_cardiaca = form.tipo_doenca_cardiaca.data if form.tem_doenca_cardiaca.data else None
            
            # Problemas Renais
            cadastro.tem_problema_rins = form.tem_problema_rins.data
            cadastro.tipo_problema_rins = form.tipo_problema_rins.data if form.tem_problema_rins.data else None
            
            # Outras Doenças
            cadastro.hanseniase = form.hanseniase.data
            cadastro.tuberculose = form.tuberculose.data
            cadastro.cancer = form.cancer.data
            
            # Situações de Saúde
            cadastro.internacao_12_meses = form.internacao_12_meses.data
            cadastro.problema_saude_mental = form.problema_saude_mental.data
            cadastro.acamado = form.acamado.data
            cadastro.domiciliado = form.domiciliado.data
            
            # Práticas Integrativas
            cadastro.usa_plantas_medicinais = form.usa_plantas_medicinais.data
            cadastro.usa_praticas_integrativas = form.usa_praticas_integrativas.data
            
            # Outras Condições
            cadastro.outras_condicoes = form.outras_condicoes.data
            
            # Situação de Rua
            cadastro.situacao_rua = form.situacao_rua.data
            if form.situacao_rua.data:
                cadastro.tempo_rua = form.tempo_rua.data
            
            # Acompanhamento institucional
            cadastro.acompanhado_instituicao = form.acompanhado_instituicao.data
            if form.acompanhado_instituicao.data:
                cadastro.qual_instituicao = form.qual_instituicao.data
            
            # Benefícios
            cadastro.recebe_beneficio = form.recebe_beneficio.data
            if form.recebe_beneficio.data:
                cadastro.qual_beneficio = form.qual_beneficio.data
            
            # Referência Familiar
            cadastro.possui_referencia_familiar = form.possui_referencia_familiar.data
            if form.possui_referencia_familiar.data:
                cadastro.grau_parentesco = form.grau_parentesco.data
            
            # Visitas Familiares
            cadastro.visita_familiar = form.visita_familiar.data
            if form.visita_familiar.data:
                cadastro.frequencia_visitas = form.frequencia_visitas.data
            
            # Higiene
            cadastro.acesso_higiene = form.acesso_higiene.data
            if form.acesso_higiene.data:
                cadastro.tipos_higiene = form.tipos_higiene.data
            
            # Alimentação
            cadastro.quantidade_alimentacao = form.quantidade_alimentacao.data
            cadastro.origem_alimentacao = form.origem_alimentacao.data
            
            db.session.add(cadastro)
            db.session.commit()
            flash('Cadastro realizado com sucesso!', 'success')
            return redirect(url_for('cadastro.lista_cadastros'))
            
        except Exception as e:
            db.session.rollback()
            flash('Erro ao salvar o cadastro. Por favor, verifique os dados e tente novamente.', 'danger')
            print(f"Erro: {str(e)}")
    
    if form.errors:
        flash('Por favor, corrija os erros no formulário.', 'danger')
        
    return render_template('cadastro/form.html', form=form, dados_profissional=dados_profissional)

@bp.route('/cadastros')
@login_required
def lista_cadastros():
    cadastros = CadastroIndividual.query.all()
    return render_template('cadastro/lista.html', cadastros=cadastros) 