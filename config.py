import os

host = os.environ["DB_HOST"]
user = os.environ["DB_USER"]
passwd = os.environ["DB_PASSWORD"]
database = os.environ["DB_NAME"]

class ApplicationConfig:
  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + user + ':' + passwd + '@' + host + '/' + database
