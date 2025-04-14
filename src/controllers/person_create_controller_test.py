import pytest
from .person_create_controller import PersonCreateController

class MockPeopleRepository:
    def insert_person(self, first_name: str, last_name: str, age: int, pet_id: id):
        pass
    
def test_create():
    person_info = {
        "first_name": "Theo",
        "last_name": "Melo",
        "age": 17,
        "pet_id": 6
    }
    
    controller = PersonCreateController(MockPeopleRepository())
    response = controller.create(person_info)
    
    assert response["data"]["type"] == "Person"
    assert response["data"]["count"] == 1
    assert response["data"]["attributes"] == person_info
    
def test_create_error():
    person_info = {
        "first_name": "Theo123",
        "last_name": "Melo",
        "age": 17,
        "pet_id": 6
    }
    
    controller = PersonCreateController(MockPeopleRepository())
    
    with pytest.raises(Exception):
        controller.create(person_info)