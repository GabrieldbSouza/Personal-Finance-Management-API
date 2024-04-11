from routes.home import home_route
from routes.user import user_route
from database.database import db
from database.models.user import User
from flask_login import LoginManager

def config_all(app):
  app.config['SECRET_KEY'] = 'a07cc77f927b7ed76aac1e3582e49dcd22e02cd8a97f6188a7540de141de475a'
  config_routes(app)
  config_db(app)
  config_login(app)

def config_routes(app):
  app.register_blueprint(home_route)
  app.register_blueprint(user_route, url_prefix = '/user/<int:user_id>/')


def config_db(app):
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///personalfinancemanagement.db'
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  db.init_app(app)
  with app.app_context():
    db.create_all()

def config_login(app):
  login_manager = LoginManager()
  login_manager.init_app(app)
  login_manager.login_view = 'home.home'  
  login_manager.session_protection = 'strong'

  @login_manager.user_loader
  def load_user(user_id):
    return User.query.get(int(user_id))