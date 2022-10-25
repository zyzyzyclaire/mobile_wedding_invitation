from flask import Flask, render_template

from model import session_scope, test, test_from_vscode

app = Flask(__name__)

@app.route("/")
def index():
    with session_scope() as session:
        test_name_1 = session.query(test.test_name).all()
        print([i for i in test_name_1])

        # test_from_vscode_item = test_from_vscode(1,'test_name')
        # session.add(test_from_vscode_item)
        # session.commit()
        # session.refresh(test_from_vscode_item)

    return render_template("index.html", 
                            groom=test_name_1, 
                            bride="이아무개", 
                            main_pic='images/main_pic.png', 
                            wedding_hall='A호텔 웨딩홀',
                            pic2='images/pic2.png',
                            account1=12345, 
                            account2=67890, 
                            account3=98765, 
                            account4=43210
    )

if __name__ == '__main__':
    app.run()
