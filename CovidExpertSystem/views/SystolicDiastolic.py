from tkinter import *
from tkinter import ttk
import tkinter as tk


class SystolicDiastolic(ttk.Frame):
    def __init__(self, container):
        super().__init__(container, padding="6 6 12 12")

        self.window_size = "300x150"

        # creating a self and placing it inside the window
        self.grid(column=0, row=0, sticky="N, W, E, S")

        # creating first label and positioning it
        covid_expert_label = ttk.Label(self, text="Covid Expert System")
        covid_expert_label.grid(row=0, column=0, columnspan=2)

        # creating the Systolic Value text label and input label
        systolic_label = ttk.Label(self, text="Systolic")
        systolic_label.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)

        systolic_entry = ttk.Entry(self)
        systolic_entry.grid(row=1, column=1, sticky=tk.E, padx=5, pady=5)

        # creating the Diastolic Value text label and input label
        diastolic_label = ttk.Label(self, text="Diastolic")
        diastolic_label.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)

        diastolic_entry = ttk.Entry(self)
        diastolic_entry.grid(row=2, column=1, sticky=tk.E, padx=5, pady=5)

        # def clicked():
        # button.configure(text="Clicked")

        # creating button and positioning it
        button = ttk.Button(self, text="Save", command='save')
        button.grid(row=3, column=1, sticky=W)

    # method to create the window
    def show_window(self):

        window = Tk()  # object/instance of the tkinter class
        window.geometry("300x150")  # setting the size of the window
        window.configure(bg='#006778')  # adding colour
        window.resizable(False, False)  # preventing the window from resizing
        window.title("Systolic & Diastolic Values")

        # configuring the window
        window.columnconfigure(0, weight=1)
        window.rowconfigure(0, weight=1)
