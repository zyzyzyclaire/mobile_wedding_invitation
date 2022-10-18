from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", groom="김아무개", bride="이아무개", 
        main_pic='images/main_pic.png', wedding_hall='A호텔 웨딩홀',
        pic2='images/pic2.png'
    )

if __name__ == '__main__':
    app.run()
