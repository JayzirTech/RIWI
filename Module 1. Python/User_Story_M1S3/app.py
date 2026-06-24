'''This a program where you can manage an inventory of products. 
You can add, show, search, update and delete products, calculate statistics.
Save the inventory to a CSV file and load the inventory from a CSV file.'''

'''Importing the necessary modules and functions for the program.'''
from services import *
from files import *
from clear_cls import *

'''Declaration of the menu of the program.'''
menu = """Options:  
1. Add product
2. Show inventory
3. Search product
4. Update Product
5. Delete product
6. Calculate statistics
7. Save CSV
8. Load CSV
9. Delete error log
0. Exit
"""

'''Function to clear the screen.'''
clearScreen()

'''Function to save the inventory current from the CSV file'''
Inventory.extend(readCSV()) 

program = True  #Start the program

print("Welcome to the inventory management system") #Wellcome massage

'''Start of the program, it will continue until the user chooses to exit.'''
while program :
    print("-----------------------------------------")

    try:    #Catch the error if there is one and repeat the request
        option = int(input(menu + "Please, choose an option: "))    #Request an option and this must be an integer value
        if option == 1 :    #Add product
            clearScreen()
            addProduct ()
            print()            

        elif option == 2 :  #Show inventory
            clearScreen()
            showInventory ()
            print()

        elif option == 3 :  #Search product
            clearScreen()
            searchProduct ()
            print()

        elif option == 4 :  #Update product
            clearScreen()
            updateProduct ()
            print()

        elif option == 5 :  #Delete product
            clearScreen()
            deleteProduct ()
            print()

        elif option == 6 :  #Calculate statistics
            clearScreen()
            calculateStatistics ()
            print()

        elif option == 7 :  #Save CSV
            clearScreen()
            saveCSV ()
            print()

        elif option == 8 :  #Load CSV
            clearScreen()
            loadCSV ()
            print()

        elif option == 9 :  #Delete error log
            clearScreen()
            deleteErrorLines ()
            print()

        elif option == 0 :  #Exit
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
print("")