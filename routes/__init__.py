from flask import Flask, render_template
from config import ApplicationConfig
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine


from sqlalchemy import create_engine




app = Flask(__name__)

app.secret_key = 'server_session'

app.config.from_object(ApplicationConfig)
db = SQLAlchemy(app)
db.init_app(app)
engine = create_engine("mysql+pymysql://root:0000@localhost:3306/wedding", encoding='utf-8')


@app.route("/")
def index():
    return render_template("index.html", 
                            groom="김아무개", 
                            bride="이아무개", 
                            main_pic='images/main_pic.png', 
                            wedding_hall='A호텔 웨딩홀',
                            pic2='images/pic2.png',
                            account1=12345, 
                            account2=67890, 
                            account3=98765, 
                            account4=43210
    )
