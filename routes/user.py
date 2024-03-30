from flask import Blueprint, render_template

user_route = Blueprint('user', __name__)

@user_route.route('/')
def page_user(user_id):
  # Rota para a página inicial do usuário.
  return render_template('user.html')

@user_route.route('/transaction/')
def all_transaction(user_id):
  # Rota para solicitar todas as transações.
  return render_template('transaction.html')  

@user_route.route('/transaction/from/<date>/')
def from_transaction(user_id, date_from):
  # Rota para solicitar todas as transações a partir de uma data específica.
  return render_template('transaction.html')

@user_route.route('/transaction/to/<date>/')
def to_transaction(user_id, date_to):
  # Rota para solicitar todas as transações até uma data específica.
  return render_template('transaction.html')

@user_route.route('/transaction/between/<date_from>/<date_to>/')
def between_transaction(user_id, date_from, date_to):
  # Rota para solicitar todas as transações entre duas datas específicas.
  return render_template('transaction.html')

@user_route.route('/transaction/new/')
def form_transaction(user_id):
  # Rota para exibir o formulário de transação
  return render_template('form_transaction.html')

@user_route.route('/transaction/new/', methods = ['POST'])
def new_transaction(user_id):
  # Rota para processar os dados de transação enviados pelo formulário.
  pass

@user_route.route('/transaction/update/')
def update_transaction(user_id):
  # Rota para atualizar os dados de transação enviados pelo formulário.
  pass

