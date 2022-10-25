from sqlalchemy import Column, Integer, String
from sqlalchemy import Column, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager


url = 'mysql://{}:{}@{}:{}/{}'.format(
    'root', #DATABASE_USER,
    '1234', #DATABASE_PASSWORD,
    '127.0.0.1', #DATABASE_HOST,
    '3306', #DATABASE_PORT,
    'mobile_wedding_invitation', #DATABASE_DB
)
  
engine = create_engine(url, echo=False, connect_args={'charset': 'utf8'}, pool_pre_ping=True, pool_size=20, max_overflow=100)
Base = declarative_base()
Session = sessionmaker(bind=engine, autoflush=False, autocommit=False)


@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise
    finally:
        session.close()

class test(Base):
    __tablename__ = 'test'
    test_id = Column(Integer, primary_key=True)
    test_name = Column(String(32), nullable=False)

    def __init__(self, test_id, test_name):
        self.test_id = test_id
        self.test_name = test_name

class test_from_vscode(Base):
    __tablename__ = 'test_from_vscode'
    test_from_vscode_id = Column(Integer, primary_key=True)
    test_from_vscode_name = Column(String(32), nullable=False)

    def __init__(self, test_from_vscode_id, test_from_vscode_name):
        self.test_from_vscode_id = test_from_vscode_id
        self.test_from_vscode_name = test_from_vscode_name