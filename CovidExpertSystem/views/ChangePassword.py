from tkinter import *
from tkinter import ttk
import tkinter as tk


class ChangePassword (ttk.Frame):
    def __init__(self, container):
        super().__init__(container, padding="6 6 12 12");

        self.window_size = "330x200"

        # creating first label and positioning it
        covid_label = ttk.Label(self, text="COVID")
        covid_label.grid(row=0, column=0, columnspan=2)

        # creating second label and positioning it
        enter_label = ttk.Label(self, text="Enter code sent via text")
        enter_label.grid(row=1, column=0, columnspan=2)

        # creating the Code text label and input label
        code_label = ttk.Label(self, text="Code")
        code_label.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)

        code_entry = ttk.Entry(self)
        code_entry.grid(row=2, column=1, sticky=tk.E, padx=5, pady=5)

        # creating the New Password text label and input label
        password_label = ttk.Label(self, text="New Password")
        password_label.grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)

        password_entry = ttk.Entry(self)
        password_entry.grid(row=3, column=1, sticky=tk.E, padx=5, pady=5)

        # creating the Confirm Password text label and input label
        confirm_password_label = ttk.Label(self, text="Confirm Password")
        confirm_password_label.grid(row=4, column=0, sticky=tk.W, padx=5, pady=5)

        confirm_password_entry = ttk.Entry(self)
        confirm_password_entry.grid(row=4, column=1, sticky=tk.E, padx=5, pady=5)

        # def clicked():
        # button.configure(text="Clicked")

        # creating button and positioning it
        button = ttk.Button(self, text="Submit", command='login')
        button.grid(row=7, column=1, sticky=W)

        self.grid(column=0, row=0, sticky="N, W, E, S")


    # method to create the window
    def show_window(self):

        window = Tk()  # object/instance of the tkinter class
        window.geometry("300x200")  # setting the size of the window
        window.configure(bg='#006778')  # adding colour
        window.resizable(False, False)  # preventing the window from resizing
        window.title("Change Password")

        # creating a mainframe and placing it inside the window
        mainframe = ttk.Frame(window, padding="6 6 12 12")
        mainframe.grid(column=0, row=0, sticky="N, W, E, S")

        # configuring the window
        window.columnconfigure(0, weight=1)
        window.rowconfigure(0, weight=1)



        window.mainloop()