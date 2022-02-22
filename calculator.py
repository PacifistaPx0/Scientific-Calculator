import math
import tkinter

from tkinter import *



class Calc():
    def __init__(self):
        self.total = 0
        self.current = ""
        self.input_value = True
        self.check_sum = False
        self.op = ""
        self.result = False

    # function for the display text
    def display(self, value):
        displaytxt.delete(0, END)
        displaytxt.insert(0, value)

    # function for C button
    def clear_Entry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value = True

    # function for CE button
    def clear_all_Entry(self):
        self.clear_Entry()
        self.total = 0

    # function for the plus and minus sign button
    def sign(self):
        self.result = FALSE
        self.current = -(float(displaytxt.get()))
        self.display(self.current)

    # function for squareroot button
    def squareroot(self):
        self.result = FALSE
        self.current = math.sqrt(float(displaytxt.get()))
        self.display(self.current)

    # function for square button 
    def squared(self):
        self.result = FALSE
        self.current = float(displaytxt.get()) ** 2
        self.display(self.current)

    # function for 10^x button
    def tenPower(self):
        self.result = False
        self.current = 10 ** float(displaytxt.get())
        self.display(self.current)

    # function for sin button
    def sin(self):
        self.result = False
        self.current = math.sin(float(displaytxt.get()))
        self.display(self.current)

    # function for cos button
    def cos(self):
        self.result = False
        self.current = math.cos(float(displaytxt.get()))
        self.display(self.current)

    # function for tan button
    def tan(self):
        self.result = False
        self.current = math.tan(float(displaytxt.get()))
        self.display(self.current)

    # function for pi button
    def pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)

       
    # function for log button
    def log(self):
        self.result = False
        self.current = math.log10(float(displaytxt.get()))
        self.display(self.current)
    
    # functio for delete button
    def Delete(self):
        text = displaytxt.get()[:-1]
        if text == "":
            text = "0"
        self.current = text
        self.display(self.current)

    # function for numbers
    def numberEnter(self, num):
        self.result = False
        firstnum = displaytxt.get()
        secondnum = str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value = False
        else:
            if secondnum == '.':
                if secondnum in firstnum:
                    return
            self.current = firstnum + secondnum
        self.display(self.current)

    # function for equals button
    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.valid_function()
        else:
            self.total = float(displaytxt.get())

    # function for confirming operations
    def valid_function(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "sub":
            self.total -= self.current
        if self.op == "multi":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        self.input_value = True
        self.check_sum = False
        self.display(self.total)

    # function for operation
    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False

added_value = Calc()
# adding GUI to calculator
root = Tk()
root.title("Richie's Calculator")
root.resizable(width = FALSE, height = FALSE)
calc = Frame(root, bg = "gray12")
calc.grid()

# creating the text field box
displaytxt = Entry(calc, relief = FLAT, font =('arial', 20, 'bold'), bg ="gray12", fg ="snow2", bd =50, width =20, justify =RIGHT)

# inserting the field box into the grid in the first row and column
displaytxt.grid(row = 0, column = 0, columnspan = 4, pady = 1)

# insert 0 as default value 
displaytxt.insert(0, "0")

# Buttons for first row
btnXSquared = Button(calc, relief = FLAT, bd=4, font =('arial', 20), width = 6, height = 1,
                  text ="x{}".format(u"\u00B2"), bg="gray8", fg = "snow2", command = added_value.squared).grid(row=1, column=0, padx=1, pady=2)
btnSin = Button(calc, relief = FLAT, bd=4, font =('arial', 20), width = 6, height = 1,
                  text ="sin", bg="gray8", fg = "snow2", command = added_value.sin).grid(row=1, column=1, padx=1, pady=2)
btnCos = Button(calc, relief = FLAT, bd=4, font =('arial', 20), width = 6, height = 1,
                  text ="cos", bg="gray8", fg = "snow2", command = added_value.cos).grid(row=1, column=2, padx=1, pady=2)
btnTan = Button(calc, relief = FLAT, bd=4, font =('arial', 20), width = 6, height = 1,
                  text ="tan", bg="gray8", fg = "snow2", command = added_value.tan).grid(row=1, column=3, padx=1, pady=2)

# Buttons for second row
btnSqrt = Button(calc, relief = FLAT, bd=4, font =('arial', 20), width = 6, height = 1,
                  text =u"\u221A", bg="gray8", fg = "snow2", command = added_value.squareroot).grid(row=2, column=0, padx=1, pady=2)
btnTenPower = Button(calc, relief = FLAT, bd=4, font =('arial', 20), width = 6, height = 1,
                  text ="10{}".format(u"\u02E3"), bg="gray8", fg = "snow2", command = added_value.tenPower).grid(row=2, column=1, padx=1, pady=2)
btnLog = Button(calc, relief = FLAT, bd=4, font =('arial', 20), width = 6, height = 1,
                  text ="log", bg="gray8", fg = "snow2", command = added_value.log).grid(row=2, column=2, padx=1, pady=2)
btnPi = Button(calc, relief = FLAT, bd=4, font =('arial', 20), width = 6, height = 1,
                  text =u"\u03C0", bg="gray8", fg = "snow2", command = added_value.pi).grid(row=2, column=3, padx=1, pady=2)


# Buttons for third row
btnClearEntry = Button(calc, relief = FLAT, bd=4, font =('arial', 20), width = 6, height = 1,
                  text ="CE", bg="gray8", fg = "snow2", command = added_value.clear_Entry).grid(row=3, column=0, padx=1, pady=2)
btnClear = Button(calc, relief = FLAT, bd=4, font =('arial', 20), width = 6, height = 1,
                  text ="C", bg="gray8", fg = "snow2", command = added_value.clear_all_Entry).grid(row=3, column=1, padx=1, pady=2)
btnDelete = Button(calc, relief = FLAT, bd=4, font =('arial', 20), width = 6, height = 1,
                  text =u"\u232B", bg="gray8", fg = "snow2", command = added_value.Delete).grid(row=3, column=2, padx=1, pady=2)
btnDivide = Button(calc, relief = FLAT, bd=4, font =('arial', 20), width = 6, height = 1,
                  text =u"\u00F7", bg="gray8", fg = "snow2", command = lambda: added_value.operation("divide")).grid(row=3, column=3, padx=1, pady=2)

# buttons for fourth row
btn7 = Button(calc, relief = FLAT, bd=4, font =('arial', 20), width = 6, height = 1,
                  text ="7", bg="black", fg = "snow2", command = lambda: added_value.numberEnter(7)).grid(row=4, column=0, padx=1, pady=2)
btn8 = Button(calc, relief = FLAT, bd=4, font =('arial', 20), width = 6, height = 1,
                  text ="8", bg="black", fg = "snow2", command = lambda: added_value.numberEnter(8)).grid(row=4, column=1, padx=1, pady=2)
btn9 = Button(calc, relief = FLAT, bd=4, font =('arial', 20), width = 6, height = 1,
                  text ="9", bg="black", fg = "snow2", command = lambda: added_value.numberEnter(9)).grid(row=4, column=2, padx=1, pady=2)
btnMultiply = Button(calc, relief = FLAT, bd=4, font =('arial', 20), width = 6, height = 1,
                  text =u"\u00D7", bg="gray8", fg = "snow2", command = lambda: added_value.operation("multi")).grid(row=4, column=3, padx=1, pady=2)

# buttons for fifth row
btn4 = Button(calc, relief = FLAT, bd=4, font =('arial', 20), width = 6, height = 1,
                  text ="4", bg="black", fg = "snow2", command = lambda: added_value.numberEnter(4)).grid(row=5, column=0, padx=1, pady=2)
btn5 = Button(calc, relief = FLAT, bd=4, font =('arial', 20), width = 6, height = 1,
                  text ="5", bg="black", fg = "snow2", command = lambda: added_value.numberEnter(5)).grid(row=5, column=1, padx=1, pady=2)
btn6 = Button(calc, relief = FLAT, bd=4, font =('arial', 20), width = 6, height = 1,
                  text ="6", bg="black", fg = "snow2", command = lambda: added_value.numberEnter(6)).grid(row=5, column=2, padx=1, pady=2)
btnMinus = Button(calc, relief = FLAT, bd=4, font =('arial', 20), width = 6, height = 1,
                  text =u"\u2212", bg="gray8", fg = "snow2", command = lambda: added_value.operation("sub")).grid(row=5, column=3, padx=1, pady=2)

# buttons for sixth row
btn1 = Button(calc, relief = FLAT, bd=4, font =('arial', 20), width = 6, height = 1,
                  text ="1", bg="black", fg = "snow2", command = lambda: added_value.numberEnter(1)).grid(row=6, column=0, padx=1, pady=2)
btn2 = Button(calc, relief = FLAT, bd=4, font =('arial', 20), width = 6, height = 1,
                  text ="2", bg="black", fg = "snow2", command = lambda: added_value.numberEnter(2)).grid(row=6, column=1, padx=1, pady=2)
btn3 = Button(calc, relief = FLAT, bd=4, font =('arial', 20), width = 6, height = 1,
                  text ="3", bg="black", fg = "snow2", command = lambda: added_value.numberEnter(3)).grid(row=6, column=2, padx=1, pady=2)
btnPlus = Button(calc, relief = FLAT, bd=4, font =('arial', 20), width = 6, height = 1,
                  text ="+", bg="gray8", fg = "snow2", command = lambda: added_value.operation("add")).grid(row=6, column=3, padx=1, pady=2)

# buttons for seventh row
btnSign = Button(calc, relief = FLAT, bd=4, font =('arial', 20), width = 6, height = 1,
                  text =u"\u00B1", bg="gray8", fg = "snow2", command = added_value.sign).grid(row=7, column=0, padx=1, pady=2)
btn0 = Button(calc, relief = FLAT, bd=4, font =('arial', 20), width = 6, height = 1,
                  text ="0", bg="black", fg = "snow2", command = lambda: added_value.numberEnter(0)).grid(row=7, column=1, padx=1, pady=2)
btnPoint = Button(calc, relief = FLAT, bd=4, font =('arial', 20), width = 6, height = 1,
                  text =".", bg="gray8", fg = "snow2", command = lambda: added_value.numberEnter(".")).grid(row=7, column=2, padx=1, pady=2)
btnEquals = Button(calc, relief = FLAT, bd=4, font =('arial', 20), width = 6, height = 1,
                  text ="=", bg="gray8", fg = "snow2", command = added_value.sum_of_total).grid(row=7, column=3, padx=1, pady=2)

if __name__ == "__main__":
    root.mainloop()
