from flask import Blueprint, render_template

home_route = Blueprint('home', __name__)

@home_route.route('/')
def home():
  # Rota para a página inicial do site.
  return render_template('home.html')

@home_route.route('/login/')
def form_login():
  # Rota para exibir o formulário de login.
  return render_template('form_login.html')

@home_route.route('/login/', methods = ['POST'])
def login():
  # Rota para processar os dados de login enviados pelo formulário.
  pass

@home_route.route('/register/')
def form_register():
  # Rota para exibir o formulário de registro.
  return render_template('form_register.html')

@home_route.route('/register/', methods = ['POST'])
def register():
  # Rota para processar os dados de registro enviados pelo formulário.
  pass
