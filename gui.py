
import tkinter
import tkinter.messagebox
import csv

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title('Employee Main Menu')
        self.main_window.geometry('600x400+100+200')
        self.button_frame = tkinter.Frame(self.main_window)

        self.main_window.configure(background='light blue')

        self.label = tkinter.Label

        self.my_button = tkinter.Button(self.main_window,
                                        text='Hourly', width=15)
        self.my_button.pack()

        self.my_button = tkinter.Button(self.main_window,
                                        text='Salary', width=15)
        self.my_button.pack()

        self.my_button = tkinter.Button(self.main_window,
                                        text='View Pay Information', width=25)
        self.my_button.pack()

        self.my_button = tkinter.Button(self.main_window,
                                        text='View Timecard', width=25)
        self.my_button.pack()

        self.my_button = tkinter.Button(self.main_window,
                                        text='Change Payment Method', width=25)
        self.my_button.pack()

        self.my_button = tkinter.Button(self.main_window,
                                        text='Process Payroll',
                                        command=self.do_something, width=20)
        self.my_button.pack()
        self.button_frame.pack(ipadx=2)

        self.my_button = tkinter.Button(self.main_window,
                                        text='Add Employee', width=20)

        self.my_button.pack()

        tkinter.mainloop()
        
    def do_something(self):
        tkinter.messagebox.showinfo('Process Payroll',
                                    'Run the Payroll')


my_gui = MyGUI()

