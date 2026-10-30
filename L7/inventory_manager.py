import json
import os

from product import Product
from inventory import Inventory

"""File Handling"""
def load_inventory(inventory):
    if os.path.exists("inventory.json"):
        with open("inventory.json", "r") as f:
            data = json.load(f)
        for item in data:
            product = Product(item["id"], item["name"], item["price"], item["stock"])
            inventory.add_product(product)
        print("inventory.json found.\nInventory loaded successfully.")
    else:
        print("inventory.json not found. Starting with an empty inventory.")

def save_inventory(inventory):
    data = []
    for product in inventory.get_products():
        data.append({
            "id": product.get_product_id(),
            "name": product.get_name(),
            "price": product.get_price(),
            "stock": product.get_stock()
        })
    with open("inventory.json", "w") as f:
        json.dump(data, f, indent=4)

"""Option2"""
def add_product(inventory):
    print("Add New Product")
    product_id = input("Product ID: ")
    if inventory.search_product(product_id) is not None:
        print("Product ID already exists.")
        return
    name = input("Product Name: ")
    price = float(input("Price: "))
    stock = int(input("Stock Quantity: "))
    new_product = Product(product_id, name, price, stock)
    inventory.add_product(new_product)
    print("Product added successfully!")

"""Option3"""
def update_stock(inventory):
    product_id = input("Enter Product ID: ")
    product = inventory.search_product(product_id)
    if product is None:
        print("Product not found.")
        return
    print("\nProduct Found:")
    print(f"Name: {product.get_name()}\nStock: {product.get_stock()}\n")
    new_stock = int(input("New Stock Quantity: "))
    if product.update_stock(new_stock):
        print("\nStock updated successfully!")
    else:
        print("\nStock cannot be negative. Stock not updated.")

"""Option4"""
def search_product(inventory):
    product_id = input("Enter Product ID to search: ")
    product = inventory.search_product(product_id)
    if product is None:
        print("\nProduct not found.\n")
    else:
        print("\nProduct Found:")
        print("-" * 40)
        product.display_information()
        print("-" * 40)

def menu():
    print("-" * 10 + "Menu" + "-" * 10)
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("-" * 10 + "Menu" + "-" * 10)

inventory = Inventory()
load_inventory(inventory)

while True:
    menu()
    choice = input("Enter option: ")

    if choice == "1":
        inventory.display_all()
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