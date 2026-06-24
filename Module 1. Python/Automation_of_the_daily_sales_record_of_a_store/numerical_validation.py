validation=True

# Functions to validate the price and quantity inputs
def numericalValidationFloat():
    while validation:   #Loop to validate the price and quantity inputs
        try:
            price=float(input("Please, Enter the product value: ")) #Enter the product price
            return price
            break 
        except ValueError:
            print()
            print("Error: Please enter a valid numeric value")
            print()


def numericalValidationInt():
    while validation:   #Loop to validate the price and quantity inputs
        try:
            quantity=int(input("Please, Enter the quantity of the product: "))    #Enter the product quantity
            return quantity
            break 
        except ValueError:
            print()
            print("Error: Please enter a valid numeric value")
            print()