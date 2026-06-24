from add_products import inventory


def calculateStatitics():
    Inventory=inventory()
    totalSales=0
    Quantity=0

    #Print the products added to the sale and calculate the total sale
    print("Statistics")
    print("--------------------------------")
    if Inventory:
        for products in Inventory:
            subTotalSale = products["price"] * products["quantity"]
            totalSales += subTotalSale
            Quantity += 1

        print(f"Number of registered products: {Quantity}")
        print(f"Total inventory value: $ {totalSales}")
        
    else: print("There are no products yet")
