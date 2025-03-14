from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
from app.models.user import User
from app import db

bp = Blueprint('auth', __name__)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('main.index'))
        flash('Usuario o contraseña inválidos')
    return render_template('auth/login.html')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        nombre_completo = request.form['nombre_completo']
        cns = request.form['cns']
        cbo = request.form['cbo']
        cnes = request.form['cnes']
        ine = request.form['ine']
        microarea = request.form['microarea']

        if password != confirm_password:
            flash('Las contraseñas no coinciden', 'error')
            return redirect(url_for('auth.register'))

        if User.query.filter_by(username=username).first():
            flash('El nombre de usuario ya existe', 'error')
            return redirect(url_for('auth.register'))

        if User.query.filter_by(cns=cns).first():
            flash('El CNS ya está registrado', 'error')
            return redirect(url_for('auth.register'))

        user = User(
            username=username,
            nombre_completo=nombre_completo,
            cns=cns,
            cbo=cbo,
            cnes=cnes,
            ine=ine,
            microarea=microarea
        )
        user.set_password(password)
        
        try:
            db.session.add(user)
            db.session.commit()
            flash('Usuario registrado exitosamente. Por favor inicie sesión.', 'success')
            return redirect(url_for('auth.login'))
        except Exception as e:
            db.session.rollback()
            flash('Error al registrar el usuario. Por favor, intente nuevamente.', 'error')
            return redirect(url_for('auth.register'))

    return render_template('auth/register.html')

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login')) 