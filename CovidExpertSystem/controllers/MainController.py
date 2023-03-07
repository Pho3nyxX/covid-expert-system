from CovidExpertSystem.views.MainWindow import MainWindow
from CovidExpertSystem.models.User import User
from CovidExpertSystem.models.Address import Address
from CovidExpertSystem.models.Patient import Patient
from CovidExpertSystem.models.Symptom import Symptom
from CovidExpertSystem.models.PatientSymptom import PatientSymptom
from CovidExpertSystem.models.UnderlyingCondition import UnderlyingCondition
from CovidExpertSystem.models.PatientUnderlyingCondition import PatientUnderlyingCondition
from CovidExpertSystem.models.Vital import Vital

from functools import partial

from sqlalchemy import create_engine  # for making connection
# from sqlalchemy import text  # for testing if connection is being made
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy import insert
import urllib.parse  # for parsing password
from pathlib import Path


class MainController:
    def __init__(self):
        # create class members for logged in user
        self.currentUser = None
        # create class members for the main app window
        self.mainWindow = None
        # create class members for database session (sqlalchemy)
        self.session = None

        # start app by connecting to db and setting up GUI
        self.connect_db()
        self.start()

    def start(self):
        self.mainWindow = MainWindow(underlying_conds=self.load_underlying_conditions_list(), symptoms=self.load_symptoms_list())
        self.mainWindow.login.login_button.config(command=self.login)
        # *****************************************************************************
        # dashboard listeners
        self.mainWindow.dashboard.new_patient_button.config(command=partial(self.mainWindow.change_current_view, "addPatient"))
        self.mainWindow.dashboard.new_symptom_button.config(command=partial(self.mainWindow.change_current_view, "addUnderlyingCondition"))
        # self.mainWindow.dashboard.new_patient_button.config(command=partial(self.mainWindow.change_current_view, "addPatient"))

        # underlying condition listeners
        self.mainWindow.addUnderlyingCondition.save_button.config(command=self.add_underlying_symptom)
        self.mainWindow.addUnderlyingCondition.cancel_button.config(command=partial(self.mainWindow.change_current_view, "dashboard"))

        # add patient listeners
        self.mainWindow.addPatient.save_button.config(command=self.add_patient)
        self.mainWindow.addPatient.cancel_button.config(command=partial(self.mainWindow.change_current_view, "dashboard"))


        self.mainWindow.mainloop()

    def login(self):
        # self.mainWindow.login.password.get()
        # print(self.mainWindow.login.password.get())
        user = User(self.session.execute(
            select(User).
                where(User.password == self.mainWindow.login.password.get()).
                where(User.username == self.mainWindow.login.username.get())
        ).first())
        if type(user) is None:
            self.mainWindow.login.login_failed_label.configure(text="Login failed")
            print("User " + self.mainWindow.login.username.get() + " login failed")

        elif user.username == self.mainWindow.login.username.get() and user.password == self.mainWindow.login.password.get():
            self.currentUser = user
            self.mainWindow.login.failTxt.set("")
            self.mainWindow.change_current_view("dashboard")
            print("User " + self.currentUser.username + " login successful")

        else:
            self.mainWindow.login.login_failed_label.configure(text="Login failed")
            print("User " + self.mainWindow.login.username.get() + " login failed")

        # print(type(user))

    def add_patient(self):
        # use try catch(except) to handle exceptions that might occur
        try:
            print("add patient")
            patient = Patient(None,
                              self.mainWindow.addPatient.email.get(),
                              self.mainWindow.addPatient.gender.get(),
                              self.mainWindow.addPatient.first_name.get(),
                              self.mainWindow.addPatient.last_name.get(),
                              self.mainWindow.addPatient.middle_name.get(),
                              None,
                              None,
                              self.mainWindow.addPatient.contact.get(),
                              self.mainWindow.addPatient.emergency_contact.get())
            self.session.add(patient)
            self.session.commit()
            # print(patient)
            # Address - create address using patient id from the patient saved above
            address = Address(patient.patient_id,
                              self.mainWindow.addPatient.street.get(),
                              self.mainWindow.addPatient.parish.get(),
                              self.mainWindow.addPatient.town.get()
                              )
            self.session.add(address)

            # # Vitals - create vitals using patient id from the patient saved above
            vital = Vital(patient.patient_id,
                          None,
                          None,
                          self.mainWindow.addPatient.temperature.get(),
                          self.mainWindow.addPatient.weight.get(),
                          self.mainWindow.addPatient.height.get(),
                          )
            self.session.add(vital)
            self.session.commit()

            # get selected symptoms
            selected_symptoms = []
            for i in self.mainWindow.addPatient.symptom_list.curselection():
                # get names of selected symptoms
                selected_symptoms.append(self.mainWindow.addPatient.symptom_list.get(i))

            # get id of symptoms from database
            symptom_ids = self.load_symptoms_list(selected_symptoms)

            # save patient_symptom record to database
            with self.engine.connect() as conn:
                for sym in symptom_ids:
                    stmt = insert(PatientSymptom).values(patient_id=patient.patient_id, symptom_id=sym)
                    self.engine.execute(stmt)

            # print(symptom_ids)

            # get selected underlying conditions
            selected_conditions = []
            # print(self.mainWindow.addPatient.underlying_list.curselection())
            for j in self.mainWindow.addPatient.underlying_list.curselection():
                selected_conditions.append(self.mainWindow.addPatient.underlying_list.get(j))

            condition_ids = self.load_underlying_conditions_list(selected_conditions)

            # save patient_underlying_condition record to database
            with self.engine.connect() as conn:
                    for und in condition_ids:
                        stmt = insert(PatientUnderlyingCondition).values(patient_id=patient.patient_id, underlying_condition_id=und)
                        self.engine.execute(stmt)
            # print(condition_ids)

        # catch any errors that occur
        except Exception as ex:
            # undo changes to the database
            self.session.rollback()
            print(ex)

    def add_underlying_symptom(self):
        # use try catch(except) to handle exceptions that might occur
        try:
            if self.mainWindow.addUnderlyingCondition.type_selected.get() == "Symptoms":
                # Symptom Object
                symptom = Symptom(None, self.mainWindow.addUnderlyingCondition.symptomTxt.get())
                self.session.add(symptom)
            elif self.mainWindow.addUnderlyingCondition.type_selected.get() == "Underlying Condition":
                # Underlying Condition Object
                underlying_condition = UnderlyingCondition(None, self.mainWindow.addUnderlyingCondition.symptomTxt.get())
                self.session.add(underlying_condition)

            self.session.commit()
            self.mainWindow.addUnderlyingCondition.save_success.set(
                self.mainWindow.addUnderlyingCondition.type_selected.get() + " Saved successfully"
            )

        # catch any errors that occur
        except Exception as ex:
            # undo changes to the database
            self.session.rollback()
            self.mainWindow.addUnderlyingCondition.save_success.set(
                "Error:" + self.mainWindow.addUnderlyingCondition.type_selected.get() + " save failed"
            )
            print(ex)

    def connect_db(self):
        # ***********************************************************************

        # load password with load_config & parse the password
        passwd = urllib.parse.quote_plus(load_config())
        # adding parsed password to connection string
        connection_string = "mysql+mysqldb://ai_project_user:" + passwd + "@localhost/expertsystem"
        self.engine = create_engine(connection_string)

        # create session object
        self.session = Session(self.engine)

    def load_underlying_conditions_list(self, list_of_names=None):
        if list_of_names is None:
            cmd = select(UnderlyingCondition)
            underlying_list = []
            for underlying in self.session.execute(cmd):
                underlying_list.append(underlying["UnderlyingCondition"].name)

        else:
            cmd = select(UnderlyingCondition).filter(UnderlyingCondition.name.in_(list_of_names))
            underlying_list = []
            for underlying in self.session.execute(cmd):
                underlying_list.append(underlying["UnderlyingCondition"].underlying_condition_id)

        # print(underlying_list)
        return underlying_list

    def load_symptoms_list(self, list_of_names=None):
        symptoms_list = []
        if list_of_names is None:
            special_symptoms = ["Blurred Vision","Fainting","Dizziness"]
            cmd = select(Symptom).filter(Symptom.name.notin_(special_symptoms));

            for symptom in self.session.execute(cmd):
                # if symptom["Symptom"].name not in special_symptoms:
                symptoms_list.append(symptom["Symptom"].name)
        else:
            cmd = select(Symptom).filter(Symptom.name.in_(list_of_names));

            for symptom in self.session.execute(cmd):
                symptoms_list.append(symptom["Symptom"].symptom_id)

        # print(underlying_list)
        return symptoms_list


# load mysql password from config file
def load_config():
    # get absolute path and add path to config file
    p = Path('../config.txt')
    # open config file and read password from it
    config_file = open(p, "r")
    passwd = config_file.read()
    # close file
    config_file.close()

    return passwd

