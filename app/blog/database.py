from sqlalchemy import create_engine
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from blog import pymysql
pymysql.install_as_MySQLdb()
from blog import MySQLdb
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/test"

engine = sqlalchemy.create_engine( SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(bind=engine,autocommit=False, autoflush=False)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()