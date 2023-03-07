from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy import ForeignKey

Base = declarative_base()


class PatientSymptom(Base):
    __tablename__ = "patient_symptom"

    # mapping to columns in database
    patient_symptom_id = Column(Integer, primary_key=True)
    test_id = Column(Integer)
    patient_id = Column(Integer)
    symptom_id = Column(Integer)

    # constructor
    def __init__(self, patient_symptom_id, test_id, patient_id, symptom_id):
        self.patient_symptom_id = patient_symptom_id
        self.test_id = test_id
        self.patient_id = patient_id
        self.symptom_id = symptom_id

    # # getters and setters
    # @property
    # def patient_symptom_id(self):
    #     return self._patient_symptom_id
    #
    # @patient_symptom_id.setter
    # def patient_symptom_id(self, value):
    #     self._patient_symptom_id = value
    #
    # @property
    # def test_id(self):
    #     return self._test_id
    #
    # @test_id.setter
    # def test_id(self, value):
    #     self._test_id = value
    #
    # @property
    # def patient_id(self):
    #     return self._patient_id
    #
    # @patient_id.setter
    # def patient_id(self, value):
    #     self._patient_id = value
    #
    # @property
    # def symptom_id(self):
    #     return self._symptom_id
    #
    # @symptom_id.setter
    # def symptom_id(self, value):
    #     self._symptom_id = value

    def __repr__(self):
        return f"Patient Symptom(patient_symptom_id={self.patient_symptom_id!r}, " \
               f"Test id={self.test_id!r}, " \
               f"Patient id={self.patient_id!r}, " \
               f"Symptom id={self.symptom_id!r}), "

