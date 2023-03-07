import tkinter as tk
from tkinter import messagebox

from CovidExpertSystem.views.Dashboard import Dashboard
from CovidExpertSystem.views.ForgetPassword import ForgetPassword
from CovidExpertSystem.views.Login import Login
from CovidExpertSystem.views.ChangePassword import ChangePassword
from CovidExpertSystem.views.SystolicDiastolic import SystolicDiastolic
from CovidExpertSystem.views.ViewPatient import ViewPatient
from CovidExpertSystem.views.AddPatient import AddPatient
from CovidExpertSystem.views.AddUnderlyingCondition import AddUnderlyingCondition
from CovidExpertSystem.views.EditPatient import EditPatient




class MainWindow(tk.Tk):
    def __init__(self, logged_in=False, underlying_conds=None, symptoms=None):
        super().__init__()

        self.geometry("330x200")  # setting the size of the window
        self.configure(bg='#006778')  # adding colour
        self.resizable(1, 1)  # preventing the window from resizing
        self.title("COVID EXPERT")

        self.dashboard = Dashboard(self)
        self.addPatient = AddPatient(self, underlying_cond_list=underlying_conds, symptoms_list=symptoms)
        self.changePassword = ChangePassword(self)
        self.login = Login(self)
        self.forgetPassword = ForgetPassword(self)
        self.editPatient = EditPatient(self)
        self.viewPatient = ViewPatient(self)
        self.systolicDiastolic = SystolicDiastolic(self)
        self.addUnderlyingCondition = AddUnderlyingCondition(self)

        if logged_in is False:
            self.change_current_view("login")
        else:
            self.change_current_view("dashboard")

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def change_current_view(self, currentFrame ="login"):
        self.currentFrame = currentFrame
        exec("self." + self.currentFrame + ".tkraise()")
        self.resize_window()

    def on_closing(self):
        match self.currentFrame:
            case "login":
                if messagebox.askokcancel("Quit", "Do you want to quit?"):
                    self.destroy()
            case _:
                self.destroy()

    def resize_window(self):
        size = eval("self."+self.currentFrame+".window_size")
        self.geometry(size)  # setting the size of the window

