from sqlalchemy.orm import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer


Base = declarative_base()

class PatientUnderlyingCondition(Base):
    __tablename__ = "patient_underlying_condition"

    patient_id = Column(Integer, primary_key=True)
    underlying_condition_id = Column(Integer, primary_key=True)

    # constructor
    def __init__(self, patient_symptom_id, test_id, patient_id, symptom_id):
        self.patient_id = patient_id
        self.underlying_condition_id = symptom_id



    def __repr__(self):
        return f"Patient ID={self.patient_id!r}, " \
               f"Underlying Condition ID={self.underlying_condition_id!r}), "

