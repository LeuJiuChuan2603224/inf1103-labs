inventory = 0
quantity = 0

enter_quantity = 0

while enter_quantity != "quit":
    enter_quantity = input("Enter the quantity of stock: ")
    if enter_quantity == "quit":
            print("Thank You and Have A Nice Day!")
            break
    elif enter_quantity.isdigit():
        enter_quantity = int(enter_quantity)
        print ("You entered:", enter_quantity)
    else:
        print("Invalid input. Please enter a number or 'quit' to exit.")
    
  

