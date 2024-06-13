from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

def create_database_connection():
    engine = create_engine('postgresql://user:password@localhost:5432/dbname')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()

