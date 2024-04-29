def bj_game():
    import random

    def initialize_deck():
        # Initialize a deck of cards
        SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
        RANKS = [
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "Jack",
            "Queen",
            "King",
            "Ace",
        ]
        deck = [{"rank": rank, "suit": suit} for suit in SUITS for rank in RANKS]
        random.shuffle(deck)
        return deck

    def calculate_score(hand):
        # Calculate the score of a hand
        score = 0
        num_aces = 0
        for card in hand:
            if card["rank"] in ["Jack", "Queen", "King"]:
                score += 10
            elif card["rank"] == "Ace":
                score += 11
                num_aces += 1
            else:
                score += int(card["rank"])

        # Adjust the score for Aces
        while score > 21 and num_aces:
            score -= 10
            num_aces -= 1

        return score

    def print_hand(hand):
        # Print the cards in a hand
        for card in hand:
            print(f"{card['rank']} of {card['suit']}")

    def blackjack_game():
        print("Welcome to Blackjack!")

        # Initialize deck and hands
        deck = initialize_deck()
        player_hand = [deck.pop(), deck.pop()]
        dealer_hand = [deck.pop(), deck.pop()]

        # Print initial hands
        print("Your hand:")
        print_hand(player_hand)
        print("Dealer's hand:")
        print(dealer_hand[0]["rank"], "of", dealer_hand[0]["suit"])
        print("--------------")

        # Player's turn
        while True:
            player_score = calculate_score(player_hand)
            if player_score == 21:
                print("Blackjack! You win!")
                return "win"
            elif player_score > 21:
                print("Bust! You lose!")
                return "lose"

            action = input("Do you want to hit or stand? (h/s): ").lower()
            if action == "h":
                player_hand.append(deck.pop())
                print("Your hand:")
                print_hand(player_hand)
            elif action == "s":
                break

        # Dealer's turn
        print("Dealer's hand:")
        print_hand(dealer_hand)
        while calculate_score(dealer_hand) < 17:
            dealer_hand.append(deck.pop())
            print("Dealer hits.")
            print_hand(dealer_hand)

        dealer_score = calculate_score(dealer_hand)
        if dealer_score > 21 or dealer_score < player_score:
            print("You win!")
            return "win"
        elif dealer_score > player_score:
            print("Dealer wins!")
            return "lose"
        else:
            print("It's a tie!")
            return "tie"

    result = blackjack_game()
    return result
