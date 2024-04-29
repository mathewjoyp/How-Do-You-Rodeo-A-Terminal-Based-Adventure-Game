#Import required modules
import sys
import time
import random
import msvcrt

#Defining attributes
class Person:
    def __init__(self, name, likeability, hp, money, bottle, gun):
        self.name = name
        self.likeability = likeability
        self.hp = hp
        self.money = money
        self.bottle = bottle
        self.gun = gun

#Function for animating text and skipping animation if necessary
def del_print(string):
    try:
        read = msvcrt.getch().decode().lower()

        for char in string:
            if read == "s":
                print(string)
                break
            print(char, end="")
            sys.stdout.flush()
            time.sleep(0.05)

    except:
        print()

#We have defined each path as functions which change player attributes and calls subsequent path functions depending on attributes and user inputs

def fight2(p1):
    del_print(
        "As you continue your journey, you start to lose hope in survival due to your supplies starting to run low\n"
    )
    del_print(
        "You find an oasis of water but are unsure if this is another one of your mirages\n"
    )
    del_print(
        "You see a man running from the other side towards the oasis and realize that it must actually be real for he too sees the oasis\n"
    )
    del_print(
        "But as you both run into each other, you realize that there's only enough water for one person's journey\nYou immediately draw your gun and notice that he's doing it too\nIt's a standoff...\n"
    )
    import random

    if random.random() <= p1.gun:
        del_print("Your bullet pierces the man before he is able to pull the trigger\n")
        if p1.bottle:
            del_print(
                "Fortunately, you remember the bottle you had initially carried along. You fill enough water with the bottle to last for the rest of your journey\n"
            )
            del_print(
                "After few days of travel, you finally see civilization\nYou rest in the nearby town for a few days, recovering your health, and finally travel towards the coast\n"
            )
            del_print(
                "Months since you initially left your hometown, you finally reach your dream destination\nYou have reached just in time to witness a triumphant sunrise from the coast of Los Angeles\nYOU HAVE WON\n"
            )
        else:
            del_print(
                "You reach out for your bottle only to realize that you never carried one\nYou drink as much water as you can from the oasis and carry on with the journey\n"
            )
            del_print(
                "But after a few days of travel, the thirst returns but it is all the more severe this time\nYou start to get dizzy more often and the guilt of killing a man for nothing comes back to haunt you every now and then\n"
            )
            del_print("One midday, under the burning heat, your collapse and die.")
    else:
        del_print(
            "Unfortunately, you miss your shot and end up getting shot. You die a slow painful death as you start to bleed profusely in the middle of nowhere.\n"
        )


def fight1(p1):
    del_print(
        "You walk across the desert for weeks surviving on minimal food and water\nThe days have all rolled into one as you have focused all your brain power into being weary of the surroundings\n"
    )
    del_print(
        "Atlast, you see a man\nPerhaps he has some food\nYou look excitedly to see if he holds water for you... only to notice that he has a gun pointed at you\n"
    )
    del_print(f"You can choose to: 1)Fight or 2)Flight\n")
    while True:
        try:
            choice = int(input("Enter (1/2): "))
        except:
            print("Enter valid input")
        else:
            if choice == 2:
                p1.hp -= 50
                print(
                    f"You have {p1.hp} health points left after losing 50hp trying to run away and getting shot"
                )
                if p1.hp == 0:
                    del_print(
                        "Since you have 0 health points, you are not able to move forward. You eventually get stuck in the desert and die of malnourishment\n"
                    )
                    break
                else:
                    fight2(p1)
                    break
            elif choice == 1:
                import random

                if random.random() <= p1.gun:
                    del_print("You shoot the man\n")
                    fight2(p1)
                    break
                else:
                    del_print(
                        "Unfortunately, you miss your shot and end up getting shot. You die a slow painful death as you start to bleed profusely in the middle of nowhere.\n"
                    )
                    break
            else:
                print("Enter valid input")


def tribe(p1):
    del_print(
        "You walk for days and nights through the roads, not facing much trouble\nAs you brace yourself for crossing the vast Mojave Desert, you see a tribe of 10 nomads ahead of you\n"
    )
    if p1.likeability > 0:
        del_print(
            f"The elder one approaches you and appreciates you for having likeability {p1.likeability}. The tribe blesses you for your journey ahead\n"
        )
        fight1(p1)
    elif p1.likeability == 0:
        del_print(
            f"The tribe lets you pass through the desert, although they advice you to do more good deeds in life\n"
        )
        fight1(p1)
    else:
        del_print(
            "One of the members approaches you and says:\n'Since you disrespected our tribe's elder woman in your journey, we have decided not to let you through'\n"
        )
        del_print("You can now choose to:\n1)Give Up\n2)Fight against all 10 members\n")
        while True:
            try:
                choice = int(input("Enter (1/2): "))
            except:
                print("Enter valid input")
            else:
                if choice == 1:
                    del_print(
                        "As you stand there dejected, the tribe offers you to adopt you under their tutelage\nYou now spend the rest of your life as one of them, fending off the desert from future travellers\n"
                    )
                    break
                elif choice == 2:
                    import random, time

                    men_hit = 0
                    for men in range(10):
                        time.sleep(1)
                        if random.random() <= p1.gun:
                            print(f"You hit person {men + 1}!")
                            men_hit += 1
                        else:
                            print(f"You missed person {men + 1}.")

                    if men_hit == 10:
                        del_print(
                            "By some miracle, you have managed to fend off the entire tribe. Fate has chosen you indeed\n"
                        )
                        fight1(p1)
                    else:
                        del_print(
                            "Well, it wasn't a fair fight but you gave it your best shot. Your body now rots in the sands, as a gruelly reminder for travellers to come\n"
                        )
                    break
                else:
                    print("Enter valid input")


def library(p1):
    from wordle import wordle

    del_print(
        "You walk past this road and find yourself in a very beautiful and peaceful town\nThere appears to be some sort of a wordle competition in the library and you walk in there\n"
    )
    result = wordle()
    if result:
        p1.money += 50
        print(f"You have {p1.money}$ after winning 50$")
        del_print("You bid farewell to the town")
        gunstore(p1)
        tribe(p1)
    else:
        del_print(
            "Having lost an easy game, you sit dejected in the library\nBut a girl, who had seen you fail, sits next to you and consoles you\n"
        )
        del_print(
            "You have no option but to listen to her for she is not leaving you to lament your abject failure alone\nHowever, you do find eventually find her interesting and find comfort in talking to her\n"
        )
        del_print(
            "As hours go by, you realize that more beautiful than the sunrise at the L.A. Coast, her smile is\nYou decide to stay back and live with her here for the rest of your life."
        )


def carnival(p1):
    from minesweeper import mingame
    from shooting_bottles import shooting_game

    result = False
    del_print(
        "You see some festive activities in a carnival. Although you are not willing to participate in it, the locals force you into one of the carnival games in order to let you pass through their town\n"
    )
    del_print("You can choose between:\n")
    del_print(
        "1) Shooting Game: You will have to shoot 3 bottles consecutively with a gun (Only playable if you already possess a gun)\n"
    )
    del_print("2) Minesweeper\n")
    if p1.gun == 0:
        result = mingame()
    else:
        while True:
            try:
                choice = int(input("Enter (1/2): "))
            except:
                print("Enter valid input")
            else:
                if choice == 1:
                    result = shooting_game(p1)
                    break
                elif choice == 2:
                    result = mingame()
                    break
                else:
                    print("Enter valid input")
    if result:
        del_print(
            "The folks here are impressed by your skill at the game and have decided to gift you with a coveted shotgun having an accuracy of 90pc\n"
        )
        p1.gun = 0.9
        tribe(p1)
    else:
        del_print(
            "Since you lost the game, the folks at the carnival have decided that you're not worthy of crossing their town\nYou are made to work at the carnival for the rest of your life\n"
        )


def corpse(p1):
    del_print(
        "As you start walking, you notice a dead old woman lying in the middle of the road with 100$ of money on her torso. Choose:\n1)If you want to rob her\n2)If you want to walk past\n"
    )
    while True:
        try:
            choice = int(input("Enter (1/2): "))
        except:
            print("Enter valid input")
        else:
            if choice == 1:
                p1.money += 100
                p1.likeability -= 1
                del_print("You walk past hoping no one noticed that\n")
                print(f"You have {p1.money}$")
                break
            elif choice == 2:
                p1.likeability += 1
                break
            else:
                print("Enter valid input")
    carnival(p1)


def junction(p1):
    del_print(
        "As you leave the gunstore, the paths diverge into two ahead of you\nThere is a checkpost at the first path which strictly prohibits firearms while the second path has no such restriction\n"
    )
    if p1.gun == 0:
        while True:
            try:
                choice = int(
                    input("Enter your number(1/2) to choose the respective path: ")
                )
            except:
                print("Enter valid input")
            else:
                if choice == 1:
                    library(p1)
                    break
                elif choice == 2:
                    corpse(p1)
                    break
                else:
                    print("Enter valid input")
    else:
        corpse(p1)


def gunstore(p1):
    del_print(
        "You spot a gunstore from afar and decide to enter\nThere are three guns in display:\n1)Pistol(60pc accuracy): 50$\n2)Revolver(70pc accuracy): 100$\n3)Rifle(80pc accuracy): 150$\n4)To exit the gunstore\n"
    )
    del_print("Make sure you have enough money for buying the gun\n")
    print(f"You have {p1.money}$")
    COST_MENU = [50, 100, 150]
    GUN_MENU = [0.6, 0.7, 0.8]
    while True:
        try:
            input_num = int(input("Enter 1/2/3/4: "))
        except:
            print("Invalid input")
        else:
            if input_num == 4:
                del_print("You choose not to buy anything and leave\n")
                break
            elif input_num in [1, 2, 3]:
                if COST_MENU[input_num - 1] <= p1.money:
                    p1.gun = GUN_MENU[input_num - 1]
                    p1.money -= COST_MENU[input_num - 1]
                    print(
                        f"You have a gun with accuracy {p1.gun} and have {p1.money}$ left"
                    )
                    break
                else:
                    print("Not enough money")
            else:
                print("Invalid number")


def hangman(p1):
    from hangman import hang_game

    del_print(
        "Due to your failed robbery, the town council has decided to hang you.\n You must now play hangman in order to survive\n"
    )
    result, hp_lost = hang_game()
    if result == "win":
        del_print(
            f"Phew, that was a close encounter with death\nYou have lost {hp_lost} health points due to your number of guesses taken\n"
        )
        p1.hp -= hp_lost
        print(f"You have {p1.hp} health points left")
        p1.money = 0
        print(f"You have {p1.money}$")
        gunstore(p1)
        junction(p1)
    if result == "lose":
        del_print(
            "The townsfolk all applaud at the death of a criminal as your lifeless body hangs for public entertainment."
        )


def robbing(p1):
    from robbing import robbery

    del_print(
        "You must collect atleast 10 bundles of money (each represented by a dot) before 30 seconds.\nYou can use w/a/s/d for moving your player. Your time starts... now\n"
    )
    result = robbery()
    if result:
        del_print(
            "You have succesfully robbed the place and paid off your debt to the dealer\n"
        )
        p1.money = 0
        print(f"You have {p1.money}$")
        gunstore(p1)
        junction(p1)
    else:
        hangman(p1)


def blackjack(p1):
    from blackjack import bj_game

    del_print(
        "As you walk across the road, a funny-looking man unravels a pack of cards in front of you\nYou are going to play blackjack\n"
    )
    del_print(
        "1)The goal is to maximize the value of your hand but keep it <= 21\n2)Initially you are dealt two cards and the dealer draws one card\n"
    )
    del_print(
        "3)In each turn, each player can (hit/stand) till they (stand) or go over 21\n4)After the player's turn is over, the dealer tries to beat the user's score in the same way, higher score wins or if either goes over 21 they bust(lose)\n"
    )
    result = bj_game()
    if result == "win":
        p1.money += 100
    elif result == "lose":
        p1.money -= 150
    print(f"You have {p1.money}$")
    if p1.money < 0:
        del_print(
            "Since you owe money to the blackjack dealer, you must attempt a robbery to settle up\n"
        )
        robbing(p1)
    else:
        gunstore(p1)
        junction(p1)


def shady(p1):
    from maze import maze

    p1.bottle = True
    del_print(
        "You find an empty bottle on the ground and pick it up for you have a long journey ahead\n"
    )
    del_print(
        "As you traverse the forest, you realize that you've trapped yourself into a maze.\nThere are only 30 seconds until sunset. E represents exit. Reach the exit before sunset\n"
    )
    del_print(
        "Input the keys: w,a,s,d for travelling through the maze. Your time starts... now\n"
    )
    result = maze()
    if result:
        del_print(
            f"Well done, {p1.name} You have explored your way out of the maze of wilderness and see yourself at a paved road\n"
        )
        blackjack(p1)
    else:
        del_print(
            "You are stuck in the maze although the sun has set. As the hours pass by, you get more and more insane in the darkness for you're lost both mentally and physically\nYou die out of agony and exhaustion\n"
        )

#To remove user inputs that have the letters h, e, l and o to make the game challenging
def checksval(string):
    global counter
    counter = 0

    for char in ["h", "e", "l", "o"]:
        if char in string:
            counter += 1
    if counter == 4:
        print(counter)
        print("Invalid input")
        return True
    else:
        return False


def bright(p1):
    del_print("You find 100$ on the ground. Looks like it's your lucky day\n")
    p1.money += 100
    print(f"You have {p1.money}$")
    del_print(
        "You pass through an old lady who speaks in a foreign tongue.\nYou can enter two words of your choice and she will reply with the translated version of those words\n"
    )
    del_print(
        "The third word you enter must be 'hello' in her language. You shall do this in order to gain her respect\n"
    )
    #Randomly choosing the cipher
    cipher = random.randint(1, 25)
    STR = "abcdefghijklmnopqrstuvwxyz"
    trans_str = STR[cipher:] + STR[:cipher]
    for i in range(2):
        while True:
            in_word = (input(f"Enter word {i+1} to be translated: ")).lower()
            if in_word.isalpha():
                if checksval(in_word):
                    print("Cant use words with h,l,o and e")

                else:
                    print("".join([trans_str[STR.index(char)] for char in in_word]))
                    break

            else:
                print("Enter a valid word consisting of alphabets")
    #Checking if the final answer is the required answer and gives outputs accordingly
    while True:
        in_word = input(f"Enter 'hello' in her language: ")
        if in_word.isalpha():
            if in_word.lower() == "".join(
                [trans_str[STR.index(char)] for char in "hello"]
            ):
                del_print("Well played! You earned 100$ and her respect\n")
                p1.money += 100
                print(f"You have {p1.money}$")
                p1.likeability += 1
                print(f"You have {p1.likeability} unit(s) of likeability")
            else:
                del_print(
                    "Well, that wasn't the expected reply and she looks pissed off now\nShe mutters something unintelligible but it is clear that she is angry at you\n"
                )
                p1.likeability -= 1
                print(f"You have {p1.likeability} unit(s) of likeability")
            break
        else:
            print("Enter a valid word consisting of alphabets")
    blackjack(p1)
