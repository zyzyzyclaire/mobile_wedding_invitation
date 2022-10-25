from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy

app = Flask(__name__)

# database 설정파일
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:1234@local:3306/mobile_wedding_invitation"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)