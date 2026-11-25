from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .config import settings

engine = create_engine(f'postgresql+psycopg2://{settings.database_username}:{settings.
database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}', echo = True)

SessionLocal = sessionmaker(autocommit= False, autoflush= False, bind= engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# while True:
#     try:
#         conn = psycopg2.connect("postgresql://postgres:mahakal%40123@localhost:5432/test" ,
#                                 cursor_factory= RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was succesfull!")
#         break
#     except Exception as error:
#         print("Connecting to database failed!")
#         print("Error:", error)
#     time.sleep(2)