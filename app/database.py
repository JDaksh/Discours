from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
import time
from psycopg2.extras import RealDictCursor
from .config import settings

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit= False, autoflush= False, bind= engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()


# could remove the latter, if no future plans to include
# while True:
    # try:
    #     conn = psycopg2.connect(host = 'localhost', database = 'fpi1', user = 'postgres', password = 'elephantrem', cursor_factory=RealDictCursor)
    #     cursor = conn.cursor()
    #     print("Database connection was successful")
    #     break
    # except Exception as e:
    #     print("Connecting to Database failed")
    #     print("Error: ", e)
    #     time.sleep(2)