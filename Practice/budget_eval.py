budget= int(input("Enter your budget: "))
print("The budget you have entered is ", budget)

price_of_item = int(input("Enter the price of the item you want to buy: \n"))
print(f"""(The price of the item you want to buy is {price_of_item})""")

if price_of_item > budget:
    print("The item is out of budget")

else:
    print("Add the item to the cart")
    print("The remaining budget is ", budget-price_of_item)
