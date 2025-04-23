from src.models.sqlite.entities.pets import PetsTable
from .pet_lister_controller import PetListerController

class MockPetsRepository:
    def list_pets(self):
        return [
            PetsTable(name="Theo", type="Dog", id=7),
            PetsTable(name="Snow", type="Cat", id=12),
        ]
        
def test_list_pets():
    controller = PetListerController(MockPetsRepository())
    response = controller.list()
    
    expected_response = {
        "data": {
             "type": "Pets",
              "count": 2,
              "attributes": [
                  {"name": "Theo", "type": "Dog", "id": 7},
                  {"name": "Snow", "type": "Cat", "id": 12}
              ]
        }
    }
    
    assert response == expected_response