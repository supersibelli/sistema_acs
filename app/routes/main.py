from flask import Blueprint, render_template
from flask_login import login_required

bp = Blueprint('main', __name__)

@bp.route('/')
@login_required
def index():
    """Página principal después del login"""
    return render_template('index.html') 