from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import db
from app.models.health_condition import HealthCondition
from app.forms.health_condition import HealthConditionForm

bp = Blueprint('health', __name__)

@bp.route('/cidadao/<int:cidadao_id>/condicoes-saude', methods=['GET', 'POST'])
@login_required
def condicoes_saude(cidadao_id):
    form = HealthConditionForm()
    
    # Buscar condição de saúde existente ou criar nova
    condicao = HealthCondition.query.filter_by(cidadao_id=cidadao_id).first()
    if not condicao:
        condicao = HealthCondition(cidadao_id=cidadao_id)
    
    if form.validate_on_submit():
        # Atualizar dados da condição de saúde
        condicao.gestante = form.gestante.data
        condicao.maternidade_referencia = form.maternidade_referencia.data
        condicao.peso_auto_referido = form.peso_auto_referido.data
        condicao.doenca_respiratoria = form.doenca_respiratoria.data
        condicao.tipo_doenca_respiratoria = form.tipo_doenca_respiratoria.data
        condicao.fumante = form.fumante.data
        condicao.uso_alcool = form.uso_alcool.data
        condicao.uso_outras_drogas = form.uso_outras_drogas.data
        condicao.hipertensao_arterial = form.hipertensao_arterial.data
        condicao.diabetes = form.diabetes.data
        condicao.teve_avc = form.teve_avc.data
        condicao.teve_infarto = form.teve_infarto.data
        condicao.doenca_cardiaca = form.doenca_cardiaca.data
        condicao.tipo_doenca_cardiaca = form.tipo_doenca_cardiaca.data
        condicao.problema_rins = form.problema_rins.data
        condicao.tipo_problema_rins = form.tipo_problema_rins.data
        condicao.hanseniase = form.hanseniase.data
        condicao.tuberculose = form.tuberculose.data
        condicao.cancer = form.cancer.data
        condicao.internacao_12_meses = form.internacao_12_meses.data
        condicao.problema_saude_mental = form.problema_saude_mental.data
        condicao.acamado = form.acamado.data
        condicao.domiciliado = form.domiciliado.data
        condicao.plantas_medicinais = form.plantas_medicinais.data
        condicao.praticas_integrativas = form.praticas_integrativas.data
        condicao.outras_condicoes = form.outras_condicoes.data

        try:
            if not condicao.id:
                db.session.add(condicao)
            db.session.commit()
            flash('Condições de saúde salvas com sucesso!', 'success')
            return redirect(url_for('citizen.view', cidadao_id=cidadao_id))
        except Exception as e:
            db.session.rollback()
            flash('Erro ao salvar as condições de saúde. Por favor, tente novamente.', 'error')
    
    # Preencher o formulário com dados existentes
    if condicao.id:
        form.gestante.data = condicao.gestante
        form.maternidade_referencia.data = condicao.maternidade_referencia
        form.peso_auto_referido.data = condicao.peso_auto_referido
        form.doenca_respiratoria.data = condicao.doenca_respiratoria
        form.tipo_doenca_respiratoria.data = condicao.tipo_doenca_respiratoria
        form.fumante.data = condicao.fumante
        form.uso_alcool.data = condicao.uso_alcool
        form.uso_outras_drogas.data = condicao.uso_outras_drogas
        form.hipertensao_arterial.data = condicao.hipertensao_arterial
        form.diabetes.data = condicao.diabetes
        form.teve_avc.data = condicao.teve_avc
        form.teve_infarto.data = condicao.teve_infarto
        form.doenca_cardiaca.data = condicao.doenca_cardiaca
        form.tipo_doenca_cardiaca.data = condicao.tipo_doenca_cardiaca
        form.problema_rins.data = condicao.problema_rins
        form.tipo_problema_rins.data = condicao.tipo_problema_rins
        form.hanseniase.data = condicao.hanseniase
        form.tuberculose.data = condicao.tuberculose
        form.cancer.data = condicao.cancer
        form.internacao_12_meses.data = condicao.internacao_12_meses
        form.problema_saude_mental.data = condicao.problema_saude_mental
        form.acamado.data = condicao.acamado
        form.domiciliado.data = condicao.domiciliado
        form.plantas_medicinais.data = condicao.plantas_medicinais
        form.praticas_integrativas.data = condicao.praticas_integrativas
        form.outras_condicoes.data = condicao.outras_condicoes

    return render_template('health/condicoes_saude.html', form=form, cidadao_id=cidadao_id) 