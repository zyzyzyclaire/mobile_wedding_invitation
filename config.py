from dotenv import load_dotenv
import os

load_dotenv()

class ApplicationConfig:
  SECRET_KEY = os.environ["SECRET_KEY"]
  SQLALCHEMY_TRACH_MODIFICATIONS = False
  SQLALCHEMY_ECHO = True
  SQLALCHEMY_DATABASE_URI = r"mysql+pymysql://root:0000@localhost:3306/wedding"
  