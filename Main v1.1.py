import os

# File paths
PRODUCTS_FILE = "product.txt"
SUPPLIERS_FILE = "suppliers.txt"
ORDERS_FILE = "orders.txt"
# File utility functions
def read_file(file_path):
    """Read the contents of a file, creating it if it doesn't exist."""
    if not os.path.exists(file_path):
        with open(file_path, "w"): pass  # Create file if it doesn't exist
    with open(file_path, "r") as file:
        return [line.strip() for line in file.readlines()]

def write_file(file_path, lines):
    """Write lines to a file, replacing its contents."""
    with open(file_path, "w") as file:
        file.writelines(lines)

def append_to_file(file_path, line):
    """Append a line to a file."""
    with open(file_path, "a") as file:
        file.write(line + "\n")

def read_products(file_path):
    """Read all products from the file and return a dictionary with product IDs as keys."""
    products = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                product_data = line.strip().split(", ")
                if len(product_data) > 0:
                    product_id = product_data[0]
                    products[product_id] = product_data
    except FileNotFoundError:
        # If the file doesn't exist, return an empty dictionary.
        pass
    return products


def add_products():
    """Function for adding products"""
    existing_products = read_products(PRODUCTS_FILE)

    while True:
        product_id = "PID" + input("Please enter the 4-digit product ID (e.g. 0001):")
        if len(product_id) != 7 or not product_id[3:].isdigit():
            print("Invalid format. Correct format: 4 digit ID (e.g. 0001).")
        elif product_id in existing_products:
            print("Product ID already exists. Please enter a unique Product ID.")
        else:
            break

    while True:
        product_name = input("Enter the product name: ").strip()
        if not product_name:
            print("Product name cannot be empty.")
        else:
            break

    while True:
        product_description = input("Enter the product description: ").strip()
        if not product_description:
            print("Product description cannot be empty.")
        else:
            break

    while True:
            try:
                product_price = float(input("Enter the product price: "))
                if product_price < 0:
                    print("Price cannot be negative.")
                else:
                    break
            except ValueError:
                print("Invalid input. Price must be a number.")

    while True:
        try:
            product_quantity = int(input("Enter the product quantity: "))
            if product_quantity < 0:
                print("Quantity cannot be negative.")
            else:
                break
        except ValueError:
            print("Invalid input. Quantity must be an integer.")

    new_product = f"{product_id}, Name: {product_name}, Description: {product_description}, Price: {product_price:.2f}, Quantity: {product_quantity}"
    append_to_file(PRODUCTS_FILE, new_product)
    print("Product added successfully!")

# Function for updating products
def up_products():
    while True:
        print("1. Update whole product")
        print("2. Update specific product details")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':  # Update whole product
            pid = "PID" + input("Enter the PID of the product you wish to update: ")
            data = read_file(PRODUCTS_FILE)
            updated = False

            for i, line in enumerate(data):
                product_details = line.split(", ")
                if product_details[0] == pid:
                    product_name = input("Enter the updated product name: ").strip()
                    product_description = input("Enter the updated product description: ").strip()
                    while True:
                        try:
                            product_price = float(input("Enter the updated product price: "))
                            if product_price < 0:
                                print("Price cannot be negative.")
                            else:
                                break
                        except ValueError:
                            print("Invalid input. Price must be a number.")
                    while True:
                        try:
                            product_quantity = int(input("Enter the updated product quantity: "))
                            if product_quantity < 0:
                                print("Quantity cannot be negative.")
                            else:
                                break
                        except ValueError:
                            print("Invalid input. Quantity must be a number.")
                    data[i] = f"{pid}, Name: {product_name}, Description: {product_description}, Price: {product_price:.2f}, Quantity: {product_quantity}"
                    updated = True
                    break

            if updated:
                write_file(PRODUCTS_FILE, [line + "\n" for line in data])
                print("Product updated successfully!")
            else:
                print("PID not found.")

        elif choice == '2':  # Update specific detail
            pid = "PID" + input("Enter the PID of the product you wish to update: ")
            data = read_file(PRODUCTS_FILE)
            updated = False

            for i, line in enumerate(data):
                product_details = line.split(", ")
                if product_details[0] == pid:
                    print("1. Update Product Name")
                    print("2. Update Product Description")
                    print("3. Update Product Price")
                    print("4. Update Product Quantity")
                    detail_choice = input("Choose the detail to update: ")

                    if detail_choice == '1':
                        product_details[1] ="Name: " + input("Enter the updated product name: ").strip()
                    elif detail_choice == '2':
                        product_details[2] = "Description: " + input("Enter the updated product description: ").strip()
                    elif detail_choice == '3':
                        while True:
                            try:
                                product_price = float(input("Enter the updated product price: "))
                                if product_price < 0:
                                    print("Price cannot be negative.")
                                else:
                                    product_details[3] = f"Price: {product_price:.2f}"
                                    break
                            except ValueError:
                                print("Invalid input. Price must be a number.")
                    elif detail_choice == '4':
                        while True:
                            try:
                                product_quantity = int(input("Enter the updated product quantity: "))
                                if product_quantity < 0:
                                    print("Quantity cannot be negative.")
                                else:
                                    product_details[4] = "Quantity: " + str(product_quantity)
                                    break
                            except ValueError:
                                print("Invalid input. Quantity must be an integer.")
                    else:
                        print("Invalid choice.")
                        break

                    data[i] = ", ".join(product_details)
                    updated = True
                    break

            if updated:
                write_file(PRODUCTS_FILE, [line + "\n" for line in data])
                print("Product detail updated successfully!")
            else:
                print("PID not found.")

        elif choice == '3':  # Exit
            break
        else:
            print("Invalid choice.")

def view(file_path):
    data = read_file(file_path)
    if not data:
        print("File is empty")
    else:
        print(file_path)
        for line in data:
            print(line)
            
def view_inventory():
    while True:
        print("View Inventory")
        print("\nSelect which File you want to view")
        print("[1] Products File")
        print("[2] Suppliers File")
        print("[3] Orders File")
        print("[4] Back to Main Menu")

        choice=input("Enter your choice:")
        if choice== '1':
            view(PRODUCTS_FILE)
        elif choice== '2':
            view(SUPPLIERS_FILE)
        elif choice== '3':
            view(ORDERS_FILE)
        elif choice== '4':
            break
        else:
            print("Invalid. Choose a valid option")

def read_suppliers(file_path):
    """Read all suppliers from the file and return a dictionary with supplier IDs as keys."""

    suppliers = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                supplier_data = line.strip().split(", ")
                if len(supplier_data) > 0:
                    supplier_id = supplier_data[0]
                    suppliers[supplier_id] = supplier_data
    except FileNotFoundError:
        # If the file doesn't exist, return an empty dictionary.
        pass
    return suppliers

def add_supplier():
    """Function to add suppliers"""
    existing_suppliers = read_suppliers(SUPPLIERS_FILE)
    
    while True: #Loop for adding supplier ID
        supplier_id = "SID" + input("Please enter the 4-digit supplier ID (e.g. 0001):")
        if len(supplier_id) != 7 or not supplier_id[3:].isdigit():
            print("Invalid format. Correct format: 4 digit ID (e.g. 0001).")
        elif supplier_id in existing_suppliers:
            print("Suppliers ID already exists. Please enter a unique Suppliers ID.")
        else:
            break
    while True:
        supplier_name = input("Enter the supplier name: ").strip()
        if not supplier_name:
            print("Supplier name cannot be empty.")
        else:
            break
    while True:
            try:
                supplier_contact = "60" + input("Enter the supplier contact number: ")
                if not len(supplier_contact) == 12 or not supplier_contact.isdigit:
                    print("Contact number is invalid")
                else:
                    break
            except ValueError:
                print("Invalid input. Contact number must be a number.")
    new_supplier = f"{supplier_id}, Name: {supplier_name}, Contact: {supplier_contact}"
    append_to_file(SUPPLIERS_FILE, new_supplier)
    print("Supplier added successfully!")
    

# Main function to run the program
def main():
    while True:
        print("\nInventory Management System")
        print("[1] Add a new product")
        print("[2] Update a product")
        print("[3] Add Supplier")
        print("[4] View Inventory")
        print("[5] Exit")

        try:
            selection = int(input("Enter your choice: "))
            if selection == 1:
                add_products()
            elif selection == 2:
                up_products()
            elif selection == 3:
                add_supplier()
               
            elif selection == 4:
                 view_inventory()
            elif selection == 5:
                print("Exiting the program. Thank you!")
                break
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
