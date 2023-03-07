from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import Table
from sqlalchemy import ForeignKey
from sqlalchemy import Float

Base = declarative_base()


class Vital(Base):
    __tablename__ = "Vital"

    # mapping to columns in database
    vital_id = Column(Integer, primary_key=True)
    diastolic = Column(Float)
    systolic = Column(Float)
    temperature = Column(Float)
    weight = Column(Float)
    height = Column(Float)

    # patient = relationship("Patient", back_populates="vitals")

    # constructor
    def __init__(self, vital_id, diastolic, systolic, temperature, weight, height):
        self.vital_id = vital_id
        self.diastolic = diastolic
        self.systolic = systolic
        self.temperature = temperature
        self.weight = weight
        self.height = height

    # # getters and setters
    # @property
    # def vital_id(self):
    #     return self._vital_id
    #
    # @vital_id.setter
    # def vital_id(self, value):
    #     self._vital_id = value
    #
    # @property
    # def diastolic(self):
    #     return self._diastolic
    #
    # @diastolic.setter
    # def diastolic(self, value):
    #     self._diastolic = value
    #
    # @property
    # def systolic(self):
    #     return self._systolic
    #
    # @systolic.setter
    # def systolic(self, value):
    #     self._systolic = value
    #
    # @property
    # def temperature(self):
    #     return self._temperature
    #
    # @temperature.setter
    # def temperature(self, value):
    #     self._temperature = value
    #
    # @property
    # def weight(self):
    #     return self._weight
    #
    # @weight.setter
    # def weight(self, value):
    #     self._weight = value
    #
    # @property
    # def height(self):
    #     return self._height
    #
    # @height.setter
    # def height(self, value):
    #     self._height = value

    def __repr__(self):
        return f"Vital(vital_id={self.vital_id!r}, " \
               f"Diastolic={self.diastolic!r}, " \
               f"Systolic={self.systolic!r}," \
               f"Temperature={self.temperature!r}," \
               f"Weight={self.weight!r}," \
               f"Height={self.height!r}"
