from src.models.sqlite.interfaces.people_repository import PeopleRepositoryInterface

class PersonCreateController:
    def __init__(self, people_repository: PeopleRepositoryInterface) -> None:
      self.__people_respository = people_repository