from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:keyblade@localhost:5432/postgres"

engine: Engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
