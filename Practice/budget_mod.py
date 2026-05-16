budget= int(input("Enter your budget: "))
print("The budget you have entered is ", budget)

itemp = int(input("Enter the price of the item you want to buy: \n"))
print(f"""(The price of the item you want to buy is {itemp})""")

if itemp < budget:
    print("Add the item to the cart")
    new_budget = budget - itemp
    print("The remaining budget is ", new_budget)

    nitemp = int(input("Enter the price of the item you want to buy: \n"))
   
    if nitemp <= new_budget:
        print("Add the item to the cart")
        updated_budget = new_budget - nitemp
        print("The updated budget is ", updated_budget)

        if updated_budget==0:
            print("We are out of budget. Our budget is finished")

    else:
        print("The second item is out of budget")
    
    

else:
    print("The item is out of budget")
