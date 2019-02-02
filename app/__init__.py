from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config['SECRET_KEY'] = 'f7dbe0239f0183dfb94fe81a46810f15'
app.config['SQLALCHEMY_DAPOstTABASE_URI'] = "sqlite:///site.db"
db = SQLAlchemy(app)

from app import routes