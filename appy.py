# importando a bilioteca do flask para fazer um site
from flask import flask, render_template, request

app=flask(_name)

@app.route('/')
def home()
  return  render_template('index.html')

  if _name_ =='_main_':
    app.run(debug=true