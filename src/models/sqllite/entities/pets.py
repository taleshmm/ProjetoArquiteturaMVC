from sqlalchemy import BIGINT, Column, String

from src.models.sqllite.settings.base import Base


class PetsTable(Base):
    __tablename__ = "pets"
    
    id = Column(BIGINT, primary_key=True)
    nome = Column(String, nullable=False)
    type = Column(String, nullable=False)
    
    def __repr__(self):
        return f"Pets [name={self.name}, type={self.type}]"