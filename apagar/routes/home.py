from flask import Blueprint, render_template, request, redirect, url_for, session
from database.models.user import User
from database.database import db

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
  email = request.form['email']
  password = request.form['password']
  print(email, password)

  user = User.query.filter_by(user_email = email, user_password = password).first()
  
  if user:
    session['user_name'] = user.user_name  # Adiciona o nome do usuário à sessão
    return redirect(url_for('user.page_user', user_id=user.user_id))
  else:
    return render_template('form_login_erro.html')

@home_route.route('/register/')
def form_register():
  # Rota para exibir o formulário de registro.
  return render_template('form_register.html')

@home_route.route('/register/', methods = ['POST'])
def register():
  # Rota para processar os dados de registro enviados pelo formulário.
  name = request.form.get('name')
  email = request.form.get('email')
  password = request.form.get('password')
  confirm_password = request.form.get('confirm_password')
  print(name, email,password)

  if password != confirm_password:
    return render_template('form_login_erro.html')
  if User.query.filter_by(user_email = email).first():
    return render_template('form_login_erro.html')
    # Aqui você pode inserir os dados no banco de dados, por exemplo, usando SQLAlchemy
  new_user = User(user_name = name, user_email = email, user_password = password)
  db.session.add(new_user)
  db.session.commit()
    # Redirecionar para outra página após o cadastro bem-sucedido
  session['user_name'] = new_user.user_name
  return redirect(url_for('user.page_user', user_id=new_user.user_id))
  
