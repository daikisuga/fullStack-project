'''
POSSIVELMENTE NÃO SERÁ NECESSÁRIO USAR ESTE ARQUIVO.
**ARQUIVO QUE TRATA AS AUTENCIAÇÕES DO USUÁRIO**
Este arquivo define as rotas de autenticação do usuário, incluindo login e logout.

from flask import Blueprint, request, redirect, render_template, session, current_app

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        config = current_app.config

        if username == config['USERNAME'] and password == config['PASSWORD']:
            session['logged_in'] = True
            return redirect('/')
        else:
            error = 'Usuário ou senha inválidos'
    return render_template('login.html', error=error)

@auth_bp.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect('/login')
'''