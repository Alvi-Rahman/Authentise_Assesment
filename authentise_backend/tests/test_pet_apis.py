import pytest
from fastapi.testclient import TestClient
from main import app


@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client


def test_create_pet(client):
    # Test creating a new pet
    response = client.post(
        "/pets/",
        json={
            "name": "Fluffy",
            "breed": "Labrador",
            "ranking": 5,
            "pet_type": "Dog",
            "image_url": "https://example.com/fluffy.jpg",
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        "name": "Fluffy",
        "breed": "Labrador",
        "ranking": 5,
        "pet_type": "Dog",
        "image_url": "https://example.com/fluffy.jpg",
    }


def test_search_pets(client):
    # Test searching for pets by type
    response = client.get("/pets/?pet_type=Dog")
    assert response.status_code == 200
    pets = response.json()
    assert type(pets) == list
    if len(pets) > 0:
        assert list(pets[0].keys()) == ["name", "breed", "ranking", "pet_type", "image_url"]


def test_search_pets_invalid_type(client):
    # Test searching for pets with an invalid type
    response = client.get("/pets/?pet_type=Cgt")
    assert response.status_code == 200
    pets = response.json()
    assert len(pets) == 0


def test_delete_pet(client):
    # Test deleting a pet by name
    response = client.delete("/pets/Fluffy/")
    assert response.status_code == 200
    assert response.json() == {"message": "Pet deleted successfully"}


def test_delete_pet_not_found(client):
    # Test deleting a pet that doesn't exist
    response = client.delete("/pets/NonexistentPet/")
    assert response.status_code == 404
    assert response.json()["detail"] == "Pet not found"
