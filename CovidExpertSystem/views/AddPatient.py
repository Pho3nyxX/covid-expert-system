import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *


class AddPatient (ttk.Frame):
    def __init__(self, container, underlying_cond_list=None, symptoms_list=None):
        super().__init__(container, padding="6 6 12 12")

        self.window_size = "800x650"
        self.email = tkinter.StringVar()
        self.street = tkinter.StringVar()
        self.parish = tkinter.StringVar()
        self.town = tkinter.StringVar()
        self.first_name = tkinter.StringVar()
        self.last_name = tkinter.StringVar()
        self.middle_name = tkinter.StringVar()
        self.contact = tkinter.StringVar()
        self.emergency_contact = tkinter.StringVar()
        self.workplace = tkinter.StringVar()
        self.dob = tkinter.StringVar()
        self.medication = tkinter.StringVar()
        self.gender = tkinter.StringVar()
        self.temperature = tkinter.DoubleVar()
        self.weight = tkinter.DoubleVar()
        self.height = tkinter.DoubleVar()
        self.systolic = tkinter.IntVar()
        self.diastolic = tkinter.IntVar()
        self.blurred = tkinter.StringVar()
        self.fainting = tkinter.StringVar()
        self.dizzy = tkinter.StringVar()

        self.dizzy.set("-- select --")
        self.blurred.set("-- select --")
        self.fainting.set("-- select --")

        self.underlying_cond_list_var = tkinter.StringVar(value=underlying_cond_list)
        self.symptoms_list_var = tkinter.StringVar(value=symptoms_list)

        # self.first_name = tkinter.StringVar()

        # ************ create columns *************
        first_column = ttk.Frame(self, borderwidth=1)
        first_column.grid(row=1, column=0)

        second_column = ttk.Frame(self, borderwidth=1)
        second_column.grid(row=1, column=1)

        third_column = ttk.Frame(self, borderwidth=1)
        third_column.grid(row=1, column=2)

        self.bp_row = ttk.Frame(third_column, borderwidth=1, padding=0)
        self.bp_row.grid(row=10, column=0, columnspan=2)

        bottom_row = ttk.Frame(self, borderwidth=1)
        bottom_row.grid(row=2, column=2, columnspan=3)

        # ***************first column starts here******************************

        # creating first label and positioning it
        covid_label = ttk.Label(self, text="Covid Expert System")
        covid_label.grid(row=0, column=0, columnspan=3)

        # creating the First Name text label and input label
        first_name_label = ttk.Label(first_column, text="First Name")
        first_name_label.grid(column=0, row=1, sticky=E, padx=5, pady=5)

        first_name_entry = ttk.Entry(first_column, textvariable=self.first_name)
        first_name_entry.grid(column=1, row=1, sticky=W, padx=5, pady=5)

        # creating the Middle Name text label and input label
        middle_name_label = ttk.Label(first_column, text="Middle Name")
        middle_name_label.grid(row=2, column=0, sticky=E, padx=5, pady=5)

        middle_name_entry = ttk.Entry(first_column, textvariable=self.middle_name)
        middle_name_entry.grid(row=2, column=1, sticky=W, padx=5, pady=5)

        # creating the Last Name text label and input label
        last_name_label = ttk.Label(first_column, text="Last Name")
        last_name_label.grid(row=3, column=0, sticky=E, padx=5, pady=5)

        last_name_entry = ttk.Entry(first_column, textvariable=self.last_name)
        last_name_entry.grid(row=3, column=1, sticky=W, padx=5, pady=5)

        # creating the Age text label and input label
        # age_label = ttk.Label(self, text="Age")
        # age_label.grid(row=4, column=0, sticky=E, padx=5, pady=5)
        #
        # age_entry = ttk.Entry(self)
        # age_entry.grid(row=4, column=1, sticky=W, padx=5, pady=5)

        # creating the Contact text label and input label
        contact_label = ttk.Label(first_column, text="Contact")
        contact_label.grid(row=5, column=0, sticky=E, padx=5, pady=5)

        contact_entry = ttk.Entry(first_column, textvariable=self.contact)
        contact_entry.grid(row=5, column=1, sticky=W, padx=5, pady=5)

        # creating the Emergency Contact text label and input label
        emergency_contact_label = ttk.Label(first_column, text="Emergency Contact")
        emergency_contact_label.grid(row=6, column=0, sticky=E, padx=5, pady=5)

        emergency_contact_entry = ttk.Entry(first_column, textvariable=self.emergency_contact)
        emergency_contact_entry.grid(row=6, column=1, sticky=W, padx=5, pady=5)

        # creating the Number of Persons in Home text label and input label
        num_of_person_label = ttk.Label(first_column, text="# of Persons in Home")
        num_of_person_label.grid(row=7, column=0, sticky=E, padx=5, pady=5)

        num_of_person_entry = ttk.Entry(first_column)
        num_of_person_entry.grid(row=7, column=1, sticky=W, padx=5, pady=5)

        # creating the Workplace text label and input label
        workplace_label = ttk.Label(first_column, text="Workplace")
        workplace_label.grid(row=7, column=0, sticky=E, padx=5, pady=5)

        workplace_entry = Entry(first_column, textvariable=self.workplace)
        workplace_entry.grid(row=7, column=1, sticky=W, padx=5, pady=5)

        # creating the DoB text label and input label
        dob_label = ttk.Label(first_column, text="DoB")
        dob_label.grid(row=8, column=0, sticky=E, padx=5, pady=5)

        dob_entry = ttk.Entry(first_column, textvariable=self.dob)
        dob_entry.grid(row=8, column=1, sticky=W, padx=5, pady=5)

        # creating the Medication text label and input label
        medication_label = ttk.Label(first_column, text="Medication")
        medication_label.grid(row=9, column=0, sticky=E, padx=5, pady=5)

        medication_entry = ttk.Entry(first_column, textvariable=self.medication)
        medication_entry.grid(row=9, column=1, sticky=W, padx=5, pady=5)

        # creating the Email text label and input label
        email_label = ttk.Label(first_column, text="Email")
        email_label.grid(row=10, column=0, sticky=E, padx=5, pady=5)

        email_entry = ttk.Entry(first_column, textvariable=self.email)
        email_entry.grid(row=10, column=1, sticky=W, padx=5, pady=5)

        # ********************** ADDRESS ***********************************
        # creating the street text label and input label
        street_label = ttk.Label(first_column, text="Street")
        street_label.grid(row=11, column=0, sticky=E, padx=5, pady=5)

        street_entry = ttk.Entry(first_column, textvariable=self.street)
        street_entry.grid(row=11, column=1, sticky=W, padx=5, pady=5)

        # creating the parish text label and input label
        parish_label = ttk.Label(first_column, text="Parish")
        parish_label.grid(row=12, column=0, sticky=E, padx=5, pady=5)

        parish_entry = ttk.Entry(first_column, textvariable=self.parish)
        parish_entry.grid(row=12, column=1, sticky=W, padx=5, pady=5)

        # creating the town text label and input label
        town_label = ttk.Label(first_column, text="Town/City")
        town_label.grid(row=13, column=0, sticky=E, padx=5, pady=5)

        town_entry = ttk.Entry(first_column, textvariable=self.town)
        town_entry.grid(row=13, column=1, sticky=W, padx=5, pady=5)

        # creating the Gender text label and input label
        gender_label = ttk.Label(first_column, text="Gender")
        gender_label.grid(row=14, column=0, sticky=E, padx=5, pady=5)

        gender_entry = ttk.Entry(first_column)
        gender_entry.grid(row=14, column=1, sticky=W, padx=5, pady=5)

        # creating the Weight text label and input label
        weight_label = ttk.Label(first_column, text="Weight")
        weight_label.grid(row=15, column=0, sticky=E, padx=5, pady=5)

        weight_entry = ttk.Entry(first_column, textvariable=self.weight)
        weight_entry.grid(row=15, column=1, sticky=W, padx=5, pady=5)

        # creating the Height text label and input label
        height_label = ttk.Label(first_column, text="Height")
        height_label.grid(row=16, column=0, sticky=E, padx=5, pady=5)

        height_entry = ttk.Entry(first_column, textvariable=self.height)
        height_entry.grid(row=16, column=1, sticky=W, padx=5, pady=5)

        # ***************second column starts here******************************
        symptom_label = ttk.Label(second_column, text="Symptoms")
        symptom_label.grid(row=0, column=0, sticky=W, padx=5, pady=5)

        # scrollbar = ttk.Scrollbar(second_column, orient= 'vertical')
        # scrollbar.grid(row=1, column=2, sticky=W, padx=5, pady=5)
        self.symptom_list = Listbox(second_column,
                                    height=12,
                                    width=32,
                                    selectmode="extended",
                                    exportselection=False,
                                    listvariable=self.symptoms_list_var)
        self.symptom_list.grid(row=1, column=0, sticky=W, padx=5, pady=5)
        # symptom_list.config(yscrollcommand=scrollbar.set)

        underlying_label = ttk.Label(second_column, text="Underlying Condition")
        underlying_label.grid(row=2, column=0, sticky=W, padx=5, pady=5)

        self.underlying_list = Listbox(second_column, height=12, width=32,
                                       selectmode="extended",
                                       exportselection=False,
                                       listvariable=self.underlying_cond_list_var)
        self.underlying_list.grid(row=3, column=0, sticky=W, padx=5, pady=5)

        # ****************************additional info section***************************************

        # additional info
        addition_label = ttk.Label(third_column, text="Add Additional Information", font=("Arial Bold", 10))
        addition_label.grid(row=0, column=1, columnspan=2)

        # medication history info
        medication_label = ttk.Label(third_column, text="Medication History")
        medication_label.grid(row=1, column=0, sticky=E, padx=5, pady=5)

        medication_text = Text(third_column, height=4, width=20)
        medication_text.grid(row=1, column=1, sticky=E, padx=5, pady=5)

        # temperature info
        temperature_label = ttk.Label(third_column, text="Temperature")
        temperature_label.grid(row=3, column=0, sticky=E, padx=5, pady=5)

        temperature_entry = ttk.Entry(third_column, textvariable=self.temperature)
        temperature_entry.grid(row=3, column=1, sticky=W, padx=5, pady=5)

        # Dizziness label
        dizzy_label = ttk.Label(third_column, text="Dizziness ")
        dizzy_label.grid(row=6, column=0, sticky=E, padx=5, pady=5)
        # combo creation
        dizzy_combo = ttk.Combobox(third_column, width=24, state="readonly", textvariable=self.dizzy)
        # Adding combo dropdown list
        dizzy_combo['values'] = (' Yes', ' No')
        dizzy_combo.grid(row=6, column=1, sticky=W, padx=5, pady=5)
        dizzy_combo.current()

        # fainting label
        fainting_label = ttk.Label(third_column, text="Fainting ")
        fainting_label.grid(row=7, column=0, sticky=E, padx=5, pady=5)
        # combo creation
        fainting_combo = ttk.Combobox(third_column, width=24, state="readonly", textvariable=self.fainting)
        # Adding combo dropdown list
        fainting_combo['values'] = (' Yes', ' No')
        fainting_combo.grid(row=7, column=1, sticky=W, padx=5, pady=5)
        fainting_combo.current()

        # blurred vision label
        blurred_label = ttk.Label(third_column, text="Blurred Vision ")
        blurred_label.grid(row=9, column=0, sticky=E, padx=5, pady=5)
        # combo creation

        blurred_combo = ttk.Combobox(third_column, width=24, state="readonly", textvariable=self.blurred)
        # Adding combo dropdown list
        blurred_combo['values'] = (' Yes', ' No')
        blurred_combo.grid(row=9, column=1, sticky=W, padx=5, pady=5)
        blurred_combo.current()

        # Blood pressure
        # systolic info
        systolic_label = ttk.Label(self.bp_row, text="Systolic")
        systolic_label.grid(row=0, column=0, sticky=E, padx=5, pady=5)

        systolic_entry = ttk.Entry(self.bp_row, textvariable=self.systolic)
        systolic_entry.grid(row=0, column=1, sticky=W, padx=5, pady=5)

        # systolic info
        diastolic_label = ttk.Label(self.bp_row, text="Diastolic")
        diastolic_label.grid(row=1, column=0, sticky=E, padx=5, pady=5)

        diastolic_entry = ttk.Entry(self.bp_row, textvariable=self.diastolic)
        diastolic_entry.grid(row=1, column=1, sticky=W, padx=5, pady=5)


        # smoke label
        smoke_label = ttk.Label(third_column, text="Smoke ")
        smoke_label.grid(row=11, column=0, sticky=E, padx=5, pady=5)
        # combo creation
        first = tkinter.StringVar()
        smoke_combo = ttk.Combobox(third_column, width=24, state="readonly", textvariable=first)
        # Adding combo dropdown list
        smoke_combo['values'] = (' Yes', ' No')
        smoke_combo.grid(row=11, column=1, sticky=W, padx=5, pady=5)
        smoke_combo.current()

        # exercise label
        exercise_label = ttk.Label(third_column, text="Exercise ")
        exercise_label.grid(row=12, column=0, sticky=E, padx=5, pady=5)
        # combo creation
        second = tkinter.StringVar()
        exercise_combo = ttk.Combobox(third_column, width=24, state="readonly", textvariable=second)
        # Adding combo dropdown list
        exercise_combo['values'] = (' Yes', ' No')
        exercise_combo.grid(row=12, column=1, sticky=W, padx=5, pady=5)
        exercise_combo.current()

        # salt intake label
        salt_label = ttk.Label(third_column, text="Salt Intake ")
        salt_label.grid(row=13, column=0, sticky=E, padx=5, pady=5)
        # combo creation
        third = tkinter.StringVar()
        salt_combo = ttk.Combobox(third_column, width=24, state="readonly", textvariable=third)
        # Adding combo dropdown list
        salt_combo['values'] = (' Heavy', ' Light')
        salt_combo.grid(row=13, column=1, sticky=W, padx=5, pady=5)
        salt_combo.current()


        self.bp_row.pack_forget()

        # ****************************button section***************************************

        # def clicked():
        # button.configure(text="Clicked")

        # creating button and positioning it
        self.save_button = ttk.Button(bottom_row, text="Save")
        self.save_button.grid(row=0, column=0, sticky=E)

        # creating button and positioning it
        self.cancel_button = ttk.Button(bottom_row, text="Cancel")
        self.cancel_button.grid(row=0, column=1, sticky=E)

        self.grid(column=0, row=0, sticky="N, W, E, S")


    # method to create the window

    def show_window(self):

        window = Tk()  # object/instance of the tkinter class
        window.geometry("800x650")  # setting the size of the window
        window.configure(bg='#006778')  # adding colour
        window.resizable(False, False)  # preventing the window from resizing
        window.title("Add New Patient")

        # configuring the window
        window.columnconfigure(0, weight=1)
        window.rowconfigure(0, weight=1)



