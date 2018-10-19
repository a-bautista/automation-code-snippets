''' Author: Alejandro Bautista Ramos
    Last modification date: March 18th, 2018 '''

# Python 3.5.2 and above
# win32com comes from the pywin32 package version 223-cp35

# Code to make the computer to speak
import os

import win32com.client as wincl

def main():
    text_to_say = computer_speaks(input("Please, type a something. The computer will read what you wrote. "))
    #runMacro()

def computer_speaks():
    announcement = wincl.Dispatch("SAPI.SpVoice")
    announcement.speak("Hello world!")

def runMacro():

    if os.path.exists("C:\\Users\\Dev\\Desktop\\Development\\completed_apps\\My_Macr_Generates_Data.xlsm"):
        # DispatchEx is required in the newest versions of Python.
        excel_macro = wincl.DispatchEx("Excel.application")
        excel_path = os.path.expanduser("C:\\Users\\Dev\\Desktop\\Development\\completed_apps\\My_Macr_Generates_Data.xlsm")
        workbook = excel_macro.Workbooks.Open(Filename = excel_path, ReadOnly =1)
        excel_macro.Application.Run("ThisWorkbook.Template2G")
        #Save the results in case you have generated data
        workbook.Save()
        excel_macro.Application.Quit()
        del excel_macro

if __name__ == "__main__":
    main()