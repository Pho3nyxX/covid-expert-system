from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy import ForeignKey

Base = declarative_base()


class Patient(Base):
    __tablename__ = "patient"

    # mapping to columns in database
    patient_id = Column(Integer, primary_key=True)
    email = Column(String(100))
    gender = Column(String(10))
    first_name = Column(String(50))
    last_name = Column(String(50))
    middle_name = Column(String(50))
    action = Column(String(200))
    result = Column(String(50))
    contact_num = Column(String(20))
    emergency_contact_num = Column(String(20))

    # addresses = relationship("Address", back_populates="patient")
    # vitals = relationship("Vital", back_populates="patient")

    # constructor
    def __init__(self, patient_id, email, gender, first_name, last_name, middle_name, action, result, contact_num, emergency_contact_num):
        self.patient_id = patient_id
        self.email = email
        self.gender = gender
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.action = action
        self.result = result
        self.contact_num = contact_num
        self.emergency_contact_num = emergency_contact_num

    # # getters and setters
    # @property
    # def patient_id(self):
    #     return self._patient_id
    #
    # @patient_id.setter
    # def patient_id(self, value):
    #     self._patient_id = value
    #
    # @property
    # def email(self):
    #     return self._email
    #
    # @email.setter
    # def email(self, value):
    #     self._email = value
    #
    # @property
    # def gender(self):
    #     return self._gender
    #
    # @gender.setter
    # def gender(self, value):
    #     self._gender = value
    #
    # @property
    # def age(self):
    #     return self._age
    #
    # @age.setter
    # def age(self, value):
    #     self._age = value
    #
    # @property
    # def first_name(self):
    #     return self._first_name
    #
    # @first_name.setter
    # def first_name(self, value):
    #     self._first_name = value
    #
    # @property
    # def last_name(self):
    #     return self._last_name
    #
    # @last_name.setter
    # def last_name(self, value):
    #     self._last_name = value
    #
    # @property
    # def middle_name(self):
    #     return self._middle_name
    #
    # @middle_name.setter
    # def middle_name(self, value):
    #     self._middle_name = value
    #
    # @property
    # def action(self):
    #     return self._action
    #
    # @action.setter
    # def action(self, value):
    #     self._action = value
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
    # def contact_num(self):
    #     return self._contact_num
    #
    # @contact_num.setter
    # def contact_num(self, value):
    #     self._contact_num = value
    #
    # @property
    # def emergency_contact_num(self):
    #     return self._emergency_contact_num
    #
    # @emergency_contact_num.setter
    # def emergency_contact_num(self, value):
    #     self._emergency_contact_num = value

    def __repr__(self):
        return f"Patient(patient_id={self.patient_id!r}, " \
               f"Email={self.email!r}, " \
               f"Gender={self.gender!r}, " \
               f"First Name={self.first_name!r}, " \
               f"Last Name={self.last_name!r}, " \
               f"Middle Name={self.middle_name!r}, " \
               f"Action={self.action!r}, " \
               f"Result={self.result!r}, " \
               f"Contact Number={self.contact_num!r}, " \
               f"Emergency Contact Number={self.emergency_contact_num!r}"


