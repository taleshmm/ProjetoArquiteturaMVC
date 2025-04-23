from typing import Dict
from src.models.sqlite.interfaces.people_repository import PeopleRepositoryInterface
from src.models.sqlite.entities.people import PeopleTable
from .interfaces.person_finder_controller import PersonFinderControllerInterface

class PersonFinderController(PersonFinderControllerInterface):
    def __init__(self, people_repository: PeopleRepositoryInterface) -> None:
        self.__people_respository = people_repository
    
    def find(self, person_id: int) -> Dict:
        person = self.__find_person_in_db(person_id)
        formated_person = self.__format_reponse(person)
        return formated_person
    
    def __find_person_in_db(self, person_id: int) -> PeopleTable:
        person = self.__people_respository.get_person(person_id)
        if not person:
            raise Exception("Pessoa não encontrada.")
        
        return person
    
    def __format_reponse(self, person: PeopleTable) -> Dict:
        return {
            "data": {
                "type": "Person",
                "count": 1,
                "attributes": {
                    "first_name": person.first_name,
                    "last_name": person.last_name,
                    "pet_name": person.pet_name,
                    "pet_type": person.pet_type
                     }           
            }
        }