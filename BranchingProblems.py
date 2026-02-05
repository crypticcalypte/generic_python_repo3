

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

total_miles = int(input("Distance in miles:"))
total_mins = 1

if 0 <= total_miles <= 2:
    total_mins = 15
    print(f"Total time = {total_mins}.")
elif 3 <= total_miles <= 5:
    total_mins = 25
    print(f"Total time = {total_mins}.")
elif 6 <= total_miles <= 10:
    total_mins = 40
    print(f"Total time = {total_mins}.")
else:
    print("Sorry, out of delivery range.")