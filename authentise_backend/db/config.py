from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


# Set up the database connection
def get_engine():
    DATABASE_URL = "sqlite:///pets.db"
    return create_engine(DATABASE_URL)


def get_session_local():
    engine = get_engine()
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return SessionLocal
