def wordle(lstwrds=["cacti", "dusty", "chaps", "rodeo", "oasis"]):
    import random

    #Returns a dictionary of each letter and its frequency
    def dicword(word):
        d = {}
        for letter in word:
            d[letter] = d.get(letter, 0) + 1
        return d

    word = random.choice(lstwrds)
    print("Welcome to Wordle!")
    guessedwords = []
    i = 1
    while i < 7:
        guess = ["⬛", "⬛", "⬛", "⬛", "⬛"]
        inwrd = str(input("Enter a five letter word: ")).lower()
        dicw = dicword(word)
        if len(inwrd) != 5:
            print("Only five letters words are allowed")
        else:
            #Using green boxes for letters in correct position and yellow if letter count is less than that in the word and is not in the right position
            if inwrd not in guessedwords:
                guessedwords += [inwrd]
                for j in range(5):
                    if inwrd[j] == word[j]:
                        guess[j] = "🟩"
                        dicw[inwrd[j]] -= 1
                for j in range(5):
                    if (inwrd[j] in word) and (guess[j] != "🟩") and dicw[inwrd[j]] > 0:
                        guess[j] = "🟨"
                        dicw[inwrd[j]] -= 1
                i += 1
            else:
                print("Already Guessed")
        print("".join(guess))
        #Breaking if word is guessed correctly
        if guess == ["🟩", "🟩", "🟩", "🟩", "🟩"]:
            break
    if guess == ["🟩", "🟩", "🟩", "🟩", "🟩"]:
        print("Congratulations")
        return True
    else:
        print("You were unfortunately not able to find the word")
        return False