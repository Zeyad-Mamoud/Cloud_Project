from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:0000@db:5432/loan_db"
engine = create_engine(DATABASE_URL)
Base = declarative_base()