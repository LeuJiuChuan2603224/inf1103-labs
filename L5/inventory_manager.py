import json
import os

def load_inventory():
    if os.path.exists("inventory.json"):
        with open("inventory.json", "r") as f:
            data = json.load(f)
        print("inventory.json found.\nInventory loaded successfully.")
        return data
    else:
        print("inventory.json not found. Starting with an empty inventory.")
        return []

# inventory = [
#     {"id": "P001", "name": "Laptop", "price": 1200.00, "stock": 15},
#     {"id": "P002", "name": "Mouse", "price": 25.00, "stock": 40},
#     {"id": "P003", "name": "Keyboard", "price": 45.00, "stock": 25}
# ]
"""Option1"""
def display_all():
    print("Current Inventory:")
    print("=" * 40)
    if len(inventory) ==0:
        print("Inventory is empty.")
    else:
        for i in inventory:
            print(f"ID: {i['id']}, Name: {i['name']}, Price: ${i['price']:.2f}, Stock: {i['stock']}")
    print("=" * 40)

"""Option2"""
def add_product(inventory):
    print("Add New Product")
    product_id = input("Product ID: ")
    name = input("Product Name: ")
    price = float(input("Price: "))
    stock = int(input("Stock Quantity: "))
    new_product = {"id": product_id, "name": name, "price": price, "stock": stock}
    inventory.append(new_product)
    print(f"Product added successfully!")

"""Option3"""
def update_stock(inventory):
    product_id = input("Enter Product ID: ")
    for product in inventory:
        if product["id"] == product_id:
            print("\nProduct Found:")
            print(f"Name: {product['name']}\nStock: {product['stock']}\n")
            new_stock = int(input(f"New Stock Quantity: "))
            product["stock"] = new_stock
            print("\nStock updated successfully!")
            return
    print("Product not found.")

"""Option4"""
def search_product(inventory):
    product_id = input("Enter Product ID to search: ")
    for product in inventory:
        if product["id"] == product_id:
            print("\nProduct Found:")
            print("-" * 40)
            print(f"ID: {product['id']}\nName: {product['name']}\nPrice: ${product['price']:.2f}\nStock: {product['stock']}")
            print("-" * 40)
            return
    print("\nProduct not found.\n")

"""Option5"""
def save_inventory(inventory):
    with open("inventory.json", "w") as f:
        json.dump(inventory, f, indent=4)

def menu():
    print("-" * 10 + "Menu" + "-" * 10)
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("-" * 10 +"Menu" + "-" * 10)

inventory = load_inventory()

while True:
    menu()
    choice = input("Enter option: ")

    if choice == "1":
        display_all()
    elif choice == "2":
         add_product(inventory)
    elif choice == "3":
         update_stock(inventory)
    elif choice == "4":
        search_product(inventory)
    elif choice == "5":
        save_inventory(inventory)
        print("\nSaving Inventory..")
        print("Inventory saved successfully to inventory.json.\n")
    elif choice == "6":
        print("Saving inventory before exit...")
        save_inventory(inventory)
        print("Inventory saved successfully\n")
        print("Thank you for using Inventory Management System.\nProgram terminated.")
        break
    else:
        print("Invalid option. Please try again.")

    