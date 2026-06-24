# User_Story_M1S3
# Register products in an inventory system. 

The user should be able to add products with their name, price and quantity, display the inventory, search for a product by name, update the product information and delete a product from the inventory. The inventory should be stored in a CSV file and the user should be able to load the inventory from the CSV file when starting the program. The user should also be able to save the inventory to the CSV file when exiting the program. Additionally, the user should be able to calculate and display statistics about the inventory: total units, total value, most expensive product and highest stock product.

## How it works:
1. The user is presented with a menu of options to choose from: add product, display inventory, search product, update product, delete product, calculate statistics, save inventory, load inventory, delete invalid lines and exit.

2. The user selects an option and the corresponding function is executed.
    - (Add Product) The user can add products by entering the name, price and quantity. The product is added to the inventory currently stored in memory and the user is informed that the product has been added successfully.
    - (Display Inventory) The user can display the inventory, which shows the name, price and quantity of each product currently stored in memory. If there are no products, a message is displayed indicating that there are no products yet.
    - (Search Product) The user can search for a product by name. If the product is found, its price and quantity are displayed. If the product is not found, a message is displayed indicating that the product was not found.
    - (Update Product) The user can update the name, price or quantity of a product. The user is prompted to enter the name of the product they want to update, and if the product is found, they can choose which attribute they want to update (name, price or quantity) and enter the new value. The product information is updated in memory and the user is informed that the product has been updated successfully. If the product is not found, a message is displayed indicating that the product was not found.
    - (Delete Product) The user can delete a product from the inventory. The user is prompted to enter the name of the product they want to delete, and if the product is found, it is removed from the inventory in memory and the user is informed that the product has been deleted successfully. If the product is not found, a message is displayed indicating that the product was not found.
    - (Calculate Statistics) The user can calculate and display statistics about the inventory. The total units is calculated by summing the quantity of all products, the total value is calculated by summing the product of price and quantity for all products, the most expensive product is determined by finding the product with the highest price, and the highest stock product is determined by finding the product with the highest quantity. The statistics are displayed to the user.
    - (Save Inventory) The user can save the inventory to a CSV file. The inventory currently stored in memory is written to the CSV file, and the user is informed that the inventory has been saved successfully. If there is an error while saving the inventory, a message is displayed indicating that there was an error.
    - (Load Inventory) The user can load the inventory from a CSV file. The inventory is read from the CSV file and stored in memory, and the user is informed that the inventory has been loaded successfully. If there is an error while loading the inventory, a message is displayed indicating that there was an error.
    - (Delete Invalid Lines) The user can delete invalid lines from the CSV file. The CSV file is read and the data is validated. If there are invalid lines, they are deleted from the CSV file and a message is displayed with the name of the product that had an invalid line. If there are no invalid lines, a message is displayed indicating that there are no invalid lines.
    - (Exit) The user can exit the program. 

## Code structure:
- app.py: Contains the main function that runs the program and displays the menu to the user.
- clear_cls.py: Contains the function to clear the screen.
- files.py: Contains the functions to save and load the inventory from a CSV file, delete invalid lines from the CSV file and fuse the CSV file with the current inventory.
- services.py: Contains the functions to add a product, display the inventory, search for a product, update a product, delete a product and calculate statistics about the inventory.

# Tecnologies used:
- Python: The programming language used to implement the inventory system.

# Contributors:
- JayzirTech: The developer who implemented the inventory system.

### This project is open source and contributions are welcome. If you want to contribute, please fork the repository and create a pull request with your changes.