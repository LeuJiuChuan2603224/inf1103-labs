inventory = 0
quantity = 0
fail_count = 0
enter_quantity = ""

while True:
    enter_quantity = input("Enter the quantity of stock: ")
    if enter_quantity.isdigit() or (enter_quantity.startswith("-") and enter_quantity[1:].isdigit()): # since .isdigit only checks for string we can only hardcode to check for negative symbols
        enter_quantity = int(enter_quantity)
        if enter_quantity < 0:
             fail_count += 1
             print("Invalid input. Please enter a positive number.") 
        else:
            print ("You entered:", enter_quantity)
            quantity += enter_quantity
            print("Total quantity in stock:", quantity)
            if quantity>=500:
                print("You have exceed 500 units limt:",quantity)
                break
    elif enter_quantity.lower() == "quit":
            print("Total rejected/failed inputs:", fail_count)
            print("Total unit processed:", quantity)
            print("Thank You and Have A Nice Day!")
            break

    else:
        fail_count += 1
        print("Invalid input. Please enter a number or 'quit' to exit.")
    
  

