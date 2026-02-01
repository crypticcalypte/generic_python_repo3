
# this is the file you need to look at for bare minimums; go look at roadTripFirst if you want inputs

# variables that apparently ARENT inputs
trip_name = "From Los Angeles, CA to Seattle, WA"
driver_name = "DJ"
car_model = "Volkswagen Beetle"
current_year = "1975"
trip_reason = "To visit Pike Place Market"
# testing edits here
# lmao i forgot to publish it ACTUALLY testing edits now


# gas
mpg = int(29)
gas_price = float(0.70)
act_gas_price = int(gas_price * 100)
total_dist = 1143
gas_cost = ((total_dist / mpg) * act_gas_price) / 100
act_gas_cost = round(gas_cost, 2)

modern_gas_price = float(4.417)
mod_gas_cost = ((total_dist / mpg) * modern_gas_price)
act_mod_gas_cost = round(mod_gas_cost, 2)

packed = ["Lunch", "Pop Glass", "Luggage Case", "Shark Plush", "Locket"]
packed_list = set(packed)

# destinations
locations = ["Los Angeles, CA", "Sacramento, CA", "Mt. Shasta, CA", "Eugene, OR", "Portland, OR", "Olympia, WA", "Seattle, WA"]
locs_list = set(locations)
# LA -> SC = 384 miles / sc -> ms = 220 / ms -> eu = 253 / eu -> pr = 110 / pr -> ol = 115 / ol -> sea = 61
locs_dist = {
    "LASA": 384,
    "SAMT": 220,
    "MTEU": 253,
    "EUPO": 110,
    "POOL": 115,
    "OLSE": 61
}

num_stops = len(locs_list)
first_stop = locations[1]
last_stop = locations[-2]

print(f"=== {trip_name} ===")
print(f"Why?\n{trip_reason}")
print(f"Who?\n{driver_name}")
print(f"What car is she driving?\n{car_model}")
print(f"... what year is it?\n{current_year}")
print(f"What are her stops?\n{locations}")
print(f"How many stops are there?\n{num_stops}")
print(f"What's the first stop?\n{first_stop}")
print(f"What's the last stop?\n{last_stop}")
print("--------")
print(f"How much is gas?\n$0.{act_gas_price} cents per gallon.")
print(f"How many miles is she going?\n{total_dist}mi.")
print(f"How much will it cost her?\nAbout ${act_gas_cost}")
print(f"How much would it cost her today?\nAbout ${act_mod_gas_cost}*")
print(f"*Take this with a grain of salt. My math might be wrong and it doesn't account for changing gas prices.")
print("--------")
# what else do i got uhhhhhhhh
