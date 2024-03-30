from routes.home import home_route
from routes.user import user_route

def config_all(app):
  config_routes(app)

def config_routes(app):
  app.register_blueprint(home_route)
  app.register_blueprint(user_route, url_prefix = '/user/<int:user_id>/')


def config_db(app):
  pass