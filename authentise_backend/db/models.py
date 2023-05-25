from pydantic import BaseModel, Field


# Pydantic model for the Pet object
class PetSchema(BaseModel):
    # id: int
    name: str
    breed: str
    ranking: int
    pet_type: str
    image_url: str

    class Config:
        orm_mode = True


# Pydantic model for creating a pet
class PetCreate(BaseModel):
    name: str
    breed: str
    ranking: int
    pet_type: str
    image_url: str = Field(default=None)
