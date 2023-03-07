from tkinter import *
from tkinter import ttk
import tkinter as tk


class Login(ttk.Frame):

    def __init__(self, container):
        super().__init__(container, padding="6 6 12 12")
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.failTxt = tk.StringVar()
        self.failTxt.set("")

        self.window_size = "330x200"

        # creating first label and positioning it
        covid_label = ttk.Label(self, text="COVID")
        covid_label.grid(row=0, column=0, columnspan=2)

        # creating second label and positioning it
        covid_expert_label = ttk.Label(self, text="Sign in to continue to Covid Expert System")
        covid_expert_label.grid(row=1, column=0, columnspan=2)

        # creating the Name text label and input label
        username_label = ttk.Label(self, text="Name")
        username_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)

        self.username_entry = ttk.Entry(self, textvariable=self.username)
        self.username_entry.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)

        # creating the Password text label and input label
        password_label = ttk.Label(self, text="Password")
        password_label.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)

        self.password_entry = ttk.Entry(self, textvariable=self.password)
        self.password_entry.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

        # creating third label and positioning it
        self.login_failed_label = ttk.Label(self, text="")
        self.login_failed_label.grid(column=1, row=4, sticky=tk.E, padx=5, pady=5)

        # creating third label and positioning it
        forget_password_label = ttk.Label(self, text="Forget password?")
        forget_password_label.grid(column=1, row=5, sticky=tk.E, padx=5, pady=5)

        # # creating fourth label and positioning it
        # create_account_label = ttk.Label(self, text="Create account")
        # create_account_label.grid(column=2, row=5, sticky=tk.E, padx=5, pady=5)

        # def clicked():
        # login_button.configure(text="Clicked")

        # creating login_button and positioning it
        self.login_button = ttk.Button(self, text="Login")
        self.login_button.grid(row=5, column=2, sticky=E)

        self.grid(column=0, row=0, sticky="N, W, E, S")

    def get_window_size(self):
        return self.window_size

    # method to create the window
    def show_window(self):

        self.window = Tk()  # object/instance of the tkinter class
        self.window.geometry("330x200")  # setting the size of the window
        self.window.configure(bg='#006778')  # adding colour
        self.window.resizable(False, False)  # preventing the window from resizing
        self.window.title("Login")

        # creating a self and placing it inside the window
        mainframe = ttk.Frame(self.window, padding="6 6 12 12")
        mainframe.grid(column=0, row=0, sticky="N, W, E, S")

        # configuring the window
        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(0, weight=1)



        self.window.mainloop()
