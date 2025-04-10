#hotel menu
#define the menu of restaurant
menu = {
        "pizza":50,
        "burger":30,
        "pasta":40,
        "salad":20,
        "soda":10,
        "water":5,
        "juice":15,
        "coffee":25,
        "tea":10,
        "cake":30,
        "ice cream":20,
        "sandwich":25,
        "fries":15,
        "wings":40,
        "steak":100,
        "seafood":80

}
#greet
print("Welcome to the restaurant!")
print("Here is the menu:")
#display the menu
for item, price in menu.items():
    print(f"{item}: ${price}")
order_total = 0
#take order
item_1= input("Please enter the item you want to order =")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your order for {item_1} has been added to your bill.")
else:
    print(f"Sorry, we don't have {item_1} on the menu.")   
another_order = input("Do you want to order another item? (yes/no)") 
if another_order == "yes":
    item_2= input("Please enter the item you want to order =")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your order for {item_2} has been added to your bill.")
    else:
        print(f"Sorry, we don't have {item_2} on the menu.")
print(f"Your total bill is ${order_total}.")
