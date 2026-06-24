validation = True
Inventory = []

#Function to register a new product
def addProduct ():

    print("Add Product")
    print("--------------------------------")
    
    while validation:
        name=input("Please, Enter the product name: ").lower().strip()  #Enter the product name and converts everything to lowercase
        if name:    #Verify that the user has entered something
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
            break 
        except ValueError:  #Verifies that the user has entered a numeric value
            print()
            print("Error: Please enter a valid numeric value")
            print()


    #Check if the user is entering a product that is already registered and update the quantity
    foundProduct=False
    for product in Inventory:
        if product["name"] == name :
            product["quantity"] += quantity
            foundProduct=True
            print(f"Updated quantity")
            print()

    if not foundProduct:    #If the product does not exist, it is added to the list as a dictionary
        product={
        "name" : name,
        "price" : price,
        "quantity" : quantity
        }

        Inventory.append(product)   #Add the new product to the list

        print("Product added successfully!")

#Function to return the product list
def inventory():
    return Inventory
