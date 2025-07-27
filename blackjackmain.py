import os
import random

ascii_art = """

.------..------..------..------..------..------..------..------..------.
|B.--. ||L.--. ||A.--. ||C.--. ||K.--. ||J.--. ||A.--. ||C.--. ||K.--. |
| :(): || :/\: || (\/) || :/\: || :/\: || :(): || (\/) || :/\: || :/\: |
| ()() || (__) || :\/: || :\/: || :\/: || ()() || :\/: || :\/: || :\/: |
| '--'B|| '--'L|| '--'A|| '--'C|| '--'K|| '--'J|| '--'A|| '--'C|| '--'K|
`------'`------'`------'`------'`------'`------'`------'`------'`------'

"""


def deal_card():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    card = random.choice(cards)
    return card


def calculate_score(card_list):
    if sum(card_list) == 21 and len(card_list) == 2:
        return 0
    elif 11 in card_list and sum(card_list) > 21:
        card_list.remove(11)
        card_list.append(1)
    return sum(card_list)


def compare(u_score, c_score):
    if u_score == c_score:
        return "DRAW"
    elif c_score == 0:
        return "LOSS, Opponent has Blackjack!"
    elif u_score == 0:
        return "WIN, Player has Blackjack!"
    elif u_score > 21:
        return "LOSS, You went Over!"
    elif c_score > 21:
        return "WIN, Computer went Over!"
    elif u_score > c_score:
        return "You WIN"
    else:
        return "You LOSE"


def game_status(choice):
    if choice == "Y" or choice == "y":
        os.system("cls")
        return True
    elif choice == "N" or choice == "n":
        print("Thanks for playing Blackjack!")
        return False
    else:
        os.system("cls")
        return False


replay = True

while replay:
    print(ascii_art)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    isGameOver = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not isGameOver:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f'Your cards: {user_cards}, current score: {user_score}')

        if user_score > 21:
            print(f"Computer's Cards: {computer_cards} Computer's score: {computer_score}")
        else:
            print(f'Computer\'s First Card: {computer_cards[0]}')

        if user_score == 0 or computer_score == 0 or user_score > 21:
            isGameOver = True
        else:
            user_deal = input("Type 'y' to get another card, type 'n' to stand: ")
            if user_deal == 'y':
                user_cards.append(deal_card())
            else:
                isGameOver = True

    while computer_cards != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # Final results
    print(f'Your cards: {user_cards}, current score: {user_score}')
    print(f"Computer's Cards: {computer_cards} Computer's score: {computer_score}")

    print(compare(user_score, computer_score) + "\n\n")

    # Ask user about replaying
    play_again = input("Would you like to play again? (y/n): ")

    replay = game_status(play_again)
