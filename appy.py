# importando a biblioteca do Flaskpara fazer um site dinâmico
from flask import Flask, render_template, request

app= Flask(__name__)
# cria uma lista e usuários e senha, depois vamos pegar no db
usuarios = {
    'admin' : 'admin',
    'usuario' : 'senha',
    'rafaela' : '111111',
    'heitor' : '1271'
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

@app.route("/música")
def música():
    return render_template("música.html")

@app.route("/principal")
def principal():
    return render_template("principal.html")

@app.route('/verificar-login',methods=['POST'])
# Parte pricipaldo programa em Python
def verificar_login():
# Pegando o que o usuário digitou no campo de entrada de user e senha
    username = request.form['Usuário']
    password = request.form['senha']

    # Verifica se o usuario digitado está na lista e se 
    # a senha está certa
    if username in usuarios and usuarios[username] == password:
        return f"Bem-vindo, {username}!"
    else:
        return "Usuário ou senha inválidos."


if __name__ == '__main__':
    app.run(debug=True)
