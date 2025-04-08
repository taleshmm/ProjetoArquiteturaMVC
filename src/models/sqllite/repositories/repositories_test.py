import pytest
from src.models.sqllite.settings.connection import db_connection_handler
from .pets_repository import PetsRepository


@pytest.mark.skip(reason="Interação com o banco")
def test_pets_list():
    repo = PetsRepository(db_connection_handler)
    response = repo.list_pets()
    print()
    print(response)
    
def test_delete_pet():
    name = "belinha"
    repo = PetsRepository(db_connection_handler)
    repo.delete_pets(name)