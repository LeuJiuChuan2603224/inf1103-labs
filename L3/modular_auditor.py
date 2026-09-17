inventory = 0
quantity = 0
fail_count = 0


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

while True:
    result = get_valid_input()
    if result == "quit":
        print("Thank You and Have A Nice Day!")
        break
    elif result is None:
        fail_count += 1
    else: 
        quantity = process_delivery(quantity, result)
        if quantity>=500:
            print("You have exceed 500 units limt:",quantity)
            break
        else:
            print("Total quantity in stock:", quantity)
   
    
  

