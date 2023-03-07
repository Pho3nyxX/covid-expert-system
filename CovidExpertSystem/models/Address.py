from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy import ForeignKey

from CovidExpertSystem.models.Patient import Patient

Base = declarative_base()


class Address(Base):
    __tablename__ = "address"

    address_id = Column(Integer, primary_key=True)
    street = Column(String(50))
    parish = Column(String(50))
    town = Column(String(50))

    # patient = relationship("Patient", back_populates="addresses")

    # constructor
    def __init__(self, address_id, street, parish, town):
        self.address_id = address_id
        self.street = street
        self.parish = parish
        self.town = town

    # getters and setters
    # @property
    # def address_id(self):
    #     return self._address_id
    #
    # @address_id.setter
    # def address_id(self, value):
    #     self._address_id = value
    #
    # @property
    # def street(self):
    #     return self._street
    #
    # @street.setter
    # def street(self, value):
    #     self._street = value
    #
    # @property
    # def parish(self):
    #     return self._parish
    #
    # @parish.setter
    # def parish(self, value):
    #     self._parish = value
    #
    # @property
    # def town(self):
    #     return self._town
    #
    # @town.setter
    # def town(self, value):
    #     self._town = value

    def __repr__(self):
        return f"Address(address_id={self.address_id!r}, " \
               f"street={self.street!r}, " \
               f"parish={self.parish!r}, " \
               f"town={self.town!r})"






