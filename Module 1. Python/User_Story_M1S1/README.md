# Inventory Management System
## Description
This application is a Python-based tool designed to manage a basic sales record. It is a lightweight solution for users who need to calculate total sales and manage itemized lists within a terminal environment.

## How it works
1. The program initializes an empty list to store multiple product entries.
2. It requests the user to input the product name, unit price, and quantity.
3. The system executes a validation loop to ensure that numeric inputs are handled without crashing the script.
4. Each entry is appended to a global sales list as a nested data structure.
5. Once the input phase is complete, the script iterates through the records to calculate subtotals and the total.

### Key Technical Features
- Input Validation: Uses try-except blocks to catch ValueError during data entry.
- Data Structures: Employs list nesting to organize product attributes (Name, Price, Quantity).
- Logic Flow:
  - The script collects user data through a series of interactive prompts.
  - The algorithm calculates the subtotal for each item by multiplying price and quantity.
  - The final output displays a summary of all processed transactions.

> <div align="center"> <img src="https://github.com/JayzirTech/User_Story_M1S1/blob/0c0be49f93abcdc2126fb3a87f2bb5fa30ac3bd4/flow_chart.drawio.png" width="15%" alt="flow_chart"> </div>
