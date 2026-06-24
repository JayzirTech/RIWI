# Variables
sales=[]
saleStatus=True
addProducts=True
totalSales=0
validation=True
input_validation=True

# Program
print()
print("Welcome to the inventory management system")  #Welcome message
print("--------------------------------")
while saleStatus:   #Loop to add products to the sale
    while input_validation:
        name=input("Please, Enter the product name: ").lower().strip()  #Enter the product name and converts everything to lowercase
        if name:    #Verify that the user has entered something
            break
        else: print("Error! You must enter a product.") 

    while validation:   #Loop to validate the price and quantity inputs
        try:
            price=float(input("Please, Enter the product value: ")) #Enter the product price and converts in float
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
            quantity=float(input("Please, Enter the quantity of the product: "))    #Enter the product quantity and converts in float
            break 
        except ValueError:  #Verifies that the user has entered a numeric value
            print()
            print("Error: Please enter a valid numeric value")
            print()

    sale=[name, price, quantity]    #Create a list with the product name, price and quantity

    #Check if the user is entering a product that is already registered
    foundProduct=False
    for i in range(len(sales)): #Go through the shopping list
        if sales[i][0] == name: #If the product already exists, add the new quantity
            sales[i][2] += quantity
            foundProduct=True
            print(f"Updated quantity")
            print()
            break

    if not foundProduct:    #If the product does not exist, it is added to the list
        sales.append(sale)  #Add the product to the sales list 
        print("product added successfully!")
        print()    

    print("Partial summary")
    for sale in sales:  #Submit a partial list of what you have purchased
        number = sales.index(sale) + 1
        subTotalSale=sale[1] * sale[2]
        print(f"Product {number}: {sale[0].capitalize()} | Value: ${sale[1]} | Quantity: {sale[2]} | Total: ${subTotalSale}")   #
        totalSales += subTotalSale
    print(f"Subtotal: $ {totalSales}")

    totalSales=0
    print()

    while addProducts:  
        addProduct=input("Want add more product? (Yes) or (No): ").lower()  #Ask the user if they want to add more products to the sale
        print()
        if addProduct == "yes":
            addProducts=False
        elif addProduct == "no":
            saleStatus=False
            addProducts=False
        else:
            print("--------------------------------")
            print("Invalid option, try again, type (yes) or (no)")  #If the user enters an invalid option, it will ask again
    addProducts=True

print("Total Sale")
print("--------------------------------")

#Print the products added to the sale and calculate the total sale
for sale in sales:  
    number = sales.index(sale) + 1
    subTotalSale=sale[1] * sale[2]
    print(f"Product {number}: {sale[0].capitalize()} | Value: ${sale[1]} | Quantity: {sale[2]} | Total: ${subTotalSale}")   #
    totalSales += subTotalSale
    
#Print the total sale    
print(f"Total sale is: ${totalSales}")
print("--------------------------------")
print("Thank you for your purchase!")
