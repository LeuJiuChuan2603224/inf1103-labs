

inventory = [
    {"id": "P001", "name": "Laptop", "price": 1200.00, "stock": 15},
    {"id": "P002", "name": "Mouse", "price": 25.00, "stock": 40},
    {"id": "P003", "name": "Keyboard", "price": 45.00, "stock": 25}
]

def display_all():
    print("Current Inventory:")
    print("=" * 40)
    if len(inventory) ==0:
        print("Inventory is empty.")
    else:
        for i in inventory:
            print(f"ID: {i['id']}, Name: {i['name']}, Price: ${i['price']:.2f}, Stock: {i['stock']}")
    print("=" * 40)

def menu():
    print("-" * 10 + "Menu" + "-" * 10)
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("-" * 10 +"Menu" + "-" * 10)

while True:
    menu()
    choice = input("Enter option: ")

    if choice == "1":
        display_all()
    elif choice == "2":
         False
    elif choice == "3":
         False
    elif choice == "4":
         False
    elif choice == "5":
        False
    elif choice == "6":
        print("Exiting the program.")
        break
    else:
        print("Invalid option. Please try again.")

    