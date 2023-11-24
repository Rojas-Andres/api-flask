from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from core.config import settings

Base = declarative_base()

engine = create_engine(settings.DATABASE_URL, echo=True)

Session = sessionmaker(bind=engine)
session = Session()
