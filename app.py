from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import pymysql
from config import ApplicationConfig

# 확장을 생성
db = SQLAlchemy()
# create the app
app = Flask(__name__)
# 앱 인스턴스 폴더를 기준으로 SQLite 데이터베이스 구성

# app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://' + user + ":" + passwd + '@' + host + "/" + database
app.config.from_object(ApplicationConfig)

# 확장 프로그램으로 앱 초기화
db.init_app(app)

from models import User

@app.route("/")
def index():
    return render_template("index.html", groom='test_name_1', bride="이아무개", main_pic='images/main_pic.png', wedding_hall='A호텔 웨딩홀',
                            pic2='images/pic2.png', account1=12345, account2=67890, account3=98765, account4=43210)
    
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run()
