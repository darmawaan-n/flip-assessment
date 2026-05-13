from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Using PostgreSQL
SQLALCHEMY_DATABASE_URL = "postgresql://user:pass@db:5432/pokemon_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
