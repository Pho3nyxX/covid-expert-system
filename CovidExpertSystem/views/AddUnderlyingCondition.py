import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *


class AddUnderlyingCondition(ttk.Frame):
    def __init__(self, container):
        super().__init__(container, padding="6 6 12 12")
        self.symptomTxt = tkinter.StringVar()
        self.type_selected = tkinter.StringVar()
        self.save_success = tkinter.StringVar()
        self.window_size = "330x200"

        # creating first label and positioning it
        covid_label = ttk.Label(self, text="Add symtom/ Underlying condition")
        covid_label.grid(row=1, column=1, columnspan=2)

        # Underlying or Symptom label
        select_one_label = Label(self, text="Select the type of factor ")
        select_one_label.grid(row=3, column=1, sticky=W, padx=5, pady=5)

        # combo creation
        type_combo_box = ttk.Combobox(self, width=24, textvariable=self.type_selected)
        # Adding combo dropdown list
        type_combo_box['values'] = ('Underlying Condition', 'Symptoms')
        type_combo_box.grid(row=4, column=1, sticky=W)
        # type_combo_box.current()

        # ***************text area starts here*******************************************

        symptoms_label = ttk.Label(self, text="Symptom/Underlying condition")
        symptoms_label.grid(row=5, column=1, sticky=W, padx=5, pady=5)

        self.symptoms_text = ttk.Entry(self, textvariable=self.symptomTxt)
        self.symptoms_text.grid(row=6, column=1, sticky=W)

        # ****************************button section***************************************
        success_label = ttk.Label(self, textvariable=self.save_success)
        success_label.grid(row=7, column=1, sticky=W, padx=5, pady=5)

        # creating button and positioning it
        self.save_button = ttk.Button(self, text="Save", command='save')
        self.save_button.grid(row=9, column=1, sticky=E)

        # creating button and positioning it
        self.cancel_button = ttk.Button(self, text="Cancel", command='cancel')
        self.cancel_button.grid(row=9, column=2, sticky=E)

        # method to create the frame
        self.grid(column=0, row=0, sticky="N, W, E, S")
