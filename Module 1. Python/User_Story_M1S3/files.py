'''This module contains functions to save and load the inventory to and from a CSV file,
as well as to compare the current inventory with the inventory from the CSV file.
It also includes functions to delete invalid lines from the CSV file and to fuse the CSV file with
the current inventory.'''

from services import Inventory
import csv

'''Functions to save the current inventory to a CSV file without comparing it with the inventory from the CSV file'''
def saveCSVWithoutCompare ():
    try:
        with open('inventory.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Price', 'Quantity'])
            for product in Inventory:
                writer.writerow([product['name'], product['price'], product['quantity']])
        
        print("")
        print("Inventory saved to inventory.csv")

    except FileNotFoundError:
        print("Error: Could not find the file to save the inventory.")

'''Function to load the inventory from a CSV file without comparing it with the current inventory'''
def loadCSVWithoutCompare ():
    try:
        with open('inventory.csv', mode='r', newline='') as file:
            reader = csv.DictReader(file)
            Inventory.clear()
            for row in reader:
                Inventory.append({'name': row['Name'], 'price': float(row['Price']), 'quantity': int(row['Quantity'])})
        
        print("")
        print("Inventory loaded from inventory.csv")

    except FileNotFoundError:
        print("Error: Could not find the file to load the inventory.")

'''Function to save the inventory to a CSV file. It compares the current inventory with the inventory from the CSV file
and if they are different, it asks the user if they want to overwrite the CSV file with the current inventory or
fuse the CSV file with the current inventory.'''
def saveCSV ():
    process=True

    compare=compareInventories (Inventory, readCSV())

    if not compare:
        print("-----------------------------")
        print("Warning: Saving the inventory to a CSV file will overwrite the current data in the file.")
        print()

        while process:
            
            try:
                option = int (input ("What do you want to do? \n " \
                "1. Overwrite the CSV file with the current inventory \n " \
                "2. Fuse the CSV file with the current inventory \n " \
                "0. Cancel the saving process \n " \
                "Please, choose an option: "))

                if option == 1:     #The program will overwrite the current inventory
                    saveCSVWithoutCompare ()  #Save the current inventory to the CSV file

                    print()
                    print("Inventory overwritten with data from inventory.csv")
                    print()

                    process=False

                elif option == 2:   #The program will fuse the CSV file with the current inventory

                    fusionInventories()  #Fuse the CSV file with the current inventory

                    process=False

                elif option == 0:
                    print("Saving process cancelled.")
                    print()
                    return
                
                else:
                    print()
                    print("Invalid option. Please, choose a valid option.")

            except ValueError:
                print()
                print("Error! Type a number")

    else:
        print("The inventory is up to date with the CSV file. No saving needed.")

'''Function to load the inventory from a CSV file. It compares the current inventory with the inventory from the CSV file
and if they are different, it asks the user if they want to overwrite the current inventory with the inventory
from the CSV file or fuse the CSV file with the current inventory.'''
def loadCSV ():
    procces=True
    compare=compareInventories (Inventory, readCSV())

    if not compare:
        print("-----------------------------")
        print("Warning: Loading a CSV file will overwrite the current inventory.")
        print()

        while procces:
                                    
            try:
                option = int (input ("What do you want to do? \n " \
                "1. Overwrite the current inventory \n " \
                "2. Fuse the CSV file with the current inventory \n " \
                "0. Cancel the loading process \n " \
                "Please, choose an option: "))

                if option == 1:     #The program will overwrite the current inventory
                    Inventory.clear()  # Clear current inventory before loading new data
                    Inventory.extend(readCSV())  # Load new data from CSV file

                    print()
                    print("Inventory overwritten with data from inventory.csv")
                    print()

                    procces=False

                elif option == 2:   #The program will fuse the CSV file with the current inventory

                    fusionInventories()  #Fuse the CSV file with the current inventory

                    print()
                    print("Inventory fused with data from inventory.csv")
                    print()

                    procces=False

                elif option == 0:
                    print("Loading process cancelled.")
                    print()
                    return
                
                else:
                    print()
                    print("Invalid option. Please, choose a valid option.")

            except ValueError:
                print()
                print("Error! Type a number")

    else:
        print("The inventory is up to date with the CSV file. No loading needed.")

'''Function to read the inventory from a CSV file and return it as a list of dictionaries.'''
def readCSV ():
    try:
        with open('inventory.csv', mode='r') as file:
            reader = csv.DictReader(file)
            inventory = []

            for row in reader:
                try:
                    price = float(row['Price'])
                    quantity = int(row['Quantity'])
                    product = {
                        'name': row['Name'],
                        'price': price,
                        'quantity': quantity
                    }
                    inventory.append(product)

                except ValueError:
                    print(f"Error: Invalid data format in CSV file for product '{row['Name']}'. Skipping the invalid line.")
                except TypeError:
                    print(f"Error: Invalid data type in CSV file for product '{row['Name']}'. Skipping the invalid line.")
            print("")
            return inventory
        
    except FileNotFoundError:
        print("Error: Could not find the file to save the inventory.")
        return []           

'''Function to compare the current inventory with the inventory from the CSV file.
It returns True if they are the same and False if they are different.'''
def compareInventories (inventory1, inventory2): #Compare the inventory actual with the inventory from CSV file.

    if len(inventory1) != len(inventory2):
        return False
    
    for product1 in inventory1: 
        for product2 in inventory2:
            if product1['name'] == product2['name']:
                if product1['price'] != product2['price'] or product1['quantity'] != product2['quantity']:
                    return False    
            
    return True

'''Function to delete invalid lines from the CSV file. It reads the CSV file,
validates the data and if there are invalid lines, it deletes them from the CSV file
and displays a message with the name of the product that had an invalid line.'''
def deleteErrorLines ():
    nameError=[]
    validationError=False

    try:
        with open(r'C:\Users\jayzi\OneDrive\Desktop\JayzirTech\Riwi\User_Story_M1S3\inventory.csv', mode='r') as file:
            reader = csv.DictReader(file)
            inventory = []

            for row in reader:
                try:
                    price = float(row['Price'])
                    quantity = int(row['Quantity'])
                    product = {
                        'name': row['Name'],
                        'price': price,
                        'quantity': quantity
                    }
                    inventory.append(product)

                except ValueError:
                    validationError=True
                    nameError.append(row['Name'])
        
        with open(r'C:\Users\jayzi\OneDrive\Desktop\JayzirTech\Riwi\User_Story_M1S3\inventory.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Price', 'Quantity'])
            for product in inventory:
                writer.writerow([product['name'], product['price'], product['quantity']])
        
        for name in nameError:
            print(f"Invalid line for product '{name}' deleted from inventory.csv")

        if validationError:

            print("")
            print("Invalid lines deleted from inventory.csv")

        else:
            print("")
            print("No invalid lines found in inventory.csv")

    except FileNotFoundError:
        print("Error: Could not find the file to save the inventory.")

'''Function to fuse the CSV file with the current inventory.'''
def fusionInventories():
    actualInventory=Inventory.copy()  #Copy the current inventory to a new variable

    Inventory.clear()  # Clear current inventory before loading new data
    Inventory.extend(readCSV())  # Load new data from CSV file

    #compare the actual inventory with the inventory from CSV file and add the products that are not in the actual inventory to the current inventory
    for product1 in actualInventory:
        if product1 not in Inventory:
            Inventory.append(product1)

    saveCSVWithoutCompare ()  #Save the current inventory to the CSV file