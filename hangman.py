import random


def hang_game(
    WORDS=[
        "aridly",
        "mirage",
        "canyon",
        "sunset",
        "tumble",
        "sahara",
        "pistol",
        "gritty",
    ]
):
    #Initializing
    word_to_guess = random.choice(WORDS).lower()
    guessed_letters = set()
    tries = 6

    #Checking conditions
    while tries > 0:
        # Display current state of the word with underscores for unguessed letters
        display_word = "".join(
            letter if letter in guessed_letters else "_" for letter in word_to_guess
        )
        print("Word to guess:", display_word)

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
        else:
            guessed_letters.add(guess)
            if guess in word_to_guess:
                print("Good guess!")
            else:
                print("Wrong guess!")
                tries -= 1

        #Winning condition
        if set(word_to_guess) <= guessed_letters:
            print("Congratulations! You guessed the word:", word_to_guess)
            return "win", 50 - tries * 10

        print("Tries left:", tries)

    print("Sorry, you ran out of tries. The word was:", word_to_guess)
    return "lose", 100
