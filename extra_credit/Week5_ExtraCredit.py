# name for coffee shop = python beans coffee shop
# need two dictionaries, one for price the other for the menu

# ------------------------ #

menu = {
    "Blackberry Tea": 4.50,
    "Raspberry Tea": 5.00,
    "Lemon Blueberry Tea": 5.50,
    "Strawberry Matcha Latte": 6.00
}

receipt = {
    "customer": " ",
    "drink": " ",
    "price": 0.0
}

customer_name = input("Customer's name: ")
drink_order = input("Customer's order: ")

receipt['customer'] = customer_name
receipt['drink'] = drink_order

if drink_order == "Blackberry Tea":
    receipt['price'] = menu["Blackberry Tea"]
elif drink_order == "Raspberry Tea":
    receipt['price'] = menu["Raspberry Tea"]
elif drink_order == "Lemon Blueberry Tea":
    receipt['price'] = menu["Lemon Blueberry Tea"]
elif drink_order == "Strawberry Matcha Latte":
    receipt['price'] = menu["Strawberry Matcha Latte"]

cost = receipt['price']

print(f"--- RECEIPT ---\nCUSTOMER: {customer_name}\nITEM: {drink_order}\nTOTAL: ${cost:.2f}")