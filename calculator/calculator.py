from tkinter import *
from tkinter.messagebox import *

class Calculator ():
    def __init __ (self):
        self.total = 0 #Retient or the total of operations is rendered
        self.current = "" #Contains the content of the display screen
        self.new_num = True #Recommences the number
        self.op_pending = False #If there is a pending operation
        self.op = "" # Operation to perform
        self.eq = False #When the equal key is pressed.

#Function to display the numbers on the screen
    def num_press (self, num):
        self.eq = False
        temp = text_box.get ()
        temp2 = str (num)
        if self.new_num:
            self.current = temp2
            self.new_num = False
        else:
            if temp2 == '.':
                if temp2 in temp:
                    return
            self.current = temp + temp2
        self.display (self.current)

#Function for the Equal key
    def calc_total (self):
        self.eq = True
        self.current = float (self.current)
        if self.op_pending == True:
            self.do_sum ()
        else:
            self.total = float (text_box.get ())

#Function to display on the screen
    def display (self, value):
        #You must write the code to display the information in the textbox.

#Function to calculate
#Dividing by 0 should show an error message "Can not Divide by 0."
    def do_sum (self):
        #You must set the code for the different operations of the calculator.
        #Dividing by 0 should show an error message "Can not Divide by 0."
        self.new_num = True
        self.op_pending = False
        self.display (self.total)

#Function to store the operation
    def operation (self, op):
        self.current = float (self.current)
        if self.op_pending:
            self.do_sum ()
        elif not self.eq:
            self.total = self.current
        self.new_num = True
        self.op_pending = True
        self.op = op
        self.eq = False

#Cancellation function (A / C button)
    def all_cancel (self):
        #You must write the code to reset the different variables.
        
#Function for percentages
    def calc_percent (self):
        self.current = float (self.current)
        self.current = (self.total * (self.current / 100))
        self.display (self.current)

#Function to change the numbers to positive and negative
    def sign (self):
        self.eq = False
        #You must write the code to change the sign of the entered number.

# Declaration of the "Calculator" application

# Text_box declaration (It's important to call it text_box)

# Declaration of buttons from 1 to 9

bttn_0 = Button (calc, text = "0", height = 3, width = 5)
#changer myCalc for the instance name of your calculator.
bttn_0 ["command"] = lambda: myCalc.num_press (0)
bttn_0.grid (row = 5, column = 0, columnspan = 2, pady = 1, sticky = N + S + E + W)

# Declaration of the other buttons.