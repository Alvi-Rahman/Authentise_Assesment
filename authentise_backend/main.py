from typing import List
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from fastapi_utils.tasks import run_in_threadpool
from db.config import get_session_local
import uvicorn


# Create the FastAPI app
from db.models import PetSchema, PetCreate
from db.schema import Pet

app = FastAPI()

SessionLocal = get_session_local()


# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# API endpoint to save a pet
@app.post("/pets/", response_model=PetSchema)
async def create_pet(pet: PetCreate, db: Session = Depends(get_db)):
    def save_pet():
        db_pet = Pet(
            name=pet.name,
            breed=pet.breed,
            ranking=pet.ranking,
            pet_type=pet.pet_type,
            image_url=pet.image_url,
        )
        db.add(db_pet)
        db.commit()
        db.refresh(db_pet)
        return db_pet

    return await run_in_threadpool(save_pet)


# API endpoint to search for pets by type
@app.get("/pets/", response_model=List[PetSchema])
async def search_pets(pet_type: str, db: Session = Depends(get_db)):
    def retrieve_pets():
        pets = db.query(Pet).filter(Pet.pet_type == pet_type).order_by(Pet.ranking.desc()).all()
        return pets

    return await run_in_threadpool(retrieve_pets)


# API endpoint to delete a pet by name
@app.delete("/pets/{pet_name}/")
async def delete_pet(pet_name: str, db: Session = Depends(get_db)):
    def remove_pet():
        db_pet = db.query(Pet).filter(Pet.name == pet_name)
        if not db_pet.first():
            raise HTTPException(status_code=404, detail="Pet not found")
        # db.delete(db_pet)
        # db.commit()
        db_pet.delete()
        db.commit()
        return {"message": "Pet deleted successfully"}

    return await run_in_threadpool(remove_pet)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
