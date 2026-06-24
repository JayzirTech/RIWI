from add_products import inventory

#Function to display the updated inventory
def showInventory():
    number=0
    products=inventory()

    
    print("Inventory")
    print("--------------------------------")
    if products: 
        for product in products:    #Scroll through the product list and display each product with its price and quantity.
            number += 1
            if product["quantity"] == 0:
                print(f"Product {number}: {product["name"].capitalize()} | No stock")   #If the product is out of stock, display a message indicating it.
            else:
                print(f"Product {number}: {product["name"].capitalize()} | Value: ${product["price"]} | Quantity: {product["quantity"]}")

    else: print("There are no products yet")
