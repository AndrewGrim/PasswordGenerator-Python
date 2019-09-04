import random
from tkinter import * # pylint: disable=W0614
import os
import platform

from gui import guiInit
# pylint: disable=W0612
# pylint: disable=E1103

systemOS = platform.platform().lower()
firstDash = systemOS.find("-")
systemOS = systemOS[:firstDash]

class PasswordGenerator():

    def __init__(self, root):
        # the gui setup
        guiInit(self, root)
        

    def generatePassword(self):
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
                password += random.choice(category)

            print("this is the generated password: " + str(password))
            print(len(password))
            self.generatePasswordVar.set(value=password)
            root.clipboard_clear()
            root.clipboard_append(password)
            root.title("Password copied to clipboard!")
            
            def changeTitle():
                root.title("Password Generator")


            root.after(2000, changeTitle)


root = Tk()
root.title("Password Generator")
if systemOS == "windows":
    try:
        root.iconbitmap(os.getcwd() + "/images/PasswordGenerator.ico")
    except:
        print("windows icon not found in the local directory!")
elif systemOS == "linux":
    try:
        icon = PhotoImage(file="/images/PasswordGenerator.png")
        root.tk.call("wm", "iconphoto", root._w, icon)
    except:
        print("linux icon not found in the local directory!")
program = PasswordGenerator(root)
root.mainloop()