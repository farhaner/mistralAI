from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

ORACLE_USER = os.getenv("ORACLE_USER")
ORACLE_PASS = os.getenv("ORACLE_PASS")
ORACLE_DSN = os.getenv("ORACLE_DSN")  # contoh: "localhost:1521/XEPDB1"

DATABASE_URL = f"oracle+oracledb://{ORACLE_USER}:{ORACLE_PASS}@{ORACLE_DSN}"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
