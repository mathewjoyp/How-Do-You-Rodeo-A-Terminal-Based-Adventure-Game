import random
import time


def shooting_game(p1):
    #Available guns in the game
    GUNS = {0.6: "Pistol", 0.7: "Revolver", 0.8: "Rifle"}
    print(f"You've chosen {GUNS[p1.gun]} with accuracy {p1.gun}. Let's start shooting!")
    bottles_hit = 0

    try:
        choice = input("Press 's' to shoot:")
        if choice.lower() == "s":
            for bottle in range(3):
                time.sleep(1)
                if random.random() <= p1.gun:
                    #Checking if the shot is hit
                    print(f"You hit bottle {bottle + 1}!")
                    bottles_hit += 1
                else:
                    print(f"You missed bottle {bottle + 1}.")
            #Winning condition
            if bottles_hit == 3:
                print("Congratulations! You hit all three bottles.")
                return True
            else:
                print("You missed some bottles. Try again next time.")
                return False

        else:
            print("Press 's' to shoot")

    except:
        print("Invalid input")
