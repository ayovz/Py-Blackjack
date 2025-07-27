import os
import random

# Game title ASCII art
ascii_art = """
.------..------..------..------..------..------..------..------..------.
|B.--. ||L.--. ||A.--. ||C.--. ||K.--. ||J.--. ||A.--. ||C.--. ||K.--. |
| :(): || :/\: || (\/) || :/\: || :/\: || :(): || (\/) || :/\: || :/\: |
| ()() || (__) || :\/: || :\/: || :\/: || ()() || :\/: || :\/: || :\/: |
| '--'B|| '--'L|| '--'A|| '--'C|| '--'K|| '--'J|| '--'A|| '--'C|| '--'K|
`------'`------'`------'`------'`------'`------'`------'`------'`------'
"""


# Clear terminal screen (Windows/Linux/Mac)
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Deal one card
def deal_card():
    return random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11])


# Calculate score from card list
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


# Compare final scores
def compare_scores(user_score, computer_score):
    if user_score == computer_score:
        return "DRAW"
    elif computer_score == 0:
        return "LOSS, Opponent has Blackjack!"
    elif user_score == 0:
        return "WIN, You have Blackjack!"
    elif user_score > 21:
        return "LOSS, You went over!"
    elif computer_score > 21:
        return "WIN, Computer went over!"
    elif user_score > computer_score:
        return "WIN, You beat the computer!"
    else:
        return "LOSS, Computer wins!"


# Ask to play again
def ask_replay():
    while True:
        choice = input("Would you like to play again? (y/n): ").lower()
        if choice == 'y':
            clear_screen()
            return True
        elif choice == 'n':
            print("Thanks for playing Blackjack! 👋")
            return False
        else:
            print("Please enter 'y' or 'n'.")


# Main game loop
def play_game():
    clear_screen()
    print(ascii_art)

    user_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]
    game_over = False

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"\nYour cards: {user_cards}, current score: {user_score}")
        if user_score > 21:
            print(f"Computer's cards: {computer_cards}, score: {computer_score}")
        else:
            print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_choice = input("Type 'y' to draw another card, or 'n' to stand: ").lower()
            if user_choice == 'y':
                user_cards.append(deal_card())
            elif user_choice == 'n':
                game_over = True
            else:
                print("Invalid input. Please type 'y' or 'n'.")

    # Computer's turn
    while calculate_score(computer_cards) < 17 and computer_score != 0:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print("\n--------------- Final Results ---------------")
    print(f"Your cards: {user_cards}, final score: {user_score}")
    print(f"Computer's cards: {computer_cards}, final score: {computer_score}")
    print(compare_scores(user_score, computer_score))
    print("---------------------------------------------\n")


# Entry point
print("🎉 Welcome to Blackjack! 🎉")
input("Press Enter to start the game...")
clear_screen()

# Replay loop
while True:
    play_game()
    if not ask_replay():
        break
