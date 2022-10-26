from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
import os
from config import ApplicationConfig

db = SQLAlchemy()

app = Flask(__name__)

app.config.from_object(ApplicationConfig)

db.init_app(app)

from models import User
    
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run()
