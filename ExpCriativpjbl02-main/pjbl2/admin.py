from flask import Blueprint, render_template, redirect, request
from login import is_authenticated, is_admin, users

adm_blueprint = Blueprint('admin',__name__, template_folder='templates')

sensores = []
atuadores = []

@adm_blueprint.route('/painel', methods=['GET', 'POST'])
def painel():
    if is_admin():
        if request.method == 'POST':
            # Adicionar usuário
            if 'nome-usuario' in request.form and 'senha-usuario' in request.form:
                nome_usuario = request.form['nome-usuario']
                senha_usuario = request.form['senha-usuario']
                users[nome_usuario] = senha_usuario

            # Deletar usuário
            elif 'nome-usuario-delete' in request.form:
                nome_usuario_delete = request.form['nome-usuario-delete']
                if nome_usuario_delete in users:
                    users.pop(nome_usuario_delete)
                        

            # Adicionar sensor
            elif 'tipo-sensor' in request.form:
                tipo_sensor = request.form['tipo-sensor']
                sensores.append(tipo_sensor)
                

            # Deletar sensor
            elif 'tipo-sensor-delete' in request.form:
                tipo_sensor_delete = request.form['tipo-sensor-delete']
                if tipo_sensor_delete in sensores:
                    sensores.remove(tipo_sensor_delete)
                    

            # Adicionar atuador
            elif 'tipo-atuador' in request.form:
                tipo_atuador = request.form['tipo-atuador']
                atuadores.append(tipo_atuador)

            # Deletar atuador
            elif 'tipo-atuador-delete' in request.form:
                tipo_atuador_delete = request.form['tipo-atuador-delete']
                if tipo_atuador_delete in atuadores:
                    atuadores.remove(tipo_atuador_delete)
                    
        return render_template('painel_adm.html')
    else:
        return redirect('/')