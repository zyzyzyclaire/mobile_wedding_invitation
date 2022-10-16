from flask import Flask, render_template

app = Flask(__name__)

#DATABASE
import sqlite3
conn = sqlite3.connect('database.db')
print ("데이터베이스를 성공적으로 열었습니다.")
conn.execute('CREATE TABLE IF NOT EXISTS wedding_invitation (text_1 TEXT, text_2 TEXT, text_3 TEXT)')
print ("테이블이 생성되었습니다.")
conn.close()

@app.route('/wedding_invitation')
def wedding_invitation():
    #데이터베이스에서 데이터를 가져 온다. 
    con = sqlite3.connect("database.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from wedding_invitation")
    rows = cur.fetchall()
    print("DB:")
    print(rows)
    return render_template('index.html', rows = rows)




@app.route("/")
def index():
    return render_template("index.html", shinramg="김아무개", shinboo="이아무개")

if __name__ == '__main__':
    app.run()