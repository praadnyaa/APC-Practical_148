cart = []

cart.append("Apple")
cart.append("Milk")
cart.append("Bread")

print("Cart:", cart)

cart.remove("Milk")

print("After removing:", cart)

item = input("Search item: ")

if item in cart:
    print("Item found")
else:
    print("Item not found")

print("Total items:", len(cart))
