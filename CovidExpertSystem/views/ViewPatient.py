from tkinter import *
from tkinter import ttk


class ViewPatient(ttk.Frame):

    def __init__(self, container):
        super().__init__(container, padding="3 3 12 12")

        self.window_size = "300x150"

        # creating first label and positioning it
        covid_label = ttk.Label(self, text="Covid Expert System")
        covid_label.grid(row=0, column=0, columnspan=2)

        # creating the Patient Name text label and input label
        name_label = ttk.Label(self, text="Patient Name")
        name_label.grid(row=1, column=0, sticky=E, padx=5, pady=5)

        name_entry = ttk.Entry(self)
        name_entry.grid(row=1, column=1, sticky=W, padx=5, pady=5)

        # creating the DOB text label and input label
        dob_label = ttk.Label(self, text="DOB")
        dob_label.grid(row=2, column=0, sticky=E, padx=5, pady=5)

        dob_entry = ttk.Entry(self)
        dob_entry.grid(row=2, column=1, sticky=W, padx=5, pady=5)

        # def clicked():
        # view_button.configure(text="Clicked")

        # creating view_button and positioning it
        view_button = ttk.Button(self, text="View")
        view_button.grid(row=5, column=1, sticky=W)

        self.grid(column=0, row=0, sticky="N, W, E, S")


    # method to create the window
    def show_window(self):

        window = Tk()  # object/instance of the tkinter class
        window.geometry("300x150")  # setting the size of the window
        window.configure(bg='#006778')  # adding colour
        window.resizable(False, False)  # preventing the window from resizing
        window.title("View Patient")

        # configuring the window
        window.columnconfigure(0, weight=1)
        window.rowconfigure(0, weight=1)


        window.mainloop()
        