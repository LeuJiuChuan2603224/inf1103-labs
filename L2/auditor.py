inventory = 0
quantity = 0

enter_quantity = ""

while True:
    enter_quantity = input("Enter the quantity of stock: ")
    if enter_quantity.isdigit() or (enter_quantity.startswith("-") and enter_quantity[1:].isdigit()):
        enter_quantity = int(enter_quantity)
        if enter_quantity < 0:
             print("Invalid input. Please enter a positive number.")
             
        else:
            print ("You entered:", enter_quantity)
    elif enter_quantity.lower() == "quit":
            print("Thank You and Have A Nice Day!")
            break
    else:
        print("Invalid input. Please enter a number or 'quit' to exit.")
    
  

