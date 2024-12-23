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

# Function for adding products
def add_products():
    while True:
        product_id = input("Please enter the 7-character product ID (e.g., PID0001): ")
        if len(product_id) != 7 or not product_id.upper().startswith('PID') or not product_id[3:].isdigit():
            print("Invalid format. Correct format: 'PID' followed by 4 digits (e.g., PID0001).")
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

    new_product = f"{product_id}, {product_name}, {product_description}, {product_price:.2f}"
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
            pid = input("Enter the PID of the product you wish to update: ")
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
                    data[i] = f"{pid}, {product_name}, {product_description}, {product_price:.2f}"
                    updated = True
                    break

            if updated:
                write_file(PRODUCTS_FILE, [line + "\n" for line in data])
                print("Product updated successfully!")
            else:
                print("PID not found.")

        elif choice == '2':  # Update specific detail
            pid = input("Enter the PID of the product you wish to update: ")
            data = read_file(PRODUCTS_FILE)
            updated = False

            for i, line in enumerate(data):
                product_details = line.split(", ")
                if product_details[0] == pid:
                    print("1. Update Product Name")
                    print("2. Update Product Description")
                    print("3. Update Product Price")
                    detail_choice = input("Choose the detail to update: ")

                    if detail_choice == '1':
                        product_details[1] = input("Enter the updated product name: ").strip()
                    elif detail_choice == '2':
                        product_details[2] = input("Enter the updated product description: ").strip()
                    elif detail_choice == '3':
                        while True:
                            try:
                                product_price = float(input("Enter the updated product price: "))
                                if product_price < 0:
                                    print("Price cannot be negative.")
                                else:
                                    product_details[3] = f"{product_price:.2f}"
                                    break
                            except ValueError:
                                print("Invalid input. Price must be a number.")
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
            


    

# Main function to run the program
def main():
    while True:
        print("\nInventory Management System")
        print("[1] Add a new product")
        print("[2] Update a product")
        print("[3] View Inventory")
        print("[4] Exit")

        try:
            selection = int(input("Enter your choice: "))
            if selection == 1:
                add_products()
            elif selection == 2:
                up_products()
            elif selection == 3:
                view()
            elif selection == 4:
                print("Exiting the program. Thank you!")
                break
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
