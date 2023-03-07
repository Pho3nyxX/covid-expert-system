from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import Table
from sqlalchemy import ForeignKey

Base = declarative_base()


class Test(Base):
    __tablename__ = "Test"

    # mapping to columns in database
    test_id = Column(Integer, primary_key=True)
    result = Column(String(100))
    test_date = Column(DateTime)
    result_date = Column(DateTime)
    notified = Column(bool=False)
    patient_id = Column(Integer, ForeignKey=True)

    # constructor
    def __init__(self, test_id, result, test_date, result_date, notified, patient_id):
        self.test_id = test_id
        self.result = result
        self.test_date = test_date
        self.result_date = result_date
        self.notified = notified
        self.patient_id = patient_id

    # # getters and setters
    # @property
    # def test_id(self):
    #     return self._test_id
    #
    # @test_id.setter
    # def test_id(self, value):
    #     self._test_id = value
    #
    # @property
    # def result(self):
    #     return self._result
    #
    # @result.setter
    # def result(self, value):
    #     self._result = value
    #
    # @property
    # def test_date(self):
    #     return self._test_date
    #
    # @test_date.setter
    # def test_date(self, value):
    #     self._test_date = value
    #
    # @property
    # def result_date(self):
    #     return self._result_date
    #
    # @result_date.setter
    # def result_date(self, value):
    #     self._result_date = value
    #
    # @property
    # def notified(self):
    #     return self._notified
    #
    # @notified.setter
    # def notified(self, value):
    #     self._notified = value
    #
    # @property
    # def patient_id(self):
    #     return self._patient_id
    #
    # @patient_id.setter
    # def patient_id(self, value):
    #     self._patient_id = value

    def __repr__(self):
        return f"Test(test_id={self.test_id!r}, " \
               f"Result={self.result!r}, " \
               f"Test Date={self.test_date!r}," \
               f"Result={self.result!r}," \
               f"Notified={self.notified!r}," \
               f"Patient id={self.patient_id!r}"
