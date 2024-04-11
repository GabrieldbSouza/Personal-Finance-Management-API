from flask import Blueprint, render_template, request, redirect, url_for, session
from werkzeug.security import check_password_hash, generate_password_hash
from database.models.user import User
from database.database import db
from flask_login import login_user

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

  user = User.query.filter_by(user_email = email).first()

  if user and check_password_hash(user.user_password, password):
    login_user(user)
    #session['user_id'] = user.user_id
    #session['user_name'] = user.user_name 
    return redirect(url_for('user.page_user', user_id = user.user_id))
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

  if password != confirm_password or User.query.filter_by(user_email=email).first() is not None:
    return render_template('form_login_erro.html') 

  new_user = User(user_name = name, user_email = email, user_password = generate_password_hash(password))
  db.session.add(new_user)
  db.session.commit()

  session['user_name'] = new_user.user_name
  session['user_id'] = new_user.user_id

  return redirect(url_for('user.page_user', user_id = new_user.user_id))

