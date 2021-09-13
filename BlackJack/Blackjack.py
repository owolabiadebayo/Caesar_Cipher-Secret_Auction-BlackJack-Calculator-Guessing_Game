# Capstone Project

import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

from os import system, name
# import sleep to show output for some time period
from time import sleep
# define our clear function

"""Returns a random card from the deck."""
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_scores, computer_scores):
    """Compares and returns outcome of 2 scores"""
    if user_scores > 21 and computer_scores > 21:
        return "You went over. You lose 😤"
    if user_scores == computer_scores:
        return "Draw 🙃"
    elif computer_scores == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_scores == 0:
        return "Win with a Blackjack 😎"
    elif user_scores > 21:
        return "You went over. You lose 😭"
    elif computer_scores > 21:
        return "Opponent went over. You win 😁"
    elif user_scores > computer_scores:
        return "You win 😃"
    else:
        return "You lose 😤"


user_cards = []
computer_cards = []
is_game_over = False

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

user_scores = calculate_score(user_cards)
computer_scores = calculate_score(computer_cards)

print(f"   Your cards: {user_cards}, current score: {user_scores}")
print(f"   Computer's first card: {computer_cards[0]}")

if user_scores == 0 or computer_scores == 0 or user_scores > 21:
    is_game_over = True
else:
    user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
if user_should_deal == "y":
    user_cards.append(deal_card())
else:
    is_game_over = True


while computer_scores != 0 and computer_scores < 17:
    computer_cards.append(deal_card())
    computer_scores = calculate_score(computer_cards)


    print(f"   Your final hand: {user_cards}, final score: {user_scores}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_scores}")
    print(compare(user_scores, computer_scores))
    
