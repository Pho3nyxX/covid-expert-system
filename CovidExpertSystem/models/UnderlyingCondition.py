from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import Table
from sqlalchemy import ForeignKey

Base = declarative_base()


class UnderlyingCondition(Base):
    __tablename__ = "underlying_condition"

    # mapping to columns in database
    underlying_condition_id = Column(Integer, primary_key=True)
    name = Column(String(50))

    # constructor
    def __init__(self, underlying_condition_id, name):
        self.underlying_condition_id = underlying_condition_id
        self.name = name

    # # getters and setters
    # @property
    # def underlying_condition_id(self):
    #     return self._underlying_condition_id
    #
    # @underlying_condition_id.setter
    # def underlying_condition_id(self, value):
    #     self._underlying_condition_id = value
    #
    # @property
    # def name(self):
    #     return self._name
    #
    # @name.setter
    # def name(self, value):
    #     self._name = value

    def __repr__(self):
        return f"underlying Condition(underlying_condition_id={self.underlying_condition_id!r}, " \
               f"Name={self.name!r}"


