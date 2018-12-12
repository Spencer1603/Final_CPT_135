'''
Created on Dec 11, 2018

@author: M.Spencer, M. Reilling, A. Hicks
'''

from tkinter import *
import tkinter.messagebox
import math
import os.path

class Calculator(Frame):
    def __init__(self):
        #Variables and constants
        self._userVar = ""
        self._varCurrent = []
        self._opCurrent = []
        
        '''
        x = 0.0
        PI = math.pi(x)
        SINE = math.sin(x)
        COSINE = math.cos(x)
        TANGEANT = math.tan(x)
        '''
        
        self._decimalPressed = False
       #self._endParenNeeded = 0
        
        #Setup window and widgets
        Frame.__init__(self)
        self.master.title("Text Editor")
        self.grid()
        
        self._display = Frame(self)
        self._display.grid(row = 0, column = 0, rowspan = 2, columnspan = 5, sticky = N+S+E+W)
        self._displayArea = Text(self._display, width = 80, height = 10)
        self._displayArea.grid(row = 0, column = 0, sticky = N+S+E+W)
        
        #Number Buttons
        self._9Btn = Button(self, text = "9", command = self._9Press(self._userVar))
        self._9Btn.grid(row = 4, column = 2)
        
        self._8Btn = Button(self, text = "8", command = self._8Press(self._userVar))
        self._8Btn.grid(row = 4, column = 1)
        
        self._7Btn = Button(self, text = "7", command = self._7Press(self._userVar))
        self._7Btn.grid(row = 4, column = 0)
        
        self._6Btn = Button(self, text = "6", command = self._6Press(self._userVar))
        self._6Btn.grid(row = 5, column = 2)
        
        self._5Btn = Button(self, text = "5", command = self._5Press(self._userVar))
        self._5Btn.grid(row = 5, column = 1)
        
        self._4Btn = Button(self, text = "4", command = self._4Press(self._userVar))
        self._4Btn.grid(row = 5, column = 0)

        self._3Btn = Button(self, text = "3", command = self._3Press(self._userVar))
        self._3Btn.grid(row = 6, column = 2)
        
        self._2Btn = Button(self, text = "2", command = self._2Press(self._userVar))
        self._2Btn.grid(row = 6, column = 1)
        
        self._1Btn = Button(self, text = "1", command = self._1Press(self._userVar))
        self._1Btn.grid(row = 6, column = 0)
        
        self._0Btn = Button(self, text = "0", command = self._0Press(self._userVar))
        self._0Btn.grid(row = 7, column = 0)
        
        #Decimal button, and parenthesis buttons
        self._decimalBtn = Button(self, text = ".", command = self._decimalPress(self._userVar, self._decimalPressed))
        self._decimalBtn.grid(row = 7, column = 1)
        
        '''
        self._parenBtn = Button(self, text = "(", command = self._parenPress)
        self._parenBtn.grid(row = 3, column = 3)
        
        self._endParenBtn = Button(self, text = ")", command = self._endParenPress)
        self._endParenBtn.grid(row = 3, column = 4)
        '''
        
        self._negativeBtn = Button(self, text = ")", command = self._negativePress)
        self._negativeBtn.grid(row = 7, column = 4)
        
        
        #Operation Buttons
        self._multiplyBtn = Button(self, text = "*", command = self._multiplyPress(self._userVar))
        self._multiplyBtn.grid(row = 4, column = 4)
        
        self._divideBtn = Button(self, text = "/", command = self._dividePress(self._userVar))
        self._divideBtn.grid(row = 5, column = 4)
        
        self._addBtn = Button(self, text = "+", command = self._addPress(self._userVar))
        self._addBtn.grid(row = 6, column = 4)
        
        self._subtractBtn = Button(self, text = "-", command = self._subtractPress(self._userVar))
        self._subtractBtn.grid(row = 7, column = 4)
        
        self.equalBtn = Button(self, text = "=", command = self._equalPress(self._userVar, self._varCurrent, self._opCurrent))
        self._subtractBtn.grid(row = 7, column = 5)
        
        '''
        self._sineBtn = Button(self, text = "SIN", command = self._sinePress)
        self._sineBtn.grid(row = 3, column = 0)

        self._cosineBtn = Button(self, text = "COS", command = self._cosinePress)
        self._cosineBtn.grid(row = 3, column = 1)

        self._tangeantBtn = Button(self, text = "TAN", command = self._tangeantPress)
        self._tangeantBtn.grid(row = 3, column = 2)
        '''
    
    #Number Button Functions
    def _9Press(self, _userVar):
        self._displayArea.insert(END, "9")
        self._userVar = self._userVar + "9"

    def _8Press(self, _userVar):
        self._displayArea.insert(END, "8")
        self._userVar = self._userVar + "8"

    def _7Press(self, _userVar):
        self._displayArea.insert(END, "7")
        self._userVar = self._userVar + "7"
        
    def _6Press(self, _userVar):
        self._displayArea.insert(END, "6")
        self._userVar = self._userVar + "6"
    
    def _5Press(self, _userVar):
        self._displayArea.insert(END, "5")
        self._userVar = self._userVar + "5"
    
    def _4Press(self, _userVar):
        self._displayArea.insert(END, "4")
        self._userVar = self._userVar + "4"
    
    def _3Press(self, _userVar):
        self._displayArea.insert(END, "3")
        self._userVar = self._userVar + "3"
    
    def _2Press(self, _userVar):
        self._displayArea.insert(END, "2")
        self._userVar = self._userVar + "2"
    
    def _1Press(self, _userVar):
        self._displayArea.insert(END, "1")
        self._userVar = self._userVar + "1"
    
    def _0Press(self, _userVar):
        self._displayArea.insert(END, "0")
        self._userVar = self._userVar + "0"
    
    #Decimal button function
    def _decimalPress(self, _userVar, decimalPressed):
        if not decimalPressed:
            self._displayArea.insert(END, ".")
            self._userVar = self._userVar + "."
            decimalPressed = True
        else:
            tkinter.messagebox("You already have a decimal pressed for this number.")
        
    #Negative sign button function
    def _negativePress(self, _userVar):
        self._displayArea.insert(1.0, "-")
        self._userVar = float(self._userVar)
        self._userVar = -self._userVar
        self._userVar = str(self._userVar)
    
    #not sure how to get these to work yet
    '''   
    #Parenthesis buttons functions
    def _parenPress(self, userVar, endParenNeeded):   
        self._displayArea.insert(END, "(")
        userVar = float(userVar)
        self._varCurrent.append(userVar)
        self._opCurrent.append("(")
        userVar = "("
        decimalPressed = False
        endParenNeeded += 1
        
    #Parenthesis buttons functions
    def _endParenPress(self, userVar, decimalPressed, endParenNeeded):   
        self._displayArea.insert(END, ")")
        self._userVar = userVar + ")"
        userVar = float(userVar)
        self._varCurrent.append(userVar)
        self._opCurrent.append(")")
        userVar = ""
        decimalPressed = False
        endParenNeeded -= 1
    ''' 
    
    #Operation Buttons
    def _multiplyPress(self, _userVar):
        if self._userVar == "":
            self._userVar = 0.0
        self._displayArea.insert(END, " * ")
        self._userVar = float(self._userVar)
        self._varCurrent.append(self._userVar)
        self._opCurrent.append(" * ")
        self._userVar = ""
        decimalPressed = False
    
    def _dividePress(self, _userVar):
        if self._userVar == "":
            self._userVar = 0.0
        self._displayArea.insert(END, " / ")
        self._userVar = float(self._userVar)
        self._varCurrent.append(self._userVar)
        self._opCurrent.append(" / ")
        self._userVar = ""
        decimalPressed = False
    
    def _addPress(self, _userVar):
        if self._userVar == "":
            self._userVar = 0.0
        self._displayArea.insert(END, " + ")
        self._userVar = float(self._userVar)
        self._varCurrent.append(self._userVar)
        self._opCurrent.append(" + ")
        self._userVar = ""
        decimalPressed = False
    
    def _subtractPress(self, _userVar):
        if self._userVar == "":
            self._userVar = 0.0
        self._displayArea.insert(END, " - ")
        self._userVar = float(self._userVar)
        self._varCurrent.append(self._userVar)
        self._opCurrent.append(" - ")
        self._userVar = ""
        decimalPressed = False
        
    #def _sinePress(self):
    #self._displayArea.insert(END, "sin(")
    #_parenPress()
        
    #def _cosinePress(self):
        #self._displayArea.insert(END, "cos(")
    
    #def _tangeantPress(self):
        #self._displayArea.insert(END, "tan(")
        
    #def _piPress(self):
    #self._displayArea.insert(END, "pi")    
     
    def _equalPress(self, _userVar, _varCurrent, _opCurrent):
        if self._userVar == "":
            self._userVar = 0.0
        self._displayArea.insert(END, " = ")
        self._userVar = float(self._userVar)
        self._varCurrent.append(self._userVar)
        self._opCurrent.append(" = ")
        self._userVar = ""
        decimalPressed = False
    


def main(): 
    Calculator().mainloop()

main()
