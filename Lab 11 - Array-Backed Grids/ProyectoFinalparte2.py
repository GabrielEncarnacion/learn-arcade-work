from pprint import pprint
import random
import time
import math

class Kid:
    def __init__(self, kHealth, kAttack, kLuck, kRanged, kDefense, kName):
        self.kHealth = kHealth
        self.kAttack = kAttack
        self.kLuck = kLuck
        self.kRanged = kRanged
        self.kName = kName
        self.kDefense = kDefense
        print("kHealth", kHealth, "")
    def getHealth(self):
        return self.kHealth

    def getAttack(self):
        return self.kAttack

    def getLuck(self):
        return self.kLuck

    def getRanged(self):
        return self.kRanged

    def getName(self):
        return self.kName

    def getDefense(self):
        return self.kDefense

    def setHealth(self, newHealth):
        self.kHealth = newHealth

    def setAttack(self, newAttack):
        self.kAttack = newAttack

    def setLuck(self, newLuck):
        self.kLuck = newLuck

    def setRanged(self, newRanged):
        self.kRanged = newRanged

    def setName(self, newName):
        self.kName = newName

    def setDefense(self, newDefense):
        self.kDefense = newDefense

class enemy:
    def __init__(self, eHealth, eAttack, ePower, eRanged, eName):
        self.kHealth = eHealth
        self.kAttack = eAttack
        self.kLuck = ePower
        self.kRanged = eRanged
        self.kName = eName
        print("Health", eHealth, "")

    def getHealth(self):
        return self.eHealth

    def getAttack(self):
        return self.eAttack

    def getPower(self):
        return self.ePower

    def getRanged(self):
        return self.eRanged

    def getName(self):
        return self.eName

    def setHealth(self, newHealth):
        self.eHealth = newHealth

    def setAttack(self, newAttack):
        self.eAttack = newAttack

    def setPower(self, newPower):
        self.ePower = newPower

    def setRanged(self, newRanged):
        self.eRanged = newRanged

    def setName(self, newName):
        self.eName = newName

class boss:
    def __init__(self, eHealth, eAttack, ePower, eRanged, eName, eSuperPowerMove):
        super().__init__(eHealth, eAttack, ePower, eRanged, eName)

        self.SuperPowerMove = eSuperPowerMove

    def getSuper(self):
        return self.SuperPowerMove

    def setSuper(self, newSuperPowerMove):
        self.SuperPowerMove = newSuperPowerMove

    def enemyGen(levelBoss):
        temperature = []
        file = open("adjectives.txt", "r")
        lines = file.readlines()
        adjectives = lines[random.randint(0, len(lines)-1)][:-1]
        file.close()
        file = open("colors.txt", "r")
        lines = file.readlines()
        colors = lines[random.randint(0, len(lines)-1)][:-1]
        file.close()

        if levelBoss == False:
            health = random.randint(50, 100)
            attack = random.randint(1, 10)
            special = random.randint(10, 20)
            chance = random.randint(1, 10)

            return enemy(health, attack, special, chance, adjectives+""+colors)

        else:
            health = random.randint(200, 250)
            attack = random.randint(20, 40)
            special = random.randint(50, 60)
            chance = random.randint(1, 8)
            SuperPowerMove = random.randint(100, 200)

            return enemy(health, attack, special, chance, adjectives+""+colors, SuperPowerMove)


levelBoss = True


def enemyAttack(hitChance, attackValue, name, defense):
    print(name, "is getting ready to attack!!")
    hit = random.randint(0, 10)
    if hitChance >= hit:
        print("you just hit the Kid!")
        loss = attackValue - defense
        print("You keep on losing", loss, "health")
        return math.ceil(loss)
    else:
        print("The enemies missed!")
        return 0

def hitChance(luck):
    hit = random.randint(0, 4)
    if luck < hit:
        print("Swing and a miss!")
        return False

    else:
        print("You hit your parents")
        return True

def isDead(health):
    if health < 1:
        return True
    else:
        return False

def loot(luck, genCharacter):
    lootChance = random.randint(0, 4)
    if luck < lootChance:
        print("NO LOOT FOR YOU!")
    else:
        tableNum = random.randrange(0, 4)
        lootTableList = ["items", "ranged", "defense", "attack"]
        itemType = lootTableList[tableNum]
        file = open(itemType + ".txt", "r")
        lines = file.readlines()

        print("Your parents dropped...")
        item = random.randint(0, len(lines) - 1)

        itemLine = lines[item]
        splitItemLine = itemLine.split(",")

        name = splitItemLine[0]
        value = int(splitItemLine[1])

        print(name)
    if itemType == "attack":
        genCharacter.setAttack(genCharacter.getAttack() + value)
        print("Your new attack is...")
        print(genCharacter.getAttack())

    elif itemType == "ranged":
        genCharacter.setRanged(genCharacter.getRanged() + value)
        print("Your new Ranged Attack is...")
        print(genCharacter.getRanged())

    elif itemType == "defense":
        genCharacter.setDefense(genCharacter.getDefense() + value)
        print("Your new defense is...")
        print(genCharacter.getDefense())

    else:

        if splitItemLine[2] == "luck":
            genCharacter.setLuck(genCharacter.getLuck() + value)
            print("Your new Luck  is...")
            print(genCharacter.getLuck())

        elif splitItemLine[2] == "health":
            genCharacter.setHealth(genCharacter.getLuck() + value)
            print("Your new Health  is...")
            print(genCharacter.getHealth())

genCharacter = Kid(100, 10, 11, 12, 13,  "Gabriel")

pprint(vars(genCharacter))

loot(100, genCharacter)
loot(100, genCharacter)
loot(100, genCharacter)
loot(100, genCharacter)
loot(100, genCharacter)
loot(100, genCharacter)



pprint(vars(genCharacter))



def createClass():
    a = input("Are you more afraid of mom(1) or more afraid of dad(2)?")
    while a != "1" and a != "2":
        print("Invalid Selection")
        a = input("Are you more afraid of mom(1) or more afraid of dad(2)?")

    if a == "1":
        kHealth = 50
        kAttack = 100

    elif a == "2":
        kHealth = 100
        kAttack = 50

    b = input("Press enter to spin the bottle")
    time.sleep(0.9)
    print("Spinning Bottle...")
    kLuck = random.randint(0, 4)
    print("Your Kid has", kLuck, "Luck out of 4")

    c = "3"
    time.sleep(1)
    kRanged = 0
    kName = 0
    kAttack = 0
    kHealth = 0
    kDefense = 0
    while c!= "1" and c!= "2":

        c = input("Are you more of a text(1) or call(2) your ex?")

        if c == "1":
            kRanged = 100

        elif c == "2":
            kRanged = 50
        else:
            print("Invalid Selection")

    kName = input("What is your name?")
    print("Welcome", kName, "!!")

    return(kHealth, kAttack, kLuck, kRanged, kDefense, kName)


class_data = createClass()

character = Kid(class_data[0], class_data[1], class_data[2], class_data[3], class_data[4], class_data[5])

print(vars(character))


def displayintro():
    print("Its a Friday night, you are tired of school and fed up with your entire family.")
    print("You have decided to get full blasted Drunk.")
    print("Survive not getting caught Drunk by your family and you'll win!")
    print("Go back to your room and you lose :(")


 # <<<<START OF GAME>>>>>>>


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
                " You can go (E) and go into the man cave, or go (SE) to the bar", None, None, 5, None, None, None, 6, None)
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
                " You are doing your physiological needs, get over it and do something better!"
                " The night is young"
                " Where do you wanna go?,"
                " (E) takes you to the movie room, "
                , None, 4, 8, 2, None, None, None, None)

    room_list.append(room)

    # Create room 4
    room = Room("You are in your sisters room"
                "Leave before her and her friends try and paint you!", None, None, 9, 3, None, None, None, None)
    room_list.append(room)

    # Create room 5
    room = Room("You are in Man Cave,"
                " Dad tells you that you cannot be in there, which gets you grounded and sent elsewhere."
                " You want to get back at Dad and go drink his whiskey at the bar, go (S) for it!", 0, 6, None, None, None, None, None, None)
    room_list.append(room)

    # Create room 6
    room = Room("You are in Bar,"
                " You can only take a few drinks before dad finds out you are in here."
                " Dad is coming, but you are a lightweight and you are Drunk!"
                " You have the option to call it a night (Q) or go to the living room (S)"
                , 0, 7, None, 5, None, None, None, None)
    room_list.append(room)

    # Create room 7
    room = Room("You are in the Living Room,"
                " Moms guests are there. Get out of there before they smell the alcohol on you!!"
                " Go (S) for the movie room and watch a movie or head (NW) to the bathroom to clean yourself up"
                , None, 8, None, None, None, 1, None, None)
    room_list.append(room)

    # Create room 8
    room = Room("You are in Movie Room, "
                " You watched The Walking Dead and now you want to shoot some zombies,"
                " Head (E) to the Gaming Room or go back to your room and call it a night (Q)", 3, None, 9, None, None, None, None, None)
    room_list.append(room)

    # Create room 9
    room = Room("You are in the Gaming Room,"
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

        # Allow the user to go North_east
        elif room_choice.upper() == "NORTH_EAST" or room_choice.upper() == "NE":
            next_room = room_list[current_room].north_east
            if next_room is None:
                print()
                print("Sorry, you cannot go that way.")
            else:
                current_room = next_room

        # Allow the user to go North_west
        elif room_choice.upper() == "NORTH_WEST" or room_choice.upper() == "NW":
            next_room = room_list[current_room].north_west
            if next_room is None:
                print()
                print("Sorry, you cannot go that way.")
            else:
                current_room = next_room

        # Allow the user to go North_east
        elif room_choice.upper() == "SOUTH_EAST" or room_choice.upper() == "SE":
            next_room = room_list[current_room].south_east
            if next_room is None:
                print()
                print("Sorry, you cannot go that way.")
            else:
                current_room = next_room

        # Allow the user to go North_west
        elif room_choice.upper() == "SOUTH_WEST" or room_choice.upper() == "SW":
            next_room = room_list[current_room].south_west
            if next_room is None:
                print()
                print("Sorry, you cannot go that way.")
            else:
                current_room = next_room

        # Allow the user to end the game
        elif room_choice.upper() == "QUIT" or room_choice.upper() == "Q":
            done = True
            print()
            print("You have chosen to go back to your room. WASTED!")

        # Create a statement for any inputs that do not match the game
        else:
            print()
            print("The server does not understand what you are trying to do. Please try again.")


en1 = createClass()

second = Kid(class_data[0], class_data[1], class_data[2], class_data[3], class_data[4], class_data[5])
pprint(vars(second))
displayintro()
main()