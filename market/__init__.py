from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY']='6a1b5cc3493a02089d88ba99'

db = SQLAlchemy(app)

app.app_context().push()

from market import routes