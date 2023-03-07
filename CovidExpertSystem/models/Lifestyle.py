from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import Table
from sqlalchemy import ForeignKey

Base = declarative_base()


class Lifestyle(Base):
    __tablename__ = "Lifestyle"

    lifestyle_id = Column(Integer, primary_key=True)
    exercise = Column(boolean=False)
    smoke = Column(boolean=False)
    salt_intake = Column(boolean=False)

    # constructor
    def __init__(self, lifestyle_id, exercise, smoke, salt_intake):
        self.lifestyle_id = lifestyle_id
        self.exercise = exercise
        self.smoke = smoke
        self.salt_intake = salt_intake

    # # getters & setters
    # @property
    # def lifestyle_id(self):
    #     return self._lifestyle_id
    #
    # @lifestyle_id.setter
    # def lifestyle_id(self, value):
    #     self._lifestyle_id = value
    #
    # @property
    # def exercise(self):
    #     return self._exercise
    #
    # @exercise.setter
    # def exercise(self, value):
    #     self._exercise = value
    #
    # @property
    # def smoke(self):
    #     return self._smoke
    #
    # @smoke.setter
    # def smoke(self, value):
    #     self._smoke = value
    #
    # @property
    # def salt_intake(self):
    #     return self._salt_intake
    #
    # @salt_intake.setter
    # def salt_intake(self, value):
    #     self._salt_intake = value

    def __repr__(self):
        return f"Lifestyle(lifestyle_id={self.lifestyle_id!r}, " \
               f"Exercise={self.exercise!r}, " \
               f"Smoke={self.smoke!r}, " \
               f"Salt Intake={self.salt_intake!r})"

