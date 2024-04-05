from routes.home import home_route
from routes.user import user_route
from database.database import db

SECRET_KEY = 'sua_chave_secreta_aqui'

def config_all(app):
  config_routes(app)
  config_db(app)

def config_routes(app):
  app.register_blueprint(home_route)
  app.register_blueprint(user_route, url_prefix = '/user/<int:user_id>/')

def config_db(app):
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///personalfinancemanagement.db'
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  db.init_app(app)
  with app.app_context():
    db.create_all()
