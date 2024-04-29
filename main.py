#import required files
from functions import shady, bright, del_print, Person

print(
    "Welcome to How Do You Rodeo?\nTo skip the text animation press the 's' key or else press any other key to continue"
)
while True:
    name = str(input("Enter your character's name: "))
    if name.isalpha():
        break
    else:
        print("Enter a valid name consisting of alphabets")


p1 = Person(name, 0, 100, 0, False, 0)

#Starting out
del_print(
    f"Welcome, {p1.name}. You have always wanted to see the sunrise at the coast of Los Angeles all your life.\nThe time has come, warrior. You must cross dangers and surprises plentifold in order to fulfill your dream."
)
print()
del_print(
    "Two roads diverged in a yellow wood,\nAnd sorry I could not travel both\nAnd be one traveler, long I stood\nAnd looked down one as far as I could\nTo where it bent in the undergrowth;"
)
print()
del_print(
    f"{p1.name}, fate seems to have given you the same conundrum Robert Frost once faced. You face two roads: One that looks well-lit and green while the other seems shady and barren\nThe choice is yours."
)

#Takes user input on which path to take initially and calls the path functions accordingly
while True:
    try:
        choice = int(
            input(
                "Enter your path number: 1 for the bright path and 2 for the shady path: "
            )
        )
    except:
        print("Enter valid input")
    else:
        if choice == 1:
            bright(p1)
            break
        elif choice == 2:
            shady(p1)
            break
        else:
            print("Enter valid input")

