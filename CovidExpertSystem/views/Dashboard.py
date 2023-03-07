import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *


class Dashboard(ttk.Frame):
    def __init__(self, container):
        super().__init__(container, padding="6 6 12 12")

        self.window_size = "800x650"


        # creating login_button and positioning it
        self.new_patient_button = ttk.Button(self, text="New patient")
        self.new_patient_button.grid(row=1, column=1, sticky=E)

        # creating login_button and positioning it
        self.new_symptom_button = ttk.Button(self, text="Add Symptom")
        self.new_symptom_button.grid(row=1, column=2, sticky=E)

        self.grid(column=0, row=0, sticky="N, W, E, S")

    def get_window_size(self):
        return self.window_size