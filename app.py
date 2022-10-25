from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from routes import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
