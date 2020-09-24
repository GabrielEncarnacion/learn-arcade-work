import random


def game_over():
    end = input("Would you like to play again? (Yes/No) ")
    if end.upper() == "Yes":
        main()
    if end.upper() == "No":
        print("WASTED")


def main():
    print("Welcome to GTA V Lester Chase")
    print("You have stolen money from Lester and he has sent a motorcycle gang to kill you.")
    print("Lester wants his money back and the gang is after you.")
    print("Stay alive or return the money to Lester.")

    done = False

    # Variables
    player_health = 100
    condition_of_money = 0
    miles_traveled = -10
    dist_traveled_p = -20
    gang_members = 6

    while not done:
        print()
        print("A. Heal up.")
        print("B. Go half speed.")
        print("C. Go full speed.")
        print("D. Stop for the night.")
        print("E. Status check.")
        print("F. Shoot.")
        print("Q. Return Money and Quit")
        choice = input("What is your choice? ")
        print()

        # if player quits
        if choice.upper() == "Q":
            done = True
            print("You quit")

        # if player heals up
        elif choice.upper() == "A":
            player_health = 100 #change if i play around
            print("health 100%")


        # if player does a status check
        elif choice.upper() == "E":
            print("You have traveled ", miles_traveled, "miles.")
            print("Their are", gang_members, " crew members left")
            print("The motorcycle gang is", miles_traveled - dist_traveled_p, "miles behind you.")


        # if player chooses to take the night
        elif choice.upper() == "D":
            player_health = 100
            print("You have regenerated health")
            dist_traveled_p += random.randrange(12, 23)


        # if player chooses to shoot
        elif choice.upper() == "F":
            print("You have shot down 1 more of the 6 motorcycle crew members")
            print("The motorcycle gang ", miles_traveled - dist_traveled_p, "miles behind you.")
            gang_members -= 1


        # if player chooses to go full speed
        elif choice.upper() == "C":
            miles_turn = random.randrange(11, 19)
            miles_traveled += miles_turn
            print("You have traveled ", miles_turn, "miles!")
            player_health -= 1
            condition_of_money += random.randrange(1, 4)
            dist_traveled_p += random.randrange(8, 15)


        # if Player chooses to go half speed
        elif choice.upper() == "B":
            miles_turn = random.randrange(6, 13)
            miles_traveled += miles_turn
            print("You have traveled ", miles_turn, "miles!")
            player_health -= 1
            condition_of_money -= 1
            dist_traveled_p += random.randrange(4, 14)

        # Player health
        if 4 < player_health <= 6:
            print("You are injured")

        elif player_health > 6:
            print("You have died because of a wound")
            done = True

            break

        # Money condition
        if 5 < condition_of_money <= 8:
            print("Take care of the money!!")

        elif condition_of_money > 8:
            print("You have lost all the money!")
            done = True

        # Motorcycle Gang distance
        if dist_traveled_p >= miles_traveled:
            print("The gang got you :(")
            done = True
            game_over()

        elif dist_traveled_p >= miles_traveled - 15 and dist_traveled_p < miles_traveled:
            print("They´re closing in!")

        # Winning the game
        if miles_traveled >= 45:
            print("You have made it alive!")
            print("You win!")
            done = True
            game_over()


if __name__ == "__main__":
    main()
