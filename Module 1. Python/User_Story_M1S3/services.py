'''This module contains the functions that perform the operations of the inventory management system,
such as adding a product, showing the inventory, searching for a product, updating a product,
deleting a product and calculating statistics about the inventory.'''

import csv

validation = True
Inventory = []

'''Function to add a product to the inventory. Asks the user for the product name, price and quantity.
It validates the inputs and checks if the product already exists.'''
def addProduct ():

    validation=True

    print("Add Product")
    print("--------------------------------")
    
    while validation:
        name=input("Please, Enter the product name: ").lower().strip()  #Enter the product name and converts everything to lowercase
        if name:    #Verify that the user has entered something
            for product in Inventory:    #Scroll through the product list and display each product with its price and quantity.
                if product["name"] == name :
                    print()
                    print(f"The product {name.upper()} already exists.")
                    print(f"Product: {product["name"].capitalize()} | Value: ${product["price"]} | Quantity: {product["quantity"]}")
                    validation=False
            break
        else: print("Error! You must enter a product.") 

    while validation:   #Loop to validate the price and quantity inputs
        try:
            price=float(input(f"Please, Enter the product value ({name.capitalize()}): ")) #Enter the product price and converts in float
            if price<=0: #Verify that the value is greater than 0
                print()
                print("The price must be greater then zero")
                print()
                continue
            break 
        except ValueError:  #Verifies that the user has entered a numeric value
            print()
            print("Error: Please enter a valid numeric value")
            print()

    while validation:   #Loop to validate the price and quantity inputs
        try:
            quantity=int(input(f"Please, Enter the quantity of the product ({name.capitalize()}): "))    #Enter the product quantity and converts in float
            if quantity<0: #Verify that the value is greater or equal to 0
                print()
                print("The quantity must be greater or equal to zero")
                print()
                continue
            break 
        except ValueError:  #Verifies that the user has entered a numeric value
            print()
            print("Error: Please enter a valid numeric value")
            print()

    if validation:    #If the product is not already in the inventory, it creates a new product with the entered name, price and quantity and adds it to the inventory list.
        product={
        "name" : name,
        "price" : price,
        "quantity" : quantity
        }

        Inventory.append(product)   #Add the new product to the list

        print()
        print("Product added successfully!")

'''Function to return the inventory list.'''
def inventory():
    return Inventory

'''Function to display the updated inventory'''
def showInventory():
    number=0
    
    print("Inventory")
    print("--------------------------------")
    if Inventory: 
        for product in Inventory:    #Scroll through the product list and display each product with its price and quantity.
            number += 1
            if product["quantity"] == 0:
                print(f"Product {number}: {product["name"].capitalize()} | No stock")   #If the product is out of stock, display a message indicating it.
            else:
                print(f"Product {number}: {product["name"].capitalize()} | Value: ${product["price"]} | Quantity: {product["quantity"]}")

    else: print("There are no products yet")

'''Function to search for a product by name and display its price and quantity.'''
def searchProduct ():

    print("Search Product")
    print("--------------------------------")
        
    if Inventory: 
        search=input("Please, Enter the product name: ").lower().strip()

        for product in Inventory:    #Scroll through the product list and display each product with its price and quantity.
            if product["name"] == search:
                print()
                print(f"The product {search.upper()} has been found")   #If the product is found, it displays a message indicating that the product was found and shows its price and quantity.
                print("--------------------------------")
                print(f"Product: {product["name"].capitalize()} | Value: ${product["price"]} | Quantity: {product["quantity"]}")
                break

            elif product == Inventory[-1]: #If the product is not found after scrolling through the entire list, it displays a message indicating that the product was not found.
                print()
                print(f"The product {search.upper()} has not been found")
    
    else: print("There are no products yet")

'''Function to update the name, price or quantity of a product.'''
def updateProduct ():
    validation=True
    menu='''What do you want to update?
1. Name
2. Price
3. Quantity
0. Cancel
Please, choose an option: '''

    products=inventory()

    print("Update Product")
    print("--------------------------------")
        
    if products: 
        while validation: 
            search=input("Please, enter the name of the product you want to update: ").lower().strip()
            if search:    #Verify that the user has entered something
                break
            else: print("Error! You must enter a product.") 

        for product in products:    #Scroll through the product list and display each product with its price and quantity.
            if product["name"] == search:
                print()
                print(f"Product: {product["name"].capitalize()} | Value: ${product["price"]} | Quantity: {product["quantity"]}")
                print()

                while validation: 
                    try:    #Catch the error if there is one and repeat the request
                        option = int(input(menu))    #Request an option and this must be an integer value
                        if option == 1 :    #It allows the user to update the name of the product
                            while validation:
                                print()
                                print("---------------------------------")
                                print(f"The actual name is: {product['name'].capitalize()}")
                                newFeature=input(f"Please, enter the new name of the product ({product["name"].capitalize()}): ").lower().strip()
                                if newFeature:
                                    print("--------------------------------")
                                    product["name"] = newFeature
                                    print(f"The new name is: {product["name"].capitalize()}")
                                    print("--------------------------------")
                                    print(f"Product: {product["name"].capitalize()} | Value: ${product["price"]} | Quantity: {product["quantity"]}")
                                    print("¡Updated Name!")
                                    validation=False
                                else: 
                                    print()
                                    print(f"Error! You must enter the new name of the product ({product["name"].capitalize()})") 
                        
                        elif option == 2:
                            print()
                            while validation:
                                try:
                                    print("---------------------------------")
                                    print(f"The actual value is ${product["price"]} of the product {product["name"].capitalize()}")
                                    newFeature=float(input(f"Please, enter the new value of the product ({product["name"].capitalize()}): "))
                                    if newFeature<=0: #Verify that the value is greater than 0
                                        print()
                                        print("The price must be greater then zero")
                                        print()
                                        continue
                                    print()
                                    product["price"] = newFeature
                                    print(f"The new value is: ${product["price"]} of the product {product["name"].capitalize()}")
                                    print()
                                    print("--------------------------------")
                                    print(f"Product: {product["name"].capitalize()} | Value: ${product["price"]} | Quantity: {product["quantity"]}")
                                    print(f"¡Updated Value!")
                                    validation=False

                                except ValueError:
                                    print()
                                    print("Error! Type a number")
                                    print()

                        elif option == 3:
                            print()
                            while validation:
                                try:
                                    print("---------------------------------")
                                    print("Note: You cannot decrease the quantity more than the current stock.")
                                    print()
                                    print(f"The actual quantity is: {product["quantity"]} of the product {product["name"].capitalize()}")
                                    newFeature=int(input(f"Please, enter the new quantity of the product ({product["name"].capitalize()}): "))
                                    newQuantity=newFeature + product["quantity"]
                                    if newQuantity<0: #Verify that the value is greater or equal to 0
                                        print()
                                        print(f"The quantity must be greater -{product["quantity"]}")
                                        print()
                                        continue
                                    product["quantity"] = newQuantity
                                    print()
                                    print(f"The new quantity is {product["quantity"]} of the product {product["name"].capitalize()}")
                                    print()
                                    print(f"Product: {product["name"].capitalize()} | Value: ${product["price"]} | Quantity: {product["quantity"]}")
                                    print(f"¡Updated Quantity!")
                                    validation=False

                                except ValueError:
                                    print()
                                    print("Error! Type a valid number")
                                    print()

                        elif option == 0:
                            validation=False

                        else:
                            print("Invalid option. Try again")  
                            print()

                    except ValueError:  #Catch the error if there is one and repeat the request
                        print("Error! Type a number")
                        print()
                
            elif product == products[-1] and validation: #If the product is not found after scrolling through the entire list, it displays a message indicating that the product was not found.
                print()
                print(f"The product {search.upper()} has not been found")

    else: print("There are no products yet")

'''Function to delete a product from the inventory.'''
def deleteProduct ():
    validation=True

    products=inventory()

    print("Delete Product")
    print("--------------------------------")
        
    if products: 
        while validation: 
            search=input("Please, enter the name of the product you want to delete: ").lower().strip()
            if search:    #Verify that the user has entered something
                break
            else: 
                print("Error! You must enter a product.") 
                print()

        for product in products:    #Scroll through the product list and display each product with its price and quantity.
            if product["name"] == search:
                print()
                print(f"Product: {product["name"].capitalize()} | Value: ${product["price"]} | Quantity: {product["quantity"]}")
                print()

                while validation:
                    confirmation=input(f"Are you sure you want to delete the product {product["name"].capitalize()}? (Yes or No): ").lower().strip()
                    if confirmation == "yes":
                        products.remove(product)
                        print()
                        print(f"The product {product["name"].upper()} has been deleted")
                        validation=False
                    elif confirmation == "no":
                        print()
                        print(f"The product {product["name"].upper()} has not been deleted")
                        validation=False
                    else:
                        print("Invalid option. Try again")  
                        print()
                
            elif product == products[-1]: #If the product is not found after scrolling through the entire list, it displays a message indicating that the product was not found.
                print()
                print(f"The product {search.upper()} has not been found")

    else: 
        if validation:
            print("There are no products yet")

'''Function to calculate and display statistics about the inventory: total units, total value, most expensive product and highest stock product.'''
def calculateStatistics ():

    if Inventory:
        totalUnits = sum(product["quantity"] for product in Inventory)
        totalValue = sum(product["price"] * product["quantity"] for product in Inventory)
        mostExpensiveProduct = max(Inventory, key=lambda p: p["price"])
        highestStockProduct = max(Inventory, key=lambda p: p["quantity"])

        print("Inventory Statistics")
        print("--------------------------------")
        print(f"Total Units: {totalUnits}")
        print(f"Total Value: ${totalValue}")
        print(f"Most Expensive Product: {mostExpensiveProduct['name'].capitalize()} | Price: ${mostExpensiveProduct['price']}")
        print(f"Highest Stock Product: {highestStockProduct['name'].capitalize()} | Quantity: {highestStockProduct['quantity']}")

    else: print("There are no products yet")