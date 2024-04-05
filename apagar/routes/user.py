from flask import Blueprint, render_template, request, redirect, url_for, Response
from database.models.transaction import Transaction
from database.database import db
from datetime import datetime
import json
user_route = Blueprint('user', __name__)

@user_route.route('/')
def page_user(user_id):
  # Rota para a página inicial do usuário.
  return render_template('user.html', user_id = user_id)

from flask import request, jsonify

@user_route.route('/transaction/html')
def transaction_html(user_id):
    return render_template('transaction.html', user_id=user_id)

@user_route.route('/transaction/data')
def transaction_data(user_id):
    transactions = Transaction.query.filter_by(trans_user_id=user_id).all()
    transaction_data = [{'id': transaction.trans_id, 'trans_user_id': transaction.trans_user_id, 'date': str(transaction.trans_date), 'amount': str(transaction.trans_amount)} for transaction in transactions]
    return jsonify(transaction_data)

    # Verifica se a solicitação é AJAX
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        print("Solicitação AJAX recebida.")

        # Se a solicitação for AJAX, retorna os dados como JSON
        transactions = Transaction.query.filter_by(trans_user_id=user_id).all()
        transaction_data = [(transaction.trans_id, transaction.trans_user_id, str(transaction.trans_date), str(transaction.trans_amount)) for transaction in transactions]
        transaction_dicts = [{'trans_id': data[0], 'trans_user_id': data[1], 'trans_date': data[2], 'trans_amount': data[3]} for data in transaction_data]
        json_data = json.dumps(transaction_dicts)
        return Response(json_data, mimetype='application/json')
    
    # Se não for AJAX, retorna o HTML normalmente
    return render_template('transaction.html', user_id=user_id)

@user_route.route('/transaction/chartjs')
def transaction_chartjs(user_id):
  transactions = Transaction.query.filter_by(trans_user_id=user_id).all()
  transaction_data = [{'date': str(transaction.trans_date), 'amount': str(transaction.trans_amount)} for transaction in transactions]
  return jsonify(transaction_data)

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
  return render_template('form_transaction.html', user_id = user_id)

@user_route.route('/transaction/new/', methods = ['POST'])
def new_transaction(user_id):
  # Rota para processar os dados de transação enviados pelo formulário.
  user_id = request.form.get('user_id')
  date = request.form.get('date')
  amount = request.form.get('amount')
  trans_date = datetime.strptime(date, '%Y-%m-%d').date()

  new_transaction = Transaction(trans_user_id = user_id, trans_date = trans_date, trans_amount = amount)
  db.session.add(new_transaction)
  db.session.commit()
  
  return redirect(url_for('user.page_user', user_id = user_id))


@user_route.route('/transaction/update/')
def update_transaction(user_id):
  # Rota para atualizar os dados de transação enviados pelo formulário.
  pass

