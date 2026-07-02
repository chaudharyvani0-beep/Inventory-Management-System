from helper import get_positive_integer
from file_handler import load_inventory, save_inventory


inventory = load_inventory()

# FUNCTION TO ADD PRODUCTS

def add_products():
    id = get_positive_integer("Enter Product ID: ")
    name = input("Enter Product Name: ")
    price = get_positive_integer("Enter Price: ")
    quantity = get_positive_integer("Enter Quantity: ")

    product = {
        "id" : id ,
        "name" : name, 
        "price" : price,
        "quantity" : quantity
    }

    for item in inventory:
        if item["id"]==id:
            print("product already exist .")
            return
    inventory.append(product)
    save_inventory(inventory)
    print("Product added successfully.")


# FUNCTION TO VIEW PRODUCT

def view_product():

    if not inventory:
        print("No products available.")
        return

    print("=" * 50)
    print(f"{'ID':<8}{'NAME':<15}{'PRICE':<10}{'QTY'}")
    print("=" * 50)

    for product in inventory:
        print(
            f"{product['id']:<8}"
            f"{product['name']:<15}"
            f"{product['price']:<10}"
            f"{product['quantity']}"
        )

    print("=" * 50)

# FUNCTION TO SEARCH PRODUCT BY ID OR NAME

def search_product():
    

    choice = input("Search by (1) ID or (2) Name : ")

    if choice == "1":
        id = get_positive_integer("Enter Product ID: ")

        for product in inventory:
            if product["id"] == id:
                print("=" * 30)
                print(f"ID       : {product['id']}")
                print(f"Name     : {product['name']}")
                print(f"Price    : ₹{product['price']}")
                print(f"Quantity : {product['quantity']}")
                print("=" * 30)
                return

    elif choice == "2":
        name = input("Enter Product Name: ").lower()

        for product in inventory:
            if product["name"].lower() == name:
                print("=" * 30)
                print(f"ID       : {product['id']}")
                print(f"Name     : {product['name']}")
                print(f"Price    : ₹{product['price']}")
                print(f"Quantity : {product['quantity']}")
                print("=" * 30)
                return

print("Product not found.")


# FUNCTION TO UPDATE PRODUCT DETAILS
def update_product():
    id = get_positive_integer("Enter Product ID: ")

    

    for product in inventory:
        if product["id"] == id:
            product["name"] = input("Enter new name: ")
            product["price"] = get_positive_integer("Enter new price: ")
            product["quantity"] = get_positive_integer("Enter new quantity: ")

            save_inventory(inventory)
            print("Product updated successfully.")
            return

    print("Product not found.")
# FUNCTION TO DELETE PRODUCT

def del_product():
    id = get_positive_integer("Enter Product ID: ")
    for product in inventory:
        if product["id"] == id :
            inventory.remove(product)
            save_inventory(inventory)
            print("Product deleted successfully.")
            return
print("Product not found.")
        
# FUNCTION TO SELL PRODUCT
        
def sell_product():
    id = get_positive_integer("Enter Product ID: ")
    quantity = get_positive_integer("Enter quantity to sell: ")
    for product in inventory:
        if product["id"] == id:
            if product["quantity"] >= quantity:
                total_bill = product["price"] * quantity
                product["quantity"] -= quantity
                save_inventory(inventory)
                print("\n")
                print("="*35)
                print("        SALES BILL")
                print("="*35)
                print(f"Product      : {product['name']}")
                print(f"Price        : ₹{product['price']}")
                print(f"Quantity     : {quantity}")
                print("-"*35)
                print(f"Total Amount : ₹{total_bill}")
                print("-"*35)
                print(f"Remaining    : {product['quantity']}")
                print("="*35)
            else:
                print("Insufficient stock to sell.")
                return
print("Product not found.")
            
# FUNCTION TO ALERT LOW STOCK PRODUCTS

def low_stock_alert():
    low_stock_found = False
    for product in inventory:
        if product["quantity"] < 10:
            print(f"{product['name']} → Stock Left: {product['quantity']}")
            low_stock_found = True
    if not low_stock_found:
        print("No low stock items.")

# FUNCTION TO RESTOCK PRODUCT

def restock_product():
    id = get_positive_integer("Enter Product ID: ")
    quantity = get_positive_integer("Enter Quantity: ")
    for product in inventory:
        if product["id"] == id:
            product["quantity"] += quantity
            save_inventory(inventory)
            print(f"Restocked {quantity} of {product['name']}. New quantity: {product['quantity']}")
            return
    print("Product not found.")

# FUNCTION TO DISPLAY INVENTORY STATISTICS

def inventory_statistics():
    if not inventory:
        print("No products available.")
        return
    total_products = len(inventory)
    total_quantity = 0 
    total_value = 0 
    most_expensive = inventory[0]
    cheapest = inventory[0]
    
    for product in inventory:
        total_quantity += product["quantity"]
        total_value += product["price"] * product["quantity"]
        if product["price"] > most_expensive["price"]:
            most_expensive = product

        if product["price"] < cheapest["price"]:
            cheapest = product

    print("\n========== INVENTORY STATISTICS ==========")
    print(f"Total Products        : {total_products}")
    print(f"Total Quantity        : {total_quantity}")
    print(f"Total Inventory Value : ₹{total_value}")
    print(
        f"Most Expensive        : {most_expensive['name']} (₹{most_expensive['price']})"
    )
    print(
        f"Cheapest Product      : {cheapest['name']} (₹{cheapest['price']})"
    )
    print("==========================================")

# FUNCTION TO EXIT PROGRAM

def exit_program():
    print("Exiting the program.")
    exit()