import random
from tkinter import * # pylint: disable=W0614
import pyperclip
import os
from gui import guiInit
# pylint: disable=W0612
# pylint: disable=E1103

class PasswordGenerator():

    def __init__(self, root):
        # the gui setup
        guiInit(self, root)
        

    def generatePassword(self):
        # generates the password from the lists below of your choosing and according to the length set
        # outputs the password into the entry box by the generate button as well as printing it to the terminal

        numbersList = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        lowercaseList = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        uppercaseList = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        specialList = ["@", "#", "£", "$", "%", "?"]
        lists = []

        if self.includeNumbersVar.get() == 1:
            lists.append(numbersList)
        if self.includeLowercaseVar.get() == 1:
            lists.append(lowercaseList)
        if self.includeUppercaseVar.get() == 1:
            lists.append(uppercaseList)
        if self.includeSpecialVar.get() == 1:
            lists.append(specialList)

        length = self.passwordLengthVar.get()
        

        password = ""
        
        if len(lists) == 0:
            self.generatePasswordVar.set(value="check at least one box!")
        else:
            for i in range(length): 
                category = random.choice(lists)
                #print(category)
                password += random.choice(category)
                #print(password)

            print("this is the generated password: " + str(password))
            print(len(password))
            self.generatePasswordVar.set(value=password)

            # copies the generated password to the clipboard so you can just paste it without copying it first
            pyperclip.copy(password)

            # displays the below message in the title bar for 2 seconds
            root.title("Password copied to clipboard!")
            
            def changeTitle():
                root.title("Password Generator")


            root.after(2000, changeTitle)



root = Tk()
root.title("Password Generator")
try:
    root.iconbitmap(os.path.abspath(os.path.dirname(__file__)) + "/PasswordGenerator.ico")
except:
    print("failed to load the windows icon")
program = PasswordGenerator(root)
root.mainloop()