import os

os.system("clear")
os.system("cls")

#
from add_products import addProduct
from show_inventory import showInventory
from calculate_statitics import calculateStatitics

# Variables
menu = """Options:  
1. Add product
2. Show inventory
3. Calculate statistics
4. Exit
"""

program = True  #Start the program

print("Welcome to the inventory management system") #Wellcome massage

# Program
while program :
    print("-----------------------------------------")

    try:    #Catch the error if there is one and repeat the request
        option = int(input(menu + "Please, choose an option: "))    #Request an option and this must be an integer value
        if option == 1 :    #It allows the user to enter a product
            print()
            addProduct ()
            print()            

        elif option == 2 :  #Show inventory
            print()
            showInventory ()
            print()

        elif option == 3 :  #It displays the statistics
            print()
            calculateStatitics ()
            print()

        elif option == 4 :  #Program ends
            program = False
            print()

        else :  #If the user enters an invalid option, it displays a message and repeats the request.
            print("Invalid option. Try again")  
            print()
            
    except ValueError:  #Catch the error if there is one and repeat the request
        print("Error! Type a number")
        print()
            
print("--------------------------------")
print("Thank you for using our service!")