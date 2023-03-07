from tkinter import *
from tkinter import ttk
import tkinter as tk


class ForgetPassword(ttk.Frame):

    def __init__(self, container):
        super().__init__(container, padding="6 6 12 12")

        self.window_size = "330x150"

        # creating first label and positioning it
        covid_label = ttk.Label(self, text="COVID")
        covid_label.grid(column=0, row=0, columnspan=2)

        # creating second label and positioning it
        request_label = ttk.Label(self, text="Request Temporary Sign in")
        request_label.grid(row=1, column=0, columnspan=2)

        # creating the Name text label and input label
        name_label = ttk.Label(self, text="Name")
        name_label.grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)

        entry_label = ttk.Entry(self)
        entry_label.grid(row=3, column=1, sticky=tk.E, padx=5, pady=5)

        # creating the Role text label and input label
        role_label = ttk.Label(self, text="Role")
        role_label.grid(row=4, column=0, sticky=tk.W, padx=5, pady=5)

        entry_label = ttk.Entry(self)
        entry_label.grid(row=4, column=1, sticky=tk.E, padx=5, pady=5)

        self.grid(column=0, row=0, sticky="N, W, E, S")


    # method to create the window
    def show_window(self):

        window = Tk()  # object/instance of the tkinter class
        window.geometry("300x150")  # setting the size of the window
        window.configure(bg='#006778')  # adding colour
        window.resizable(False, False)  # preventing the window from resizing
        window.title("Forget Password")

        # creating a mainframe and placing it inside the window
        mainframe = ttk.Frame(window, padding="6 6 12 12")
        mainframe.grid(column=0, row=0, sticky="N, W, E, S")

        # configuring the window
        window.columnconfigure(0, weight=1)
        window.rowconfigure(0, weight=1)


    # def clicked():
        # button.configure(text="Clicked")

        # creating button and positioning it
        button = ttk.Button(mainframe, text="Request", command='request')
        button.grid(row=5, column=1, sticky=W)

        window.mainloop()

