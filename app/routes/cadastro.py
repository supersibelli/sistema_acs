from flask import Blueprint, render_template, redirect, url_for, flash, request
from app.models.cadastro_individual import CadastroIndividual
from app.forms.cadastro_forms import CadastroIndividualForm
from app import db
from flask_login import login_required
from datetime import datetime

bp = Blueprint('cadastro', __name__)

@bp.route('/cadastro/novo', methods=['GET', 'POST'])
@login_required
def novo_cadastro():
    form = CadastroIndividualForm()
    
    if form.validate_on_submit():
        try:
            cadastro = CadastroIndividual()
            
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
        
    return render_template('cadastro/form.html', form=form)

@bp.route('/cadastros')
@login_required
def lista_cadastros():
    cadastros = CadastroIndividual.query.all()
    return render_template('cadastro/lista.html', cadastros=cadastros) 