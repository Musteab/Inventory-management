import os
from datetime import datetime

#File paths

PRODUCTS_FILE = "product.txt"
SUPPLIERS_FILE = "suppliers.txt"
ORDERS_FILE = "orders.txt"

"""Function to handle file utilities"""
def read_file(file_path):
    if not os.path.exists(file_path):
        with open(file_path, "w"): pass  # Create file if it doesn't exist
    with open(file_path, "r") as file:
        return [line.strip() for line in file.readlines()]

def write_file(file_path, lines):
    with open(file_path, "w") as file:
        file.writelines("\n".join(lines) + "\n")

def append_to_file(file_path, line):
    with open(file_path, "a") as file:
        file.write(line + "\n")


"""Function for adding products"""
def add_products():

    #This loop only reaches a break statement if correct format is inputed
    while True:
        product_id = input("Please enter the 7 character product ID which starts with 'PID': ")

        if len(product_id) != 7 or not product_id.upper().startswith('PID') or not product_id[3:7].isdigit():
            print("Wrong ID format, correct format: \n 'PID & PRODUCT NUMBER' \n 'Example: PID0001'")
        else:
            break
    #This loop will be broken once the product name is inputed
    while True:
        product_name = input("Enter the product name: ")
        
        if product_name.strip() is False or product_name.strip() == "":
            print("Please enter a product name!")
        else:
            break
    #This loop will be broken once the product description has been added
    while True:
        product_description = input("Enter the product description: ")
        
        if product_description.strip() is False or product_description.strip() == "":
            print("Please enter a product description!")
        else:
            break
    #This loop will be broken once the product price has been added
    while True:
        product_price = int(input("Enter the product price: "))
        
        if product_price is False:
            print("Please enter a product price!")
        else:
            break

    new_product = f"{product_id}, {product_name}, {product_description}, {product_price}"

    append_to_file(PRODUCTS_FILE, new_product)
    print("Product added successfully!")


    """Main function to run the program"""
def main():

    continue_program = ''

    #loop program until exited
    while continue_program != 'n':

        print('\nInventory Management System')
        print('[1] Add a new product')
        print('[2] Exit')
        #More functionalities to be added

    #Handling the wrong input
        try:
            selection = int(input("Enter your choice: "))

            match selection:
                case 1:
                    add_products()
                case 2:
                    #breaks loop if exited
                    break
                case _:
                    print("Invalid choice")
        except ValueError as e:
            print(e)
            print("ERROR: Choice must be an Integer.")

        #ask the user if they want to continue using the program
        continue_program = input('Do you want to continue the program [y/n]: ').lower()

        #loop it when users input is invalid, not 'y'/'n'
        while continue_program != 'y' and continue_program != 'n':

            print('Invalid Input')
            continue_program = input('\nDo you want to continue the program [y/n]:').lower()
    print('Thank you for using the our Inventory management system.')

#call the main function to run the program
main()