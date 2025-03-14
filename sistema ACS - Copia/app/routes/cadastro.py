from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_required, current_user
from app import db
from app.models import CadastroIndividual, InfoSociodemografica, CondicoesSaude, SituacaoRua
from app.forms.cadastro import CadastroIndividualForm
import uuid

bp = Blueprint('cadastro', __name__)

@bp.route('/cadastro/novo', methods=['GET', 'POST'])
@login_required
def novo_cadastro():
    form = CadastroIndividualForm()
    if form.validate_on_submit():
        try:
            # Criar o cadastro principal
            cadastro = CadastroIndividual()
            form.populate_obj(cadastro)
            cadastro.uuid = str(uuid.uuid4())
            cadastro.criado_por_id = current_user.id
            cadastro.microarea = current_user.microarea
            
            # Criar info sociodemográfica
            info_socio = InfoSociodemografica(
                frequenta_escola=form.frequenta_escola.data,
                curso_mais_elevado=form.curso_mais_elevado.data,
                situacao_trabalho=form.situacao_trabalho.data,
                ocupacao_codigo_cbo2002=form.ocupacao_codigo_cbo2002.data,
                status_deseja_informar_orientacao_sexual=form.status_deseja_informar_orientacao_sexual.data,
                orientacao_sexual=form.orientacao_sexual.data if form.status_deseja_informar_orientacao_sexual.data else None,
                status_deseja_informar_identidade_genero=form.status_deseja_informar_identidade_genero.data,
                identidade_genero=form.identidade_genero.data if form.status_deseja_informar_identidade_genero.data else None
            )
            cadastro.info_sociodemografica = info_socio
            
            # Criar condições de saúde
            condicoes = CondicoesSaude(
                status_eh_gestante=form.status_eh_gestante.data,
                maternidade_referencia=form.maternidade_referencia.data if form.status_eh_gestante.data else None,
                status_tem_hipertensao=form.status_tem_hipertensao.data,
                status_tem_diabetes=form.status_tem_diabetes.data,
                status_tem_deficiencia=form.status_tem_deficiencia.data,
                deficiencias=form.deficiencias.data if form.status_tem_deficiencia.data else None
            )
            cadastro.condicoes_saude = condicoes
            
            # Criar situação de rua se aplicável
            if form.status_situacao_rua.data:
                situacao_rua = SituacaoRua(
                    status_situacao_rua=True,
                    tempo_rua=form.tempo_rua.data
                )
                cadastro.situacao_rua = situacao_rua
            
            # Salvar tudo no banco
            db.session.add(cadastro)
            db.session.commit()
            
            flash('Cadastro realizado com sucesso!', 'success')
            return redirect(url_for('cadastro.ver_cadastro', id=cadastro.id))
            
        except Exception as e:
            db.session.rollback()
            flash('Erro ao salvar o cadastro. Por favor, tente novamente.', 'danger')
            print(str(e))  # Para debug
            
    return render_template('cadastro/novo.html', form=form)

@bp.route('/cadastro/<int:id>', methods=['GET'])
@login_required
def ver_cadastro(id):
    cadastro = CadastroIndividual.query.get_or_404(id)
    # Verificar se o usuário tem acesso a este cadastro
    if not current_user.is_admin and cadastro.microarea != current_user.microarea:
        flash('Você não tem permissão para acessar este cadastro.', 'danger')
        return redirect(url_for('main.index'))
    return render_template('cadastro/ver.html', cadastro=cadastro)

@bp.route('/cadastro/<int:id>/editar', methods=['GET', 'POST'])
@login_required
def editar_cadastro(id):
    cadastro = CadastroIndividual.query.get_or_404(id)
    # Verificar se o usuário tem acesso a este cadastro
    if not current_user.is_admin and cadastro.microarea != current_user.microarea:
        flash('Você não tem permissão para editar este cadastro.', 'danger')
        return redirect(url_for('main.index'))
        
    form = CadastroIndividualForm(obj=cadastro)
    
    if form.validate_on_submit():
        try:
            # Atualizar cadastro principal
            form.populate_obj(cadastro)
            
            # Atualizar info sociodemográfica
            if not cadastro.info_sociodemografica:
                cadastro.info_sociodemografica = InfoSociodemografica()
            form.populate_obj(cadastro.info_sociodemografica)
            
            # Atualizar condições de saúde
            if not cadastro.condicoes_saude:
                cadastro.condicoes_saude = CondicoesSaude()
            form.populate_obj(cadastro.condicoes_saude)
            
            # Atualizar situação de rua
            if form.status_situacao_rua.data:
                if not cadastro.situacao_rua:
                    cadastro.situacao_rua = SituacaoRua()
                form.populate_obj(cadastro.situacao_rua)
            elif cadastro.situacao_rua:
                db.session.delete(cadastro.situacao_rua)
            
            db.session.commit()
            flash('Cadastro atualizado com sucesso!', 'success')
            return redirect(url_for('cadastro.ver_cadastro', id=cadastro.id))
            
        except Exception as e:
            db.session.rollback()
            flash('Erro ao atualizar o cadastro.', 'danger')
            print(str(e))
            
    return render_template('cadastro/editar.html', form=form, cadastro=cadastro) 