from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# SQL Server connection string
DATABASE_URL = "mssql+pyodbc://@DESKTOP-CG1SEAC\\SQLEXPRESS/mydb?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()