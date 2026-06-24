from numerical_validation import numericalValidationFloat
from numerical_validation import numericalValidationInt

# Variables
sales=[]
salesDay=[]
saleStatus=True
addProducts=True
sistemStatus=True
addNewSales=True
programStatus=True
totalSales=0
salesDayTotal=0

# Program
print()
print("Welcome to the inventory management system")  #Welcome message
print("--------------------------------")

while programStatus:   #Loop to ask the user if they want to start the program
    while sistemStatus:   #Loop to ask the user if they want to start the program
        while saleStatus:   #Loop to add products to the sale
            name=input("Please, Enter the product name: ")  #Enter the product name
            price=numericalValidationFloat()  #Call the function to validate the price input
            quantity=numericalValidationInt()  #Call the function to validate the quantity input
            print("product added successfully!")

            sale=[name, price, quantity]    #Create a list with the product name, price and quantity
            sales.append(sale)  #Add the product to the sales list
            salesDay.append(sale)   #Add the product to the salesDay list to keep track of the sales of the day
            print()

            while addProducts:  
                addProduct=input("Want add more product? (Yes) or (No): ").lower()  #Ask the user if they want to add more products to the sale
                if addProduct == "yes":
                    addProducts=False
                elif addProduct == "no":
                    saleStatus=False
                    addProducts=False
                else:
                    print("--------------------------------")
                    print("Invalid option, try again")  #If the user enters an invalid option, it will ask again
            addProducts=True

        print()
        print("--------------------------------")

        #Print the products added to the sale and calculate the total sale
        for sale in sales:  
            number = sales.index(sale) + 1
            subTotalSale=sale[1] * sale[2]
            print(f"Product {number}: {sale[0]} | Value: ${sale[1]} | Quantity: {sale[2]} | Total: ${subTotalSale}")   #
            totalSales= totalSales + subTotalSale
            
        #Print the total sale    
        print(f"Total sale is: ${totalSales}")
        print("Thank for your purchase!")
        print("--------------------------------")
        print()
        sales.clear()  #Clear the sales list for the next sale
        totalSales=0   #Reset the total sales for the next sale

        while addNewSales:   #Loop to ask the user if they want to add a new sale
            addNewSale=input("Want add a new sale? (Yes) or (No): ").lower()  #Ask the user if they want to add a new sale
            if addNewSale == "yes":
                saleStatus=True
                addNewSales=False
            elif addNewSale == "no":
                sistemStatus=False
                addNewSales=False
            else:
                print("--------------------------------")
                print("Invalid option, try again")  #If the user enters an invalid option, it will ask again
        addNewSales=True

    print("Main menu")
    print("1. Add a new sale")
    print("2. View sales of the day")
    print("3. Exit")
    Option=input("Enter the option number: ")   #Ask the user to choose an option

    if Option == "1":
        saleStatus=True
        addProducts=True
        sistemStatus=True
        saleStatus=True
        print()
    elif Option == "2":
        print()
        print("Sales of the day")
        print("--------------------------------")
        for sale in salesDay:  #Print the products added to the salesDay list and calculate the total sales of the day
            number = salesDay.index(sale) + 1
            subTotalSale=sale[1] * sale[2]
            print(f"Product {number}: {sale[0]} | Quantity: {sale[2]}")   #
            salesDayTotal=subTotalSale + salesDayTotal
        print("Total sales of the day: $", salesDayTotal)   #Print the total sales of the day
        print("--------------------------------")
        print()
        salesDayTotal=0   #Reset the total sales of the day for the next time the user wants to view the sales of the day

    elif Option == "3":
        programStatus=False
        print()
        print("Thank you for using the inventory management system, see you next time!")  #Exit message
        print("")
    else:
        print("--------------------------------")
        print("Invalid option, try again")  #If the user enters an invalid option, it will ask again