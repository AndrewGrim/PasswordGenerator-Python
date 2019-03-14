import random
import pyperclip

numbersList = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
lowercaseList = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
uppercaseList = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
specialList = ["@", "#", "£", "$", "%", "?"]
lists = [numbersList, lowercaseList, uppercaseList, specialList]

length = 16

password = ""

for i in range(length): #pylint: disable=W0612
    category = random.choice(lists)
    #print(category)
    password += random.choice(category)
    #print(password)

print("this is the generated password: " + str(password))
print(len(password))

# copies the generated password to the clipboard so you can just paste it without copying it first
pyperclip.copy(password)
