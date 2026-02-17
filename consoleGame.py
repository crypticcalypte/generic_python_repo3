player_location = "+"
not_PL = "-"
layout = f"-----------\n-----------\n-----------\n-----+-----\n"

#   1    -   11
# 1 -----------
# 2 -----------
# 3 -----------
# 4 -----------


player = {
    "name": "input",
    "loc": 4.6,
    "in_church": True
}

while player["in_church"] != False:
    print("while loop is working!")
    while player["loc"] == 4.6:
        layout = layout
        move = input(print("Before you stands a church. How do you proceed?\nEnter: NORTH, EAST, WEST, SOUTH"))


        if move == "NORTH":
            print("test")
            layout = f"-----------\n-----------\n-----+-----\n-----------\n"
            print(layout)
            player["loc"] = 3.6

        elif move == "EAST":
            print("east test")
            layout = f"-----------\n-----------\n-----------\n------+----\n"
            print(layout)
            player["loc"] = 4.6

        elif move == "WEST":
            print("west test")
            layout = f"-----------\n-----------\n-----------\n----+------\n"
            print(layout)
            player["loc"] = 4.6

        elif move == "SOUTH":
            player["in_church"] = False
            layout = f"-----------\n-----------\n-----------\n-----------\n"
            print(layout)
            player["loc"] = 5.6

        else:
            "the if statement worked but you didnt enter the right command!"


    player["in_church"] = False