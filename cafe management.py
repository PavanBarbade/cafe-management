menu = {
    'piza' : 40,
    'Pasta' : 50,
    'Burger' : 60,
    'Salad' : 70,
    'Coffee' : 80,
}
print("WELCOME TO PYTHON RESTAURANT ")
print("Pizza: Rs 40\nPasta: Rs 50\nBurger: Rs 60\nSalad: Rs 70\nCoffee: Rs 80\n")

order_total = 0

item_1 = input ("Enter then name of itmen you want to order =")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item is {item_1} added in your orderd :")
else:
    print(f"the item is not {item_1} yet")
another_item =input("you want to add another item (yes/no) :")
if another_item == "yes":
    item_2 = input("enter the second item =")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"item_2 added in your order {item_2}")
    else:
        print("nhi item ")
else:
    print("no additional item will be added ")

print(f"total amout of order{order_total}")