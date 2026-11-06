import json
import os

from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from can_be_shipped import CanBeShipped
from inventory import Inventory

"""File Handling"""
def create_product_from_data(item):
    # The saved "type" decides which subclass gets rebuilt
    if item.get("type") == "physical":
        return PhysicalProduct(item["id"], item["name"], item["price"], item["stock"], item["weight"])
    if item.get("type") == "digital":
        return DigitalProduct(item["id"], item["name"], item["price"], item["stock"], item["download_size"])
    return None

def load_inventory(inventory):
    if os.path.exists("inventory.json"):
        with open("inventory.json", "r") as f:
            data = json.load(f)
        for item in data:
            product = create_product_from_data(item)
            if product is None:
                print(f"Skipping product {item.get('id')}: unknown type {item.get('type')}.")
            else:
                inventory.add_product(product)
        print("inventory.json found.\nInventory loaded successfully.")
    else:
        print("inventory.json not found. Starting with an empty inventory.")

def save_inventory(inventory):
    data = []
    for product in inventory.get_products():
        data.append(product.to_dict())
    with open("inventory.json", "w") as f:
        json.dump(data, f, indent=4)

"""Option2"""
def add_product(inventory):
    print("Add New Product")
    product_type = input("Product Type (1 = Physical, 2 = Digital): ")
    if product_type not in ("1", "2"):
        print("Invalid product type.")
        return
    product_id = input("Product ID: ")
    if inventory.search_product(product_id) is not None:
        print("Product ID already exists.")
        return
    name = input("Product Name: ")
    price = float(input("Price: "))
    stock = int(input("Stock Quantity: "))
    if product_type == "1":
        weight = float(input("Weight (kg): "))
        new_product = PhysicalProduct(product_id, name, price, stock, weight)
    else:
        download_size = float(input("Download Size (MB): "))
        new_product = DigitalProduct(product_id, name, price, stock, download_size)
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
        print(product.get_fulfilment_info())
        if isinstance(product, CanBeShipped):
            print(f"Shipping Cost: ${product.calculate_shipping_cost():.2f}")
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

def main():
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

if __name__ == "__main__":
    main()