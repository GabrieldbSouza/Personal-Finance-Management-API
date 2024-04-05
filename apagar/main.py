from flask import Flask
from config import config_all, SECRET_KEY
from database.database import init_db,db

app = Flask(__name__)

app.config['SECRET_KEY'] = SECRET_KEY
config_all(app)
init_db(app)

app.run(debug = True)
