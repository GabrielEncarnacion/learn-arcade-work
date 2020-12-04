"""
Parents v Kid 2020
"""
from pprint import pprint
import random
import time
import math

# creating class variable "kid"


class Kid:
    def __init__(self, kid_health, kid_attack, kid_luck, kid_ranged, kid_defense, kid_name):
        self.kid_health = kid_health
        self.kid_attack = kid_attack
        self.kid_luck = kid_luck
        self.kid_ranged = kid_ranged
        self.kid_name = kid_name
        self.kid_defense = kid_defense
        print("kid_health", kid_health, "")

    # creating getters and setters for the class variable "kid"

    def get_health(self):
        return self.kid_health

    def get_attack(self):
        return self.kid_attack

    def get_luck(self):
        return self.kid_luck

    def get_ranged(self):
        return self.kid_ranged

    def get_name(self):
        return self.kid_name

    def get_defense(self):
        return self.kid_defense

    def set_health(self, new_health):
        self.kid_health = new_health

    def set_attack(self, new_attack):
        self.kid_attack = new_attack

    def set_luck(self, new_luck):
        self.kid_luck = new_luck

    def set_ranged(self, new_ranged):
        self.kid_ranged = new_ranged

    def set_name(self, new_name):
        self.kid_name = new_name

    def set_defense(self, new_defense):
        self.kid_defense = new_defense

 # Youtube/github, L. (2020, June 23). Advanced Text Adventure. Retrieved December 02, 2020,
# from https://github.com/learntocodeGCSE/AdvancedTextAdventure/blob/master/Advanced%20Text%20Adventure%20Part%201%20-%20Hero%20Class.py


# creating class variable "enemy"


class Enemy:

    def __init__(self, enemy_health, enemy_attack1, enemy_power, enemy_ranged, enemy_name):
        self.kid_health = enemy_health
        self.kid_attack = enemy_attack1
        self.kid_luck = enemy_power
        self.kid_ranged = enemy_ranged
        self.kid_name = enemy_name
        print("Health", enemy_health, "")

# creating getters and setters for the class variable "enemy"

    def get_health(self):
        return self.enemy_health

    def get_attack(self):
        return self.enemy_attack1

    def get_power(self):
        return self.enemy_power

    def get_ranged(self):
        return self.enemy_ranged

    def get_name(self):
        return self.enemy_name

    def set_health(self, new_health):
        self.enemy_health = new_health

    def set_attack(self, new_attack):
        self.enemy_attack1 = new_attack

    def set_power(self, new_power):
        self.enemy_power = new_power

    def set_ranged(self, new_ranged):
        self.enemy_ranged = new_ranged

    def set_name(self, new_name):
        self.enemy_name = new_name

# creating class variable "Boss"


class Boss:
    def __init__(self, enemy_health, enemy_attack1, enemy_power, enemy_ranged, enemy_name, enemy_super_power_move):
        super().__init__(enemy_health, enemy_attack1, enemy_power, enemy_ranged, enemy_name)

        self.SuperPowerMove = enemy_super_power_move

    def get_super(self):
        return self.SuperPowerMove

    def set_super(self, new_super_power_move):
        self.SuperPowerMove = new_super_power_move

# randomizing my files to choose random texts

    def enemy_gen(level_boss):
        file = open("adjectives.txt", "r")
        lines = file.readlines()
        adjectives = lines[random.randint(0, len(lines)-1)][:-1]
        file.close()
        file = open("colors.txt", "r")
        lines = file.readlines()
        colors = lines[random.randint(0, len(lines)-1)][:-1]
        file.close()

        if not level_boss:
            health = random.randint(50, 100)
            attack = random.randint(1, 10)
            special = random.randint(10, 20)
            chance = random.randint(1, 10)

            return Enemy(health, attack, special, chance, adjectives + "" + colors)

        else:
            health = random.randint(200, 250)
            attack = random.randint(20, 40)
            special = random.randint(50, 60)
            chance = random.randint(1, 8)

            return Enemy(health, attack, special, chance, adjectives + "" + colors)


level_boss = True


# Youtube/github, L. (2020, June 23). Advanced Text Adventure. Retrieved December 02, 2020,
# from https://github.com/learntocodeGCSE/AdvancedTextAdventure/blob/master/Advanced%20Text%20Adventure%20Part%202%20-%20Enemy%20Class%20%26%20Enemy%20Generator.py

# creating attack variables

def enemy_attack(hit_chance, attack_value, name, defense):
    print(name, "is getting ready to attack!!")
    hit = random.randint(0, 10)
    if hit_chance >= hit:
        print("You just hit the kid!")
        loss = attack_value - defense
        print("You keep on losing", loss, "health")
        return math.ceil(loss)
    else:
        print("The enemies missed!")
        return 0

# creating the chance and luck variables


def hitchance(luck):
    hit = random.randint(0, 4)
    if luck < hit:
        print("Swing and a miss!")
        return False

    else:
        print("You hit your parents!")
        return True


def isdead(health):
    if health < 1:
        return True
    else:
        return False

# loot variable


def loot(luck, gen_character1):
    loot_chance = random.randint(0, 4)
    if luck < loot_chance:
        print("NO LOOT FOR YOU!")
    else:
        table_num = random.randrange(0, 4)
        loot_table_list = ["items", "ranged", "defense", "attack"]
        item_type = loot_table_list[table_num]
        file = open(item_type + ".txt", "r")
        lines = file.readlines()

        print("Your parents dropped...")
        item = random.randint(0, len(lines) - 1)

        item_line = lines[item]
        split_item_line = item_line.split(",")

        name = split_item_line[0]
        value = int(split_item_line[1])

        print(name)

# if statements regarding what would happen if you choose to act in the game

    if item_type == "attack":
        gen_character1.set_attack(gen_character1.get_attack() + value)
        print("Your new attack is...")
        print(gen_character1.get_attack())

    elif item_type == "ranged":
        gen_character1.set_ranged(gen_character1.get_ranged() + value)
        print("Your new ranged attack is...")
        print(gen_character1.get_ranged())

    elif item_type == "defense":
        gen_character1.set_defense(gen_character1.get_defense() + value)
        print("Your new defense is...")
        print(gen_character1.get_defense())

# what you caused because of the contingency concept in the game
    else:

        if split_item_line[2] == "luck":
            gen_character1.set_luck(gen_character1.get_luck() + value)
            print("Your new Luck  is...")
            print(gen_character1.get_luck())

        elif split_item_line[2] == "health":
            gen_character1.set_health(gen_character1.get_luck() + value)
            print("Your new Health  is...")
            print(gen_character1.get_health())


gen_character = Kid(100, 10, 11, 12, 13, "Little Timmy")

pprint(vars(gen_character))

loot(100, gen_character)
loot(100, gen_character)
loot(100, gen_character)
loot(100, gen_character)
loot(100, gen_character)
loot(100, gen_character)


pprint(vars(gen_character))

# Youtube/github, L. (2020, July 2). Advanced Text Adventure. Retrieved December 02, 2020,
# from https://github.com/learntocodeGCSE/AdvancedTextAdventure/blob/master/Advanced%20Text%20Adventure%20Part%203.py


def create_class():
    a = input("Are you more afraid of mom(1) or more afraid of dad(2)?")
    while a != "1" and a != "2":
        print("Invalid Selection")
        a = input("Are you more afraid of mom(1) or more afraid of dad(2)?")

    kid_attack = 0
    kid_health = 0

    if a == "1":
        kid_health = 50
        kid_attack = 100

    elif a == "2":
        kid_health = 100
        kid_attack = 50

    input("Press enter to spin the bottle")
    time.sleep(0.9)
    print("Spinning Bottle...")
    kid_luck = random.randint(0, 4)
    print("Your Kid has", kid_luck, "Luck out of 4")

# Youtube/github, L. (2020, October 23). Advanced Text Adventure. Retrieved December 02, 2020,
# from https://github.com/learntocodeGCSE/AdvancedTextAdventure/blob/master/Advanced%20Text%20Adventure%20Part%204.py

    c = "3"
    time.sleep(1)
    kid_ranged = 0
    kid_defense = 0

    while c != "1" and c != "2":

        c = input("Are you more of a text(1) or call(2) your ex? ")

        if c == "1":
            kid_ranged = 100

        elif c == "2":
            kid_ranged = 50
        else:
            print("Invalid Selection")

    kid_name = input("What is your name? ")
    print("Welcome", kid_name, "!!")

    return kid_health, kid_attack, kid_luck, kid_ranged, kid_defense, kid_name


def game_over(enemy_dead):
    if enemy_dead == True:
        print("Time to fight again!")

    else:
        print("You are out health")
        print("Better luck next time!!")
        exit()

# Youtube/github, L. (2020, November 13). Advanced Text Adventure. Retrieved December 02, 2020,
# https://github.com/learntocodeGCSE/AdvancedTextAdventure/blob/master/Advanced%20Text%20Adventure%20Part%205%20COMPLETE.py
 # <<<<START OF GAME OF ADVENTURE>>>>
# intro to game


def display_intro():
    print("Its a Friday night, you are tired of school and fed up with your entire family.")
    print("You have decided to get full blasted Drunk.")
    print("Survive not getting caught Drunk by your family and you'll win!")
    print("Go back to your room and you lose :(")


class Room:
    def __init__(self, description, north, south, east, west, north_east, north_west, south_east, south_west):
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.north_east = north_east
        self.north_west = north_west
        self.south_east = south_east
        self.south_west = south_west


def main():
    room_list = []

    # Create room 0
    room = Room("You are in your bedroom" 
                " You can go (E) and go into the man cave, or go (SE) to the bar",
                None, None, 5, None, None, None, 6, None)
    room_list.append(room)
    time.sleep(2)

    random.randint(1, 2)

    # Create room 1
    room = Room("You are in a bathroom,\n"
                "You are doing your physiological needs,\n"
                "mom looks at you suspicious, get outta there!\n"
                "Go (S) for the Master Bedroom or go back to your room (Q)", None, 2, None, 0, None, None, None, None)
    room_list.append(room)
    time.sleep(2)

    # Create room 2
    room = Room("You are in the Master Bedroom,"
                " You threw up on moms bed and blamed it on the dog."
                " You either go to the gaming room (SE) and act innocent"
                " or go back to the bathroom (E)?", None, None, 3, None, None, None, 9, None)
    room_list.append(room)
    time.sleep(2)

    # Create room 3
    room = Room("You are in the bathroom,"
                " You are doing your physiological needs, get over it and do something better!\n"
                " The night is young"
                " Where do you wanna go?,"
                " (E) takes you to the movie room, "
                , None, 4, 8, 2, None, None, None, None)

    room_list.append(room)

    # Create room 4
    room = Room("You are in your sister's room."
                "Leave before her and her friends try and paint you!", None, None, 9, 3, None, None, None, None)
    room_list.append(room)

    # Create room 5
    room = Room("You are in Man Cave,"
                " Dad tells you that you cannot be in there, which gets you grounded and sent elsewhere."
                " You want to get back at Dad and go drink his whiskey at the bar, go (S) for it!"
                , 0, 6, None, None, None, None, None, None)
    room_list.append(room)

    # Create room 6
    room = Room("You are in the bar,"
                " You can only take a few drinks before dad finds out you are in here."
                " Dad is coming, but you are a lightweight and you are drunk!"
                " You have the option to call it a night (Q) or go to the living room (S)"
                , 0, 7, None, 5, None, None, None, None)
    room_list.append(room)

    # Create room 7
    room = Room("You are in the living room,"
                " Moms guests are there. Get out of there before they smell the alcohol on you!!"
                " Go (S) for the movie room and watch a movie or head (NW) to the bathroom to clean yourself up"
                , None, 8, None, None, None, 1, None, None)
    room_list.append(room)

    # Create room 8
    room = Room("You are in movie room, "
                " You watched The Walking Dead and now you want to shoot some zombies,"
                " Head (E) to the Gaming Room or go back to your room and call it a night (Q)"
                , 3, None, 9, None, None, None, None, None)
    room_list.append(room)

    # Create room 9
    room = Room("You are in the gaming room,"
                " You have got on Modern Warfare with your buddies and they have told their moms you are drunk."
                " You cussed them out and their moms called your mom!"
                " You are caught being drunk and have received physical punishment, being sent back to your room :( (Q)"
                , 4, None, None, 8, None, None, None, None)
    room_list.append(room)

    # Create the starting point
    current_room = 0

    # Create the boolean variable
    done = False
    while not done:
        print()
        print(room_list[current_room].description)
        user_input = input("What direction would you like to go? ")
        room_choice = user_input

        # Allow the user to go North
        if room_choice.upper() == "NORTH" or room_choice.upper() == "N":
            next_room = room_list[current_room].north
            if next_room is None:
                print()
                print("Sorry, you cannot go that way.")
            else:
                current_room = next_room

        # Allow the user to go South
        elif room_choice.upper() == "SOUTH" or room_choice.upper() == "S":
            next_room = room_list[current_room].south
            if next_room is None:
                print()
                print("Sorry, you cannot go that way.")
            else:
                current_room = next_room

        # Allow the user to go East
        elif room_choice.upper() == "EAST" or room_choice.upper() == "E":
            next_room = room_list[current_room].east
            if next_room is None:
                print()
                print("Sorry, you cannot go that way.")
            else:
                current_room = next_room

        # Allow the user to go West
        elif room_choice.upper() == "WEST" or room_choice.upper() == "W":
            next_room = room_list[current_room].west
            if next_room is None:
                print()
                print("Sorry, you cannot go that way.")
            else:
                current_room = next_room

        # Allow the user to go North East
        elif room_choice.upper() == "NORTH_EAST" or room_choice.upper() == "NE":
            next_room = room_list[current_room].north_east
            if next_room is None:
                print()
                print("Sorry, you cannot go that way.")
            else:
                current_room = next_room

        # Allow the user to go North West
        elif room_choice.upper() == "NORTH_WEST" or room_choice.upper() == "NW":
            next_room = room_list[current_room].north_west
            if next_room is None:
                print()
                print("Sorry, you cannot go that way.")
            else:
                current_room = next_room

        # Allow the user to go South East
        elif room_choice.upper() == "SOUTH_EAST" or room_choice.upper() == "SE":
            next_room = room_list[current_room].south_east
            if next_room is None:
                print()
                print("Sorry, you cannot go that way.")
            else:
                current_room = next_room

        # Allow the user to go South West
        elif room_choice.upper() == "SOUTH_WEST" or room_choice.upper() == "SW":
            next_room = room_list[current_room].south_west
            if next_room is None:
                print()
                print("Sorry, you cannot go that way.")
            else:
                current_room = next_room

        # Allow the user to quit the game
        elif room_choice.upper() == "QUIT" or room_choice.upper() == "Q":
            done = True
            print()
            print("You have chosen to go back to your room. WASTED!")

        # Create a statement for any inputs that do not match the game
        else:
            print()
            print("The server does not understand what you are trying to do. Please try again.")


class_data = create_class()

second = Kid(class_data[0], class_data[1], class_data[2], class_data[3], class_data[4], class_data[5])
pprint(vars(second))
display_intro()
# All copyright text is properly cited and all full credit is given to its authors.
main()
