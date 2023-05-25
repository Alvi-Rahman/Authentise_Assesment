from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from db.config import get_engine


Base = declarative_base()
engine = get_engine()


# Define the SQLAlchemy model
class Pet(Base):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    breed = Column(String)
    ranking = Column(Integer)
    pet_type = Column(String)
    image_url = Column(String, nullable=True)


# Create the database tables
Base.metadata.create_all(bind=engine)
