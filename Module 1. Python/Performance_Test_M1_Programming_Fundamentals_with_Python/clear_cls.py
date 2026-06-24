import os

'''Function to clear the screen. It uses the os module to execute the clear command for Linux/Mac and cls command for Windows.'''
def clearScreen():
    os.system("clear")
    #os.system("cls")