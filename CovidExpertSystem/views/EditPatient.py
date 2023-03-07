from tkinter import *
from tkinter import ttk


class EditPatient(ttk.Frame):

    def __init__(self, container):
        super().__init__(container, padding="3 3 12 12");

        self.window_size = "520x650"

        # ***************first column starts here******************************

        # creating the First Name text label and input label
        first_name_label = ttk.Label(self, text="First Name")
        first_name_label.grid(row=1, column=0, sticky=E, padx=5, pady=5)

        first_name_entry = ttk.Entry(self)
        first_name_entry.grid(row=1, column=1, sticky=W, padx=5, pady=5)

        # creating the Middle Name text label and input label
        middle_name_label = ttk.Label(self, text="Middle Name")
        middle_name_label.grid(row=2, column=0, sticky=E, padx=5, pady=5)

        middle_name_entry = ttk.Entry(self)
        middle_name_entry.grid(row=2, column=1, sticky=W, padx=5, pady=5)

        # creating the Last Name text label and input label
        last_name_label = ttk.Label(self, text="Last Name")
        last_name_label.grid(row=3, column=0, sticky=E, padx=5, pady=5)

        last_name_entry = ttk.Entry(self)
        last_name_entry.grid(row=3, column=1, sticky=W, padx=5, pady=5)

        # creating the Age text label and input label
        age_label = ttk.Label(self, text="Age")
        age_label.grid(row=4, column=0, sticky=E, padx=5, pady=5)

        age_entry = ttk.Entry(self)
        age_entry.grid(row=4, column=1, sticky=W, padx=5, pady=5)

        # creating the Contact text label and input label
        contact_label = ttk.Label(self, text="Contact")
        contact_label.grid(row=5, column=0, sticky=E, padx=5, pady=5)

        contact_entry = ttk.Entry(self)
        contact_entry.grid(row=5, column=1, sticky=W, padx=5, pady=5)

        # creating the Emergency Contact text label and input label
        emergency_label = ttk.Label(self, text="Emergency Contact")
        emergency_label.grid(row=6, column=0, sticky=E, padx=5, pady=5)

        emergency_entry = ttk.Entry(self)
        emergency_entry.grid(row=6, column=1, sticky=W, padx=5, pady=5)

        # creating the Number of Persons in Home text label and input label
        num_of_person_label = ttk.Label(self, text="# of Persons in Home")
        num_of_person_label.grid(row=6, column=0, sticky=E, padx=5, pady=5)

        num_of_person_entry = ttk.Entry(self)
        num_of_person_entry.grid(row=6, column=1, sticky=W, padx=5, pady=5)

        # creating the Workplace text label and input label
        workplace_label = ttk.Label(self, text="Workplace")
        workplace_label.grid(row=7, column=0, sticky=E, padx=5, pady=5)

        workplace_entry = ttk.Entry(self)
        workplace_entry.grid(row=7, column=1, sticky=W, padx=5, pady=5)

        # creating the DoB text label and input label
        dob_label = ttk.Label(self, text="DoB")
        dob_label.grid(row=8, column=0, sticky=E, padx=5, pady=5)

        dob_entry = ttk.Entry(self)
        dob_entry.grid(row=8, column=1, sticky=W, padx=5, pady=5)

        # creating the Medication text label and input label
        medication_label = ttk.Label(self, text="Medication")
        medication_label.grid(row=9, column=0, sticky=E, padx=5, pady=5)

        medication_entry = ttk.Entry(self)
        medication_entry.grid(row=9, column=1, sticky=W, padx=5, pady=5)

        # creating the Email text label and input label
        email_label = ttk.Label(self, text="Email")
        email_label.grid(row=10, column=0, sticky=E, padx=5, pady=5)

        email_entry = ttk.Entry(self)
        email_entry.grid(row=10, column=1, sticky=W, padx=5, pady=5)

        # creating the Gender text label and input label
        gender_label = ttk.Label(self, text="Gender")
        gender_label.grid(row=11, column=0, sticky=E, padx=5, pady=5)

        gender_entry = ttk.Entry(self)
        gender_entry.grid(row=11, column=1, sticky=W, padx=5, pady=5)

        # creating the Weight text label and input label
        weight_label = ttk.Label(self, text="Weight")
        weight_label.grid(row=12, column=0, sticky=E, padx=5, pady=5)

        weight_entry = ttk.Entry(self)
        weight_entry.grid(row=12, column=1, sticky=W, padx=5, pady=5)

        # creating the Height text label and input label
        height_label = ttk.Label(self, text="Height")
        height_label.grid(row=13, column=0, sticky=E, padx=5, pady=5)

        height_entry = ttk.Entry(self)
        height_entry.grid(row=13, column=1, sticky=W, padx=5, pady=5)

        # ***************second column starts here******************************

        # creating the smoke text label and input label
        smoke_label = ttk.Label(self, text="Smoke")
        smoke_label.grid(row=1, column=2, sticky=W, padx=5, pady=5)

        smoke_entry = ttk.Entry(self)
        smoke_entry.grid(row=1, column=2, sticky=E, padx=5, pady=5)

        # creating the exercise text label and input label
        exercise_label = ttk.Label(self, text="Exercise")
        exercise_label.grid(row=2, column=2, sticky=W, padx=5, pady=5)

        exercise_entry = ttk.Entry(self)
        exercise_entry.grid(row=2, column=2, sticky=E, padx=5, pady=5)

        # creating the salt intake text label and input label
        salt_label = ttk.Label(self, text="Salt Intake")
        salt_label.grid(row=3, column=2, sticky=W, padx=5, pady=5)

        salt_entry = ttk.Entry(self)
        salt_entry.grid(row=3, column=2, sticky=E, padx=5, pady=5)

        # creating the temperature text label and input label
        temperature_label = ttk.Label(self, text="Temperature")
        temperature_label.grid(row=4, column=2, sticky=W, padx=5, pady=5)

        temperature_entry = ttk.Entry(self)
        temperature_entry.grid(row=4, column=2, sticky=E, padx=5, pady=5)

        # creating the Dizziness text label and input label
        dizzy_label = ttk.Label(self, text="Dizziness")
        dizzy_label.grid(row=5, column=2, sticky=W, pady=5, padx=5)

        dizzy_entry = ttk.Entry(self)
        dizzy_entry.grid(row=5, column=2, sticky=E, padx=5, pady=5)

        # creating the Fainting text label and input label
        fainting_label = ttk.Label(self, text="Fainting")
        fainting_label.grid(row=6, column=2, sticky=W, padx=5, pady=5)

        fainting_entry = ttk.Entry(self)
        fainting_entry.grid(row=6, column=2, sticky=E, padx=5, pady=5)

        # creating the Blurred Vision text label and input label
        blurred_label = ttk.Label(self, text="Blurred Vision")
        blurred_label.grid(row=7, column=2, sticky=W, padx=5, pady=5)

        blurred_entry = ttk.Entry(self)
        blurred_entry.grid(row=7, column=2, sticky=E, padx=5, pady=5)

        # creating the Systolic text label and input label
        systolic_label = ttk.Label(self, text="Systolic")
        systolic_label.grid(row=8, column=2, sticky=W, padx=5, pady=5)

        systolic_entry = ttk.Entry(self)
        systolic_entry.grid(row=8, column=2, sticky=E, padx=5, pady=5)

        # creating the Diastolic text label and input label
        diastolic_label = ttk.Label(self, text="Diastolic")
        diastolic_label.grid(row=9, column=2, sticky=W, padx=5, pady=5)

        diastolic_entry = ttk.Entry(self)
        diastolic_entry.grid(row=9, column=2, sticky=E, padx=5, pady=5)

        # creating the medical history text label and input label
        medical_label = ttk.Label(self, text="Medical History")
        medical_label.grid(row=10, column=2, sticky=W, padx=5, pady=5)

        medical_text = Text(self, height=4, width=20)
        medical_text.grid(row=11, column=2, sticky=E, padx=5, pady=5)

        # creating the symptom text label and input label
        symptom_label = ttk.Label(self, text="Symptoms")
        symptom_label.grid(row=12, column=2, sticky=W, padx=5, pady=5)

        symptom_text = Text(self, height=4, width=22)
        symptom_text.grid(row=13, column=2, sticky=E, padx=5, pady=5)

        # creating the underlying condition text label and input label
        underlying_label = ttk.Label(self, text="Underlying Condition")
        underlying_label.grid(row=14, column=0, sticky=W, padx=5, pady=5)

        underlying_text = Text(self, height=4, width=20)
        underlying_text.grid(row=14, column=1, sticky=E, padx=5, pady=5)

        # ****************************button section***************************************

        # def clicked():
        # button.configure(text="Clicked")

        # creating button and positioning it
        close_button = ttk.Button(self, text="Close")
        close_button.grid(row=14, column=2, sticky=E)

        # creating a frame and placing it inside the window
        self.grid(column=0, row=0, sticky="N, W, E, S")

    # method to create the window
    def show_window(self):

        window = Tk()  # object/instance of the tkinter class
        window.geometry("520x650")  # setting the size of the window
        window.configure(bg='#006778')  # adding colour
        window.resizable(False, False)  # preventing the window from resizing
        window.title("Patient")


        # configuring the window
        window.columnconfigure(0, weight=1)
        window.rowconfigure(0, weight=1)

        # creating first label and positioning it
        covid_label = ttk.Label(mainframe, text="Covid Expert System")
        covid_label.grid(row=0, column=0, columnspan=4)


        window.mainloop()