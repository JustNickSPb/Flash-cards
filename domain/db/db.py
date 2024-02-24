from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from domain.db.models import Base

engine = create_engine("postgresql+psycopg2://postgres:postgres@postgres:5432/postgres", echo=True)
Base.metadata.create_all(engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
