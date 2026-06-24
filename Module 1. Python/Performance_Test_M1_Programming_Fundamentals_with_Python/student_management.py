'''Importing the necessary modules and functions for the program.'''
from services import *
from files import *
from clear_cls import *

'''Declaration of the menu of the program.'''
menu = """Options:  
1. Register new students
2. Show the student list
3. Search a student
4. Update a student's information
5. Delete students
0. Exit
"""

notOption="Opción sin operación"

'''Function to clear the screen.'''
clearScreen()

#'''Function to save the inventory current from the CSV file'''
sstudents.extend(loadCSV())

program = True  #Start the program

print("Welcome to the student management system") #Wellcome massage
print()

'''Start of the program, it will continue until the user chooses to exit.'''
while program :
    print("          Student management             ")
    print("-----------------------------------------")

    try:    #Catch the error if there is one and repeat the request
        Option = int(input(menu + "Please, choose an option: "))    #Request an option and this must be an integer value
        if Option == 1 :    #Add product
            clearScreen()
            addStudent ()
            print()            

        elif Option == 2 :  #Show inventory
            clearScreen()
            showTheStudentsList()

        elif Option == 3 :  #Search product
            clearScreen()
            searchStudent()
            print()

        elif Option == 4 :  #Update product
            clearScreen()
            updateStudent()
            print()

        elif Option == 5 :  #Delete product
            clearScreen()
            deleteStudent()

        elif Option == 0 :  #Exit
            program = False
            clearScreen()

        else :  #If the user enters an invalid option, it displays a message and repeats the request.
            clearScreen()
            print("Invalid option. Try again")  
            print()
            
    except ValueError:  #Catch the error if there is one and repeat the request
        clearScreen()
        print("Error! Type a number")
        print()
            
'''End of the program, it will display a thank you message.'''
print("--------------------------------")
print("Thank you for using our service!")
print("--------------------------------")
print("")