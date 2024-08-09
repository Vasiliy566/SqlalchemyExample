from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = create_engine("postgresql+psycopg2://username:password@ip:5432/default_db")


session_maker = sessionmaker(bind=engine)
