from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.pets import PetsTable
from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInterface

db_connection_handler.connect_to_db()

class PetsRepository(PetsRepositoryInterface):
    def __init__(self, db_connection) -> None:
      self.__db_connection = db_connection
      
    def list_pets(self) -> list[PetsTable]:
        with self.__db_connection as database:
            try:
              pets = database.session.query(PetsTable).all()
              return pets
            except NoResultFound:
              return []
          
    def delete_pets(self, name: str) -> None:
        with self.__db_connection as database:
            try:
                (
                  database.session
                  .query(PetsTable)
                  .filter(PetsTable.name == name)
                  .delete() 
                )
                database.session.commit()
            except Exception as exception:
              database.session.rollback()
              raise exception