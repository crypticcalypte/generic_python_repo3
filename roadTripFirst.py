# import math

# must include:
# at least 5 trip variables
# 3 f-strings to display info
# 3 lists
# list indexing
# - use len() on at least one list
# at least one calculation
# 2 string methods - see link in pages

# what to define:
# - trip info: aka, driver name, trip name, car model, +2 other string variables
# - destinations list with 4 cities
# - distances list with miles between each city
# - one more list (snacks, clothes, entertainment, etc)
# - calc total distance and estimated gas cost
# - - gas_cost = (total_miles / miles_per_gallon) * price_per_gallon)

# ideas for what Else to define:
# - budget? enter a number and subtract the gas prices of the trip to get the remaining money you can spend
# - show_list command (if statement the goat)


print("Road Trip Planner")

trip_name = input()
if trip_name == "a":
    trip_name = "default"
driver_name = input()
if driver_name == "a":
    driver_name = "default"

# locs =

# tuple here so it can be indexed? sets can apparently be len()ed
# are tuples immutable? make it so you can add stuff to the list? -- yes they are use a list or set
# take advantage of sorted()
# nope! use a list. or a dictionary one of the two


print(f"{trip_name}, {driver_name}")

