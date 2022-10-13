from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", shinramg="김아무개", shinboo="이아무개")

if __name__ == '__main__':
    app.run()