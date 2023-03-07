from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy import ForeignKey

Base = declarative_base()


class Symptom(Base):
    __tablename__ = "Symptom"

    # mapping to columns in database
    symptom_id = Column(Integer, primary_key=True)
    name = Column(String(50))

    # constructor
    def __init__(self, symptom_id, name):
        self.symptom_id = symptom_id
        self.name = name

    # # getters and setters
    # @property
    # def symptom_id(self):
    #     return self._symptom_id
    #
    # @symptom_id.setter
    # def symptom_id(self, value):
    #     self._symptom_id = value
    #
    # @property
    # def name(self):
    #     return self._name
    #
    # @name.setter
    # def name(self, value):
    #     self._name = value

    def __repr__(self):
        return f"Symptom(symptom_id={self.symptom_id!r}, " \
               f"Name={self.name!r}"
