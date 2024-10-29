# importando a biblioteca do Flaskpara fazer um site dinâmico
from flask import Flask, render_template, request

app= Flask(_name_)
# cria uma lista e usuários e senha, depois vamos pegar no db
# 
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
if _name== 'main_':
    app.run(debug=True)
