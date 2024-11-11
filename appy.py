# importando a biblioteca do Flaskpara fazer um site dinâmico
from flask import Flask, render_template, request,flash,redirect,url_for

app= Flask(__name__)
app.secret_key ='usuario123'
# cria uma lista e usuários e senha, depois vamos pegar no db
usuarios = {
    'admin' : 'admin',
    'joao vitor' : 'belobravo1234',
    'rafaela' : '111111',
    'heitor' : '1271',
}
# 
# 
# 
# definindo a rota pricipal do site
@app.route('/')
def home():
    return render_template('index.html')

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

@app.route("/pagina-do-aluno")
def pagina_do_aluno():
    return render_template("página do aluno.html")

@app.route('/verificar-login',methods=['POST'])
# Parte pricipaldo programa em Python
def verificar_login():
# Pegando o que o usuário digitou no campo de entrada de user e senha
    username = request.form['Usuário']
    password = request.form['senha']

    # Verifica se o usuario digitado está na lista e se 
    # a senha está certa
    if username in usuarios and usuarios[username] == password:
        return redirect(url_for('pagina_do_aluno'))
    else:
        flash('Usuário ou senha incorretos', 'danger')
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
