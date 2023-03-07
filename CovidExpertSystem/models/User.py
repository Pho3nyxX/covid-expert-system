from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import Table
from sqlalchemy import ForeignKey

Base = declarative_base()


class User (Base):
    __tablename__ = "User"

    # mapping to columns in database
    user_id = Column(Integer, primary_key=True)
    age = Column(Integer)
    password = Column(String(50))
    username = Column(String(50))
    gender = Column(String(10))
    first_name = Column(String(50))
    last_name = Column(String(50))
    middle_name = Column(String(50))
    role = Column(String(50))

    # user log in status
    loggedIn = False;

    # constructor
    def __init__(self, user_id=None, age=None, username=None, password=None, gender=None, first_name=None, last_name=None, middle_name=None, role=None):
        super().__init__()

        self.user_id = user_id
        self.age = age
        self.username = username
        self.password = password
        self.gender = gender
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.role = role

    def __init__(self, user):
        super().__init__()
        if user is not None:
            self.user_id = user["User"].user_id
            self.age = user["User"].age
            self.username = user["User"].username
            self.password = user["User"].password
            self.gender = user["User"].gender
            self.first_name = user["User"].first_name
            self.last_name = user["User"].last_name
            self.middle_name = user["User"].middle_name
            self.role = user["User"].role

    # # getters and setters
    # @property
    # def user_id(self):
    #     return self._user_id
    #
    # @user_id.setter
    # def user_id(self, value):
    #     self._user_id = value
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
    # def password(self):
    #     return self._password
    #
    # @password.setter
    # def password(self, value):
    #     self._password = value
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
    # def role(self):
    #     return self._role
    #
    # @role.setter
    # def role(self, value):
    #     self._role = value

    def __repr__(self):
        return f"User(user_id={self.user_id!r}, " \
               f"Age={self.age!r}, " \
               f"Username={self.username!r}," \
               f"Password={self.password!r}," \
               f"Gender={self.gender!r}," \
               f"First Name={self.first_name!r}," \
               f"Last Name={self.last_name!r}," \
               f"Middle Name={self.middle_name!r}," \
               f"Role={self.role!r}"


