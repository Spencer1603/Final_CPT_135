'''
Created on Dec 11, 2018

@author: M.Spencer, M. Reilling, A. Hicks
'''
#option 1:
'''
#Variables and constants
    self._userVar = ""
    self._varCurrent = []
    self._opCurrent = []

#Number Button Functions
def _9Press(self, _userVar):
    self._displayArea.insert(END, "9")
    self._userVar = str(self._userVar)
    self._userVar = self._userVar + "9"
    self._userVar = float(self._userVar)

#def _8Press - _0Press
         
   
#Operation Buttons
def _multiplyPress(self, _userVar):
    self._displayArea.insert(END, " * ")
    
    #possibility of modularizing this chunk (see below)
    self._varCurrent.append(self._userVar)
    self._userVar = ""
    decimalPressed = False
    
    self._opCurrent.append(" * ")
    
#'' we could do something like this
def _opperandPress(self,_userVar):
    self._userVar = float(self._userVar)
    self._varCurrent.append(self._userVar)
    self._userVar = ""
    decimalPressed = False
    
def _multiplyPress(self, _userVar):
    self._displayArea.insert(END, " * ")
    self._opperandPress(_userVar)
    self._opCurrent.append(" * ")
#''
  
#def other operands

 
def _equalPress(self, _userVar, _varCurrent, _opCurrent):
    if self._userVar != "":   
        self._userVar =  float(self._userVar)
        self._varCurrent.append(self._userVar)
        self._userVar = ""
        
    self._currentNum = 0.0
    self._prevNum = 0.0
    self._operand = ""
    
    i = 0
    x = 0
    y = 1
        
    for i in range(len(_varCurrent)): 
        if i == 0:
            self._prevNum = self._varCurrent[i]
            
        elif i == y:
            self._currentNum = self._varCurrent[i]  
        
        else:
            for x in range(len(_opCurrent)):
                if x == 0:
                    self._operand = self._opCurrent[i]
                
                if self._operand == " * ":
                    self._prevNum = self._prevNum * self._currentNum
                    
                #Def other funtions
            
            
                
     self._displayArea.insert(END, self._prevNum)
'''    
     
#option 2

from tkinter import *
import tkinter.messagebox
import math
import os.path

class Calculator(Frame):

    def __init__(self):
    #Variables and constants
        self._userVar = ""
        self._varCurrent = []
        
        Frame.__init__(self)
        self.master.title("Text Editor")
        self.grid()
        
        self._display = Frame(self)
        self._display.grid(row = 0, column = 0, rowspan = 2, columnspan = 5, sticky = N+S+E+W)
        self._displayArea = Text(self._display, width = 80, height = 10)
        self._displayArea.grid(row = 0, column = 0, sticky = N+S+E+W)
        
        #Number Buttons
        self._9Btn = Button(self, text = "9", command = self._numPress(_val="9"))
        self._9Btn.grid(row = 4, column = 2)
        
        self._8Btn = Button(self, text = "8", command = self._numPress(_val="8"))
        self._8Btn.grid(row = 4, column = 1)
        
        self._7Btn = Button(self, text = "7", command = self._numPress(_val="7"))
        self._7Btn.grid(row = 4, column = 0)
        
        self._6Btn = Button(self, text = "6", command = self._numPress(_val="6"))
        self._6Btn.grid(row = 5, column = 2)
        
        self._5Btn = Button(self, text = "5", command = self._numPress(_val="5"))
        self._5Btn.grid(row = 5, column = 1)
        
        self._4Btn = Button(self, text = "4", command = self._numPress(_val="4"))
        self._4Btn.grid(row = 5, column = 0)

        self._3Btn = Button(self, text = "3", command = self._numPress(_val="3"))
        self._3Btn.grid(row = 6, column = 2)
        
        self._2Btn = Button(self, text = "2", command = self._numPress(_val="2"))
        self._2Btn.grid(row = 6, column = 1)
        
        self._1Btn = Button(self, text = "1", command = self._numPress(_val="1"))
        self._1Btn.grid(row = 6, column = 0)
        
        self._0Btn = Button(self, text = "0", command = self._numPress(_val="0"))
        self._0Btn.grid(row = 7, column = 0)
        
        #in case above doesnt work
        '''
        self._9Btn = Button(self, text = "9", command = self._9Press(self._userVar, _val="9"))
        self._9Btn.grid(row = 4, column = 2)
        
        self._8Btn = Button(self, text = "8", command = self._8Press(self._userVar, _val="8"))
        self._8Btn.grid(row = 4, column = 1)
        
        self._7Btn = Button(self, text = "7", command = self._7Press(self._userVar, _val="7"))
        self._7Btn.grid(row = 4, column = 0)
        
        self._6Btn = Button(self, text = "6", command = self._6Press(self._userVar, _val="6"))
        self._6Btn.grid(row = 5, column = 2)
        
        self._5Btn = Button(self, text = "5", command = self._5Press(self._userVar, _val="5"))
        self._5Btn.grid(row = 5, column = 1)
        
        self._4Btn = Button(self, text = "4", command = self._4Press(self._userVar, _val="4"))
        self._4Btn.grid(row = 5, column = 0)

        self._3Btn = Button(self, text = "3", command = self._3Press(self._userVar, _val="3"))
        self._3Btn.grid(row = 6, column = 2)
        
        self._2Btn = Button(self, text = "2", command = self._2Press(self._userVar, _val="2"))
        self._2Btn.grid(row = 6, column = 1)
        
        self._1Btn = Button(self, text = "1", command = self._1Press(self._userVar, _val="1"))
        self._1Btn.grid(row = 6, column = 0)
        
        self._0Btn = Button(self, text = "0", command = self._0Press(self._userVar, _val="0")))
        self._0Btn.grid(row = 7, column = 0)
        '''
   
        self._multBtn = Button(self, text = "*", command = self._opPress(self._userVar, _val=" * "))
        self._multBtn.grid(row = 3, column = 4)
        
        self._divBtn = Button(self, text = "/", command = self._opPress(self._userVar, _val=" / "))
        self._divBtn.grid(row = 4, column = 4)
        
        self._addBtn = Button(self, text = "+", command = self._opPress(self._userVar, _val=" + "))
        self._addBtn.grid(row = 5, column = 4)
        
        self._subBtn = Button(self, text = "-", command = self._opPress(self._userVar, _val=" - "))
        self._subBtn.grid(row = 6, column = 4)
        
        
        self._equalBtn = Button(self, text = "=", command = self._equalPress(self._userVar, self._varCurrent, session))
        self._equalBtn.grid(row = 7, column = 4)
    
    #Number Button Functions
    def _numPress(self, _val=""):
        self._displayArea.insert(END, _val)
        self._userVar = self._userVar + _val
    
    #in case above doesnt work
    '''
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
    '''
        
    #Operation Buttons
    def _opPress(self, _userVar, _val=""):
        self._displayArea.insert(END, _val)
        self._varCurrent.append(self._userVar)
        self._userVar = ""
        self._varCurrent.append(_val)
        
    #def other operands
    
     
    def _equalPress(self, _userVar, _varCurrent, session):
        self._displayArea.insert(END, " = ")
        self._varCurrent.append(self._userVar)
        self._userVar = ""
        funcToWrite = "".join(self._varCurrent)
        
        #placeholder
        funcAnswer = 0.0
        
        self._displayArea.insert(END, str(funcAnswer))
        session.write(str(funcAnswer))

def main(): 
    Calculator().mainloop()
    
session = open('../memory.txt', 'w')    
main()
session.close()                      