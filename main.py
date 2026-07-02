from inventory import *

while True:
    print("\nInventory Management System")
    print("1. Add Product")
    print("2. View Products")
    print("3. Search Product")
    print("4. Update Product")
    print("5. Delete Product")
    print("6. Sell Product")
    print("7. Low Stock Alert")
    print("8. Restock Product")
    print("9. Inventory Statistics")
    print("10. Exit")

    # Get valid menu choice from user
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= 10:
                break
            print("Please enter a valid menu option.")
        except ValueError:
            print("Please enter numbers only.")

    if choice == 1:
        add_products()
    elif choice == 2:
        view_product()
    elif choice == 3:
        search_product()
    elif choice == 4:
        update_product()
    elif choice == 5:
        del_product()
    elif choice == 6:
        sell_product()
    elif choice == 7:
        low_stock_alert()
    elif choice == 8:
        restock_product()
    elif choice == 9:
        inventory_statistics()
    elif choice == 10:
        exit_program()
    else:
        print("Invalid choice. Please try again.")
