import random
from tkinter import * #pylint: disable=W0614
from tkinter import ttk
import pyperclip
import os

class PasswordGenerator():


    def __init__(self, root):
        # the gui setup

        # top frame which includes all the options such as length and each of the list from which the password is generated
        self.passwordOptionsFrame = Frame(root)
        self.passwordOptionsFrame.grid(row=0, column=0)

        self.passwordLengthVar = IntVar(value=16)
        self.passwordLengthButton = ttk.Spinbox(self.passwordOptionsFrame, from_=1, to=100, increment=1, textvariable=self.passwordLengthVar)
        self.passwordLengthButton.pack()

        self.includeNumbersVar = IntVar(value=1)
        self.includeNumbersCheck = ttk.Checkbutton(self.passwordOptionsFrame, text="Include numbers", variable=self.includeNumbersVar)
        self.includeNumbersCheck.pack(fill=X)

        self.includeLowercaseVar = IntVar(value=1)
        self.includeLowercaseCheck = ttk.Checkbutton(self.passwordOptionsFrame, text="Include lower case letters", variable=self.includeLowercaseVar)
        self.includeLowercaseCheck.pack(fill=X)

        self.includeUppercaseVar = IntVar(value=1)
        self.includeUppercaseCheck = ttk.Checkbutton(self.passwordOptionsFrame, text="Inlcude upper case letters", variable=self.includeUppercaseVar)
        self.includeUppercaseCheck.pack(fill=X)

        self.includeSpecialVar = IntVar(value=1)
        self.includeSpecialCheck = ttk.Checkbutton(self.passwordOptionsFrame, text="Inlcude special characters", variable=self.includeSpecialVar)
        self.includeSpecialCheck.pack(fill=X)


        # bottom frame which contains the generate button and the entry box used for output
        self.outputFrame = Frame(root)
        self.outputFrame.grid(row=1, column=0)

        self.generatepasswordButton = ttk.Button(self.outputFrame, text="Generate Password", command=self.generatePassword)
        self.generatepasswordButton.pack(side=LEFT)

        self.generatePasswordVar = StringVar(value="")
        self.generatedPasswordEntry = ttk.Entry(self.outputFrame, textvariable=self.generatePasswordVar, width=50, justify=CENTER)
        self.generatedPasswordEntry.pack(side=RIGHT)


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
            for i in range(length): #pylint: disable=W0612
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
    root.iconbitmap(os.path.abspath(os.path.dirname(__file__)) + "/passwordGeneratorIcon.ico")
except:
    print("failed to load the windows icon")
program = PasswordGenerator(root)
root.mainloop()

