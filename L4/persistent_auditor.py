FILENAME = "inventory.txt"

def load_inventory(file):
    total=0
    history=[]
    file=open("inventory.txt", "a")
    file.close()

    with open("inventory.txt", "r") as file:
        data = file.readlines()
 
        if len(data) >= 1 and data[0].strip() != "":
            total = int(data[0].strip())
 
        if len(data) >= 2 and data[1].strip() != "":
            history = [int(item) for item in data[1].strip().split(",")]
 
    print(f"Inventory loaded. Starting total: {total}")
    return total, history


def get_valid_input():
    enter_quantity = input("Enter the quantity of stock: ")
    if enter_quantity.lower() == "quit":
        return "quit"
    elif enter_quantity.isdigit() or (enter_quantity.startswith("-") and enter_quantity[1:].isdigit()):
         enter_quantity = int(enter_quantity)
         if enter_quantity < 0:
            print("Invalid input. Please enter a positive number.")
            return None
         else:
            print ("You entered:", enter_quantity)
            return enter_quantity
    else:
      print("Invalid input. Please enter a number or 'quit' to exit.")   
      return None

def process_delivery(current_total, new_value):
    return current_total + new_value

def calculate_tax(amount):
    return amount * 0.1

def generate_report(total_units, failed_attempts): 
    print("Total quantity in stock:", total_units)
    print("Failed attempts:", failed_attempts)


quantity, transaction_history = load_inventory('inventory.txt')
fail_count = 0
while True:
    result = get_valid_input()
    if result == "quit":
        generate_report(quantity,fail_count)
        print("Thank You and Have A Nice Day!")
        break
    elif result is None:
        fail_count += 1
        generate_report(quantity,fail_count)
    else: 
        quantity = process_delivery(quantity, result)
        tax = calculate_tax(result)
        if quantity>=500:
            print("You have exceed 500 units limt:",quantity)
            break
        else:
            generate_report(quantity,fail_count)
            print("Tax:", f"${tax:.2f}")
   
    
  

