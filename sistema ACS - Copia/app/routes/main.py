from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from app import db
from app.models import CadastroIndividual
from sqlalchemy import or_

bp = Blueprint('main', __name__)

@bp.route('/')
@login_required
def index():
    page = request.args.get('page', 1, type=int)
    per_page = 20
    
    # Construir query base
    query = CadastroIndividual.query

    # Aplicar filtros
    nome = request.args.get('nome', '')
    if nome:
        query = query.filter(or_(
            CadastroIndividual.nome_completo.ilike(f'%{nome}%'),
            CadastroIndividual.nome_social.ilike(f'%{nome}%'),
            CadastroIndividual.cns.ilike(f'%{nome}%')
        ))

    microarea = request.args.get('microarea')
    if microarea:
        query = query.filter_by(microarea=microarea)

    status = request.args.get('status')
    if status:
        query = query.filter_by(status=status)

    # Si no es admin, mostrar solo los de su microárea
    if not current_user.is_admin:
        query = query.filter_by(microarea=current_user.microarea)

    # Ordenar y paginar
    cadastros = query.order_by(CadastroIndividual.nome_completo).paginate(
        page=page, per_page=per_page, error_out=False)

    # Obtener lista de microáreas para el filtro
    if current_user.is_admin:
        microareas = db.session.query(CadastroIndividual.microarea)\
            .distinct()\
            .order_by(CadastroIndividual.microarea)\
            .all()
        microareas = [m[0] for m in microareas if m[0]]
    else:
        microareas = [current_user.microarea]

    return render_template('index.html',
        cadastros=cadastros.items,
        page=page,
        pages=cadastros.pages,
        microareas=microareas
    ) 