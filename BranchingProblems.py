

# part one

# the problem:
# You run a pizza shop and promise delivery times based on distance from the store.
# Delivery Times:
# - 0-2 miles: 15 minutes
# - 3-5 miles: 25 minutes
# - 6-10 miles: 40 minutes
# - Over 10 miles: "Sorry, out of delivery range"
# Write a program that takes the distance in miles and outputs the delivery time or the out-of-range message.

# ----------------------------

program = input("Enter 'pizza' to see the pizza problem (#2), 'coffee' to see the coffee problem (#4), or 'thermostat' to see the thermometer problem (#6). ")

if program == "pizza":
    total_miles = int(input("Distance in miles: "))
    total_mins = 0

    if 0 <= total_miles <= 2:
        total_mins = 15
    elif 3 <= total_miles <= 5:
        total_mins = 25
    elif 6 <= total_miles <= 10:
        total_mins = 40
    else:
        print("Sorry, out of delivery range.")

    print(f"Total time = {total_mins}.")


elif program == "coffee":
    # ------------ theyre all doing coffee so i wanna do that too ------------

    coffee_size = (input("Enter the size: "))
    shot_count = input("Is there an extra shot?: ")
    coffee_price = 0

    if coffee_size == "small":
        coffee_price = 3
    elif coffee_size == "medium":
        coffee_price = 4
    elif coffee_size == "large":
        coffee_price = 5
    else:
        print("Please choose a different size.")

    if shot_count == "yes":
        coffee_price = coffee_price + 2
    else:
        coffee_price = coffee_price

    print(f"Total price is: ${coffee_price}.")

elif program == "thermostat":
    # ------------ one more. for good measure ------------

    temp = int(input("What's the temperature?: "))

    if temp < 32:
        print("Freezing - pipes may burst!")
    elif 32 <= temp <= 50:
        print("Very cold")
    elif 51 <= temp <= 65:
        print("Cool")
    elif 66 <= temp <= 75:
        print("Comfortable")
    elif 76 <= temp <= 85:
        print("Warm")
    elif 86 <= temp <= 95:
        print("Hot")
    elif 95 < temp:
        print("Extreme heat - stay hydrated!")