# views import
from CovidExpertSystem.views.ForgetPassword import ForgetPassword
from CovidExpertSystem.views.Login import Login
from CovidExpertSystem.views.ChangePassword import ChangePassword
from CovidExpertSystem.views.SystolicDiastolic import SystolicDiastolic
from CovidExpertSystem.views.ViewPatient import ViewPatient
from CovidExpertSystem.views.AddPatient import AddPatient
from CovidExpertSystem.views.AddUnderlyingCondition import AddUnderlyingCondition
from CovidExpertSystem.views.EditPatient import EditPatient
from CovidExpertSystem.views.MainWindow import MainWindow

from CovidExpertSystem.controllers.MainController import MainController
# models import
#from CovidExpertSystem.models.Address import Address
#from CovidExpertSystem.models.Lifestyle import Lifestyle
from CovidExpertSystem.models.Patient import Patient
#from CovidExpertSystem.models.PatientSymptom import PatientSymptom
from CovidExpertSystem.models.Symptom import Symptom
# from CovidExpertSystem.models.Test import Test
from CovidExpertSystem.models.UnderlyingCondition import UnderlyingCondition
from CovidExpertSystem.models.User import User
# from CovidExpertSystem.models.Vital import Vital





def main():

    # ******************* Testing Classes ************************

    # address = Address(1, "hanover", "St Andrew", "Kgn")
    # print(address.parish)

    # lifestyle = Lifestyle(0, True, False, "heavy")
    # print(lifestyle.smoke)

    # print(patient.contact_num)

    # ****************************** Testing Views *****************

   # forgetPassword = ForgetPassword()
   # forgetPassword.show_window()

   # changePassword = ChangePassword()
   # changePassword.show_window()

   # systolicDiastolic = SystolicDiastolic()
   # systolicDiastolic.show_window()

   # viewPatient = ViewPatient()
   # viewPatient.show_window()

   # addPatient = AddPatient()
   # addPatient.show_window()

   # condition = UnderlyingCondition()
   # condition.show_window()

   # patient = Patient()
   # patient.show_window()


    # ****************************** Patient Object *****************
    # patient = Patient(0, "mail@mail.com", "F", 12, "Joe", "John", "Pocket", "the course of action", "covid",
    #                  "111-2222", "555-4444")
    # session.add(patient)

    # ****************************** User Object *****************
    # user = User(1, 15, "password", "M", "Kindle", "Book", "Paige", "Supervisor")
    # session.add(user)

    # session.commit()
    # with engine.connect() as conn:
    #     result = conn.execute(text("select 'hello world'"))
    #     print(result.all())


    # current_user = User()
    # while(current_user.loggedIn == False):
    #     login = Login()
    #     login.show_window()

    mainController = MainController()



main()








