from flask import Flask
from config import config_all
from database.database import init_db

app = Flask(__name__)

config_all(app)
#init_db(app)

app.run(debug = True)
