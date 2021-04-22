import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv(verbose=True)

POSTGRES_USERNAME = os.getenv('POSTGRES_USERNAME', 'fastapi')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'fastapi')
POSTGRES_HOST = os.getenv('POSTGRES_HOST', '127.0.0.1')
POSTGRES_PORT = os.getenv('POSTGRES_PORT', 5432)
POSTGRES_DB = os.getenv('POSTGRES_DB', 'fastapi')

SQLALCHEMY_DATABASE_URL = ("postgresql://"
                           f"{POSTGRES_USERNAME}:"
                           f"{POSTGRES_PASSWORD}@"
                           f"{POSTGRES_HOST}:"
                           f"{POSTGRES_PORT}/"
                           f"{POSTGRES_DB}")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
