import pytest
from src.models.sqlite.settings.connection import db_connection_handler
from .pets_repository import PetsRepository
from .people_repository import PeopleRepository


@pytest.mark.skip(reason="Interação com o banco")
def test_pets_list():
    repo = PetsRepository(db_connection_handler)
    response = repo.list_pets()
    print()
    print(response)
 
@pytest.mark.skip(reason="Interação com o banco")   
def test_delete_pet():
    name = "belinha"
    repo = PetsRepository(db_connection_handler)
    repo.delete_pets(name)
    
@pytest.mark.skip(reason="Interação com o banco")
def test_insert_people():
    first_name = "Jose"
    last_name = "Silva"
    age = 42
    pet_id = 3
    
    repo = PeopleRepository(db_connection_handler)
    repo.insert_person(first_name, last_name, age, pet_id)
 
@pytest.mark.skip(reason="Interação com o banco")   
def test_get_person():
    person_id = 1
    
    repo = PeopleRepository(db_connection_handler)
    response = repo.get_person(person_id)
    print()
    print(response)
    
