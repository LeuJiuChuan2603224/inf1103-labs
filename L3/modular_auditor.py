inventory = 0
quantity = 0
fail_count = 0
enter_quantity = ""

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

while True:
    entered_quantity = get_valid_input()
    if entered_quantity == "quit":
        print("Thank You and Have A Nice Day!")
        break
    elif entered_quantity is None:
        fail_count += 1
    else: 
     
        if quantity>=500:
            print("You have exceed 500 units limt:",quantity)
            break
   
    
  

