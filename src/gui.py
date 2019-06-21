from tkinter import * #pylint: disable=W0614
from tkinter import ttk
# pylint: disable=W0612

class TTKSpinbox(ttk.Entry):
    # ttk.Spinbox was omitted from python version prior to 3.7
    # if the machine has python version prior to 3.7 this class will make it work as intended

    def __init__(self, master=None, **kw):

        ttk.Entry.__init__(self, master, "ttk::spinbox", **kw)
    def set(self, value):
        self.tk.call(self._w, "set", value)

def guiInit(self, root):
    # top frame which includes all the options such as length and each of the list from which the password is generated
    self.passwordOptionsFrame = Frame(root)
    self.passwordOptionsFrame.grid(row=0, column=0)

    self.passwordLengthVar = IntVar(value=16)
    try:
        self.passwordLengthButton = ttk.Spinbox(self.passwordOptionsFrame, from_=1, to=100, increment=1, textvariable=self.passwordLengthVar)
    except:
        self.passwordLengthButton = TTKSpinbox(self.passwordOptionsFrame, from_=1, to=100, increment=1, textvariable=self.passwordLengthVar)
        print("python version older than 3.7")
    self.passwordLengthButton.pack()

    self.includeNumbersVar = IntVar(value=1)
    self.includeNumbersCheck = ttk.Checkbutton(self.passwordOptionsFrame, text="Include numbers", variable=self.includeNumbersVar)
    self.includeNumbersCheck.pack(fill=X)

    self.includeLowercaseVar = IntVar(value=1)
    self.includeLowercaseCheck = ttk.Checkbutton(self.passwordOptionsFrame, text="Include lower case letters", variable=self.includeLowercaseVar)
    self.includeLowercaseCheck.pack(fill=X)

    self.includeUppercaseVar = IntVar(value=1)
    self.includeUppercaseCheck = ttk.Checkbutton(self.passwordOptionsFrame, text="Include upper case letters", variable=self.includeUppercaseVar)
    self.includeUppercaseCheck.pack(fill=X)

    self.includeSpecialVar = IntVar(value=1)
    self.includeSpecialCheck = ttk.Checkbutton(self.passwordOptionsFrame, text="Include special characters", variable=self.includeSpecialVar)
    self.includeSpecialCheck.pack(fill=X)


    # bottom frame which contains the generate button and the entry box used for output
    self.outputFrame = Frame(root)
    self.outputFrame.grid(row=1, column=0)

    self.generatepasswordButton = ttk.Button(self.outputFrame, text="Generate Password", command=self.generatePassword)
    self.generatepasswordButton.pack(side=LEFT)

    self.generatePasswordVar = StringVar(value="")
    self.generatedPasswordEntry = ttk.Entry(self.outputFrame, textvariable=self.generatePasswordVar, width=50, justify=CENTER)
    self.generatedPasswordEntry.pack(side=RIGHT)
