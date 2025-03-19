from flask import Blueprint, render_template, redirect, url_for, flash, request
from app.models.cadastro_individual import CadastroIndividual
from app.forms.cadastro_forms import CadastroIndividualForm
from app import db
from flask_login import login_required, current_user
from datetime import datetime
from app.models.historico_cadastro import HistoricoCadastro

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
            if form.acesso_higiene.data and form.tipos_higiene.data:
                cadastro.tipos_higiene = ','.join(form.tipos_higiene.data)
            else:
                cadastro.tipos_higiene = None
            
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

@bp.route('/cadastros', methods=['GET'])
@login_required
def lista_cadastros():
    cadastros = CadastroIndividual.query.all()
    return render_template('cadastro/lista.html', cadastros=cadastros)

@bp.route('/cadastro/<int:id>', methods=['GET'])
@login_required
def ver_cadastro(id):
    cadastro = CadastroIndividual.query.get_or_404(id)
    return render_template('cadastro/ver.html', cadastro=cadastro)

@bp.route('/cadastro/<int:id>/editar', methods=['GET', 'POST'])
@login_required
def editar_cadastro(id):
    cadastro = CadastroIndividual.query.get_or_404(id)
    form = CadastroIndividualForm()
    
    # Datos del profesional
    dados_profissional = {
        'cns_profissional': current_user.cns,
        'cbo': current_user.cbo,
        'cnes': current_user.cnes,
        'ine': current_user.ine,
        'microarea': current_user.microarea,
        'data_cadastro': datetime.now().strftime('%d/%m/%Y')
    }
    
    # Historial de modificaciones
    historico = HistoricoCadastro.query.filter_by(cadastro_id=id).order_by(HistoricoCadastro.data_modificacao.desc()).all()
    
    if request.method == 'GET':
        form.nome_completo.data = cadastro.nome_completo
        form.nome_social.data = cadastro.nome_social
        form.data_nascimento.data = cadastro.data_nascimento.strftime('%d/%m/%Y')
        form.sexo.data = cadastro.sexo
        form.raca_cor.data = cadastro.raca_cor
        form.etnia.data = cadastro.etnia
        form.numero_nis.data = cadastro.numero_nis
        
        # Datos de los padres
        form.nome_mae.data = cadastro.nome_mae
        form.mae_desconhecida.data = cadastro.mae_desconhecida
        form.nome_pai.data = cadastro.nome_pai
        form.pai_desconhecido.data = cadastro.pai_desconhecido
        
        # Nacionalidad y nacimiento
        form.nacionalidade.data = cadastro.nacionalidade
        form.pais_nascimento.data = cadastro.pais_nascimento
        if cadastro.data_naturalizacao:
            form.data_naturalizacao.data = cadastro.data_naturalizacao.strftime('%d/%m/%Y')
        form.portaria_naturalizacao.data = cadastro.portaria_naturalizacao
        form.municipio_nascimento.data = cadastro.municipio_nascimento
        form.uf_nascimento.data = cadastro.uf_nascimento
        if cadastro.data_entrada_brasil:
            form.data_entrada_brasil.data = cadastro.data_entrada_brasil.strftime('%d/%m/%Y')

        # Contacto
        form.telefone_celular.data = cadastro.telefone_celular
        form.email.data = cadastro.email

        # Identificación
        form.cns_cidadao.data = cadastro.cns_cidadao
        form.cpf_cidadao.data = cadastro.cpf_cidadao
        form.responsavel_familiar.data = cadastro.responsavel_familiar
        form.cns_responsavel.data = cadastro.cns_responsavel
        form.cpf_responsavel.data = cadastro.cpf_responsavel

        # Campos sociodemográficos
        form.parentesco_responsavel.data = cadastro.parentesco_responsavel
        form.frequenta_escola.data = cadastro.frequenta_escola
        form.curso_frequenta.data = cadastro.curso_frequenta
        form.situacao_trabalho.data = cadastro.situacao_trabalho
        form.ocupacao.data = cadastro.ocupacao
        form.crianca_ficacom.data = cadastro.crianca_ficacom
        form.frequenta_cuidador.data = cadastro.frequenta_cuidador
        form.participa_grupo.data = cadastro.participa_grupo
        form.possui_plano_saude.data = cadastro.possui_plano_saude

        # Comunidade Tradicional
        form.membro_comunidade.data = cadastro.membro_comunidade
        if cadastro.membro_comunidade:
            form.qual_comunidade.data = cadastro.qual_comunidade

        # Orientación Sexual e Identidad de Género
        form.informa_orientacao.data = cadastro.informa_orientacao
        if cadastro.informa_orientacao:
            form.orientacao_sexual.data = cadastro.orientacao_sexual

        # Identidade de Gênero
        form.informa_identidade.data = cadastro.informa_identidade
        if cadastro.informa_identidade:
            form.identidade_genero.data = cadastro.identidade_genero

        # Deficiência
        form.tem_deficiencia.data = cadastro.tem_deficiencia
        if cadastro.tem_deficiencia:
            form.deficiencias.data = cadastro.deficiencias

        # Saída do Cadastro
        form.motivo_saida.data = cadastro.motivo_saida
        if cadastro.data_obito:
            form.data_obito.data = cadastro.data_obito.strftime('%d/%m/%Y')
        form.numero_do.data = cadastro.numero_do

        # TRIA
        form.tria_alimentos_acabaram.data = cadastro.tria_alimentos_acabaram
        form.tria_comeu_alguns.data = cadastro.tria_comeu_alguns
        form.consideracao_peso.data = cadastro.consideracao_peso

        # Doença Respiratória
        form.tem_doenca_respiratoria.data = cadastro.tem_doenca_respiratoria
        form.tipo_doenca_respiratoria.data = cadastro.tipo_doenca_respiratoria

        # Hábitos
        form.fumante.data = cadastro.fumante
        form.uso_alcool.data = cadastro.uso_alcool
        form.uso_drogas.data = cadastro.uso_drogas

        # Doenças Crônicas
        form.hipertensao_arterial.data = cadastro.hipertensao_arterial
        form.diabetes.data = cadastro.diabetes
        form.teve_avc.data = cadastro.teve_avc
        form.teve_infarto.data = cadastro.teve_infarto
        form.tem_doenca_cardiaca.data = cadastro.tem_doenca_cardiaca
        form.tipo_doenca_cardiaca.data = cadastro.tipo_doenca_cardiaca

        # Problemas Renais
        form.tem_problema_rins.data = cadastro.tem_problema_rins
        form.tipo_problema_rins.data = cadastro.tipo_problema_rins

        # Outras Doenças
        form.hanseniase.data = cadastro.hanseniase
        form.tuberculose.data = cadastro.tuberculose
        form.cancer.data = cadastro.cancer

        # Situações de Saúde
        form.internacao_12_meses.data = cadastro.internacao_12_meses
        form.problema_saude_mental.data = cadastro.problema_saude_mental
        form.acamado.data = cadastro.acamado
        form.domiciliado.data = cadastro.domiciliado

        # Práticas Integrativas
        form.usa_plantas_medicinais.data = cadastro.usa_plantas_medicinais
        form.usa_praticas_integrativas.data = cadastro.usa_praticas_integrativas
        form.outras_condicoes.data = cadastro.outras_condicoes

        # Situação de Rua
        form.situacao_rua.data = cadastro.situacao_rua
        form.tempo_rua.data = cadastro.tempo_rua
        form.acompanhado_instituicao.data = cadastro.acompanhado_instituicao
        form.qual_instituicao.data = cadastro.qual_instituicao
        form.recebe_beneficio.data = cadastro.recebe_beneficio
        form.qual_beneficio.data = cadastro.qual_beneficio
        form.possui_referencia_familiar.data = cadastro.possui_referencia_familiar
        form.grau_parentesco.data = cadastro.grau_parentesco
        form.visita_familiar.data = cadastro.visita_familiar
        form.frequencia_visitas.data = cadastro.frequencia_visitas

        # Higiene
        form.acesso_higiene.data = cadastro.acesso_higiene
        if cadastro.acesso_higiene:
            form.tipos_higiene.data = cadastro.tipos_higiene
        form.quantidade_alimentacao.data = cadastro.quantidade_alimentacao
        form.origem_alimentacao.data = cadastro.origem_alimentacao
        
        # Pre-llenar microarea
        form.microarea.data = cadastro.microarea
    
    if form.validate_on_submit():
        try:
            # Registrar en el histórico
            historico = HistoricoCadastro(
                cadastro_id=cadastro.id,
                modificado_por=current_user.nome_completo,
                descricao=f"Cadastro atualizado por {current_user.nome_completo}"
            )
            db.session.add(historico)
            
            # Actualizar campos básicos
            cadastro.nome_completo = form.nome_completo.data
            cadastro.nome_social = form.nome_social.data
            cadastro.data_nascimento = datetime.strptime(form.data_nascimento.data, '%d/%m/%Y')
            cadastro.sexo = form.sexo.data
            cadastro.raca_cor = form.raca_cor.data
            cadastro.etnia = form.etnia.data
            cadastro.numero_nis = form.numero_nis.data

            # Datos de los padres
            if form.mae_desconhecida.data:
                cadastro.nome_mae = 'Desconhecido'
            else:
                cadastro.nome_mae = form.nome_mae.data
            cadastro.mae_desconhecida = form.mae_desconhecida.data

            if form.pai_desconhecido.data:
                cadastro.nome_pai = 'Desconhecido'
            else:
                cadastro.nome_pai = form.nome_pai.data
            cadastro.pai_desconhecido = form.pai_desconhecido.data

            # Nacionalidad y nacimiento
            cadastro.nacionalidade = form.nacionalidade.data
            cadastro.pais_nascimento = form.pais_nascimento.data
            if form.data_naturalizacao.data:
                cadastro.data_naturalizacao = datetime.strptime(form.data_naturalizacao.data, '%d/%m/%Y')
            cadastro.portaria_naturalizacao = form.portaria_naturalizacao.data
            cadastro.municipio_nascimento = form.municipio_nascimento.data
            cadastro.uf_nascimento = form.uf_nascimento.data
            if form.data_entrada_brasil.data:
                cadastro.data_entrada_brasil = datetime.strptime(form.data_entrada_brasil.data, '%d/%m/%Y')

            # Contacto
            cadastro.telefone_celular = form.telefone_celular.data
            cadastro.email = form.email.data

            # Identificación
            cadastro.cns_cidadao = form.cns_cidadao.data
            cadastro.cpf_cidadao = form.cpf_cidadao.data
            cadastro.responsavel_familiar = form.responsavel_familiar.data
            cadastro.cns_responsavel = form.cns_responsavel.data
            cadastro.cpf_responsavel = form.cpf_responsavel.data

            # Campos sociodemográficos
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
            
            # Orientación Sexual e Identidad de Género
            cadastro.informa_orientacao = form.informa_orientacao.data
            cadastro.orientacao_sexual = form.orientacao_sexual.data if form.informa_orientacao.data else None
            
            # Identidade de Gênero
            cadastro.informa_identidade = form.informa_identidade.data
            cadastro.identidade_genero = form.identidade_genero.data if form.informa_identidade.data else None
            
            # Deficiência
            cadastro.tem_deficiencia = form.tem_deficiencia.data
            if form.tem_deficiencia.data:
                cadastro.deficiencias = form.deficiencias.data
            else:
                cadastro.deficiencias = None
            
            # Saída do Cadastro
            cadastro.motivo_saida = form.motivo_saida.data
            if cadastro.data_obito:
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
            else:
                cadastro.tipos_higiene = None
            
            # Alimentação
            cadastro.quantidade_alimentacao = form.quantidade_alimentacao.data
            cadastro.origem_alimentacao = form.origem_alimentacao.data
            
            # Actualizar microarea
            cadastro.microarea = form.microarea.data
            
            db.session.commit()
            flash('Cadastro atualizado com sucesso!', 'success')
            return redirect(url_for('cadastro.lista_cadastros'))
            
        except Exception as e:
            db.session.rollback()
            flash('Ocorreu um erro ao salvar o cadastro.', 'danger')
    else:
        # Mejorar los mensajes de error
        for field, errors in form.errors.items():
            field_label = getattr(form, field).label.text
            for error in errors:
                # Traducir mensajes de error comunes
                if error == 'This field is required.':
                    error = 'Este campo é obrigatório'
                elif error == 'Invalid value':
                    error = 'Valor inválido'
                
                flash(f'{field_label}: {error}', 'danger')
    
    return render_template('cadastro/form.html', 
                         form=form, 
                         cadastro=cadastro,
                         dados_profissional=dados_profissional,
                         historico=historico)

@bp.route('/cadastro/<int:id>/excluir', methods=['GET'])
@login_required
def excluir_cadastro(id):
    cadastro = CadastroIndividual.query.get_or_404(id)
    db.session.delete(cadastro)
    db.session.commit()
    flash('Cadastro excluído com sucesso!', 'success')
    return redirect(url_for('cadastro.lista_cadastros')) 