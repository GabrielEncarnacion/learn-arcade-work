class Room:
    def __init__(self, description, north, east, south, west):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west


def main():

    room_list: []

    # Room Descriptions 0-9
    room = Room(" You are in a kids bedroom", None, 1, 5, None)
    room_list.append(room)

    room = Room("You are in a bathroom", None, 2, 7, 0)
    room_list.append(room)

    room = Room("You are in the Master Bedroom", None, 3, 7, 1)
    room_list.append(room)

    room = Room("You are in a bathroom", None, 4, 8, 2)
    room_list.append(room)

    room = Room("You are in a Kids Room", None, None, 9, 3)
    room_list.append(room)

    room = Room("You are in Man Cave", 0, 6, None, None)
    room_list.append(room)

    room = Room("You are in Bar", 0, 7, None, 5)
    room_list.append(room)

    room = Room("You are Living Room", 1, 8, None, 6)
    room_list.append(room)

    room = Room("You are in Movie Room", 3, 9, None, 7)
    room_list.append(room)

    room = Room("You are in Gaming Room", 4, None, None, 8)
    room_list.append(room)

    current_room = 0

    done = False

    while not done:
        print(room_list[current_room].description)
        print()
        user_input = input("Where do you wanna go?.")
        room_choice = user_input

        if room_choice.upper() == "North" or room_choice.upper() == "N":
            next_room = room_list[current_room].north
            if next_room is None:
                print("Not this way.")
                print()
            else:
                current_room = next_room

        elif room_choice.upper() == "South" or room_choice.upper() == "S":
            next_room = room_list[current_room].south
            print()
            if next_room is None:
                print("Not that way.")
                print()
            else:
                current_room = next_room

        elif room_choice.upper() == "East" or room_choice.upper() == "E":
            next_room = room_list[current_room].east
            print()
            if next_room is None:
                print("Not that way.")
                print()
            else:
                current_room = next_room

        elif room_choice.upper() == "West" or room_choice.upper() == "W":
            next_room = room_list[current_room].west
            print()
            if next_room is None:
                print("Not that way.")
                print()
            else:
                current_room = next_room

        elif room_choice.upper() == "Quit" or room_choice.upper() == "Q":
            done = True
            print()
            print("Quitter.")

        else:
            print()
            print("ERROR 404. Try Again.")


main()