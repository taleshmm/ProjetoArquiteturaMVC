from typing import Dict
import re
from src.models.sqlite.interfaces.people_repository import PeopleRepositoryInterface

class PersonCreateController:
    def __init__(self, people_repository: PeopleRepositoryInterface) -> None:
        self.__people_respository = people_repository
        
    def create(self, person_info: Dict) -> Dict:
        first_name = person_info["first_name"]
        last_name = person_info["last_name"]
        age = person_info["age"]
        pet_id = person_info["pet_id"]
      
        self.__validade_first_name_and_last_name(first_name, last_name)
        self.__insert_person_in_db(first_name, last_name, age, pet_id)
        formated_response = self.__format_response(person_info)
        
        
        return formated_response
      
    def __validade_first_name_and_last_name(self, first_name: str, last_name: str) -> None:
        # Expressão regular para caracteres que não são letras
        non_valid_caracteres = re.compile(r'[^a-zA-Z]')
          
        if non_valid_caracteres.search(first_name) or non_valid_caracteres.search(last_name):
          raise Exception("Nome da pessoa inválido!")
    
    def __insert_person_in_db(self, first_name: str, last_name: str, age: int, pet_id: int) -> None:
        self.__people_respository.insert_person(first_name, last_name, age, pet_id)
    
    def __format_response(self, person_info: Dict) -> Dict:
      return {
        "data": {
          "type": "Person",
          "count": 1,
          "attributes": person_info
        }
      }
       
        