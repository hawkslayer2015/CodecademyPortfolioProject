# 'Higher or Lower' - My First Codecademy Portfolio Project.
# A simple 'higher or lower' terminal based card game.
# A player is dealt a card and has to guess whether the following card will have a higher or lower value (ie. 10 of clubs is higher than 7 of diamonds).
# As the game progresses, the player's skill level will increase or decrease depending on the success of their guesses.
# ----------
import random

class Player:
    def __init__(self, name="Player 1"):
        self.name = name
        self.skill_level = 1
        self.has_played = 0
        self.has_won = 0
        self.has_lost = 0

    def __repr__(self):
        return """
        Player's name is '{a}'\n
        {a}'s current skill level is {b}\n
        {a} has played {c} games - Won {d} and lost {e}
        """.format(a=self.name, b=self.skill_level, c=self.has_played, d=self.has_won, e=self.has_lost)

# A list of all 52 suited cards + one JOKER card (53 cards total).
deck_of_cards = [
    "2 of Hearts", "3 of Hearts", "4 of Hearts", "5 of Hearts", "6 of Hearts", "7 of Hearts", "8 of Hearts", "9 of Hearts", "10 of Hearts", "Jack of Hearts", "Queen of Hearts", "King of Hearts", "Ace of Hearts",
    "2 of Clubs", "3 of Clubs", "4 of Clubs", "5 of Clubs", "6 of Clubs", "7 of Clubs", "8 of Clubs", "9 of Clubs", "10 of Clubs", "Jack of Clubs", "Queen of Clubs", "King of Clubs", "Ace of Clubs",
    "2 of Diamonds", "3 of Diamonds", "4 of Diamonds", "5 of Diamonds", "6 of Diamonds", "7 of Diamonds", "8 of Diamonds", "9 of Diamonds", "10 of Diamonds", "Jack of Diamonds", "Queen of Diamonds", "King of Diamonds", "Ace of Diamonds",
    "2 of Spades", "3 of Spades", "4 of Spades", "5 of Spades", "6 of Spades", "7 of Spades", "8 of Spades", "9 of Spades", "10 of Spades", "Jack of Spades", "Queen of Spades", "King of Spades", "Ace of Spades",
    "JOKER"
]

# This function (deal) returns one randomly chosen card from deck_of_cards. The chosen card is then removed from deck_of_cards (so it cannot be chosen again).
def deal():
    return deck_of_cards.pop(random.randint(0, len(deck_of_cards)-1))

# This function (get_value) takes a card name (str) and returns its value as an integer - ie. '5 of Clubs' = 5 and 'Jack of Hearts' = 11.
def get_value(card):
    card_value = 0
    if "2" in card:
        card_value = 2
    elif "3" in card:
        card_value = 3
    elif "4" in card:
        card_value = 4
    elif "5" in card:
        card_value = 5
    elif "6" in card:
        card_value = 6
    elif "7" in card:
        card_value = 7
    elif "8" in card:
        card_value = 8
    elif "9" in card:
        card_value = 9
    elif "10" in card:
        card_value = 10
    elif "Jack" in card:
        card_value = 11
    elif "Queen" in card:
        card_value = 12
    elif "King" in card:
        card_value = 13
    elif "Ace" in card:
        card_value = 14
    else:
        card_value = 0
    return card_value

game_counter = 0
current_card = ""
player_1 = Player()

# Gameplay starts here!
# Introduction...
print("""
------------------------------------------------------------------------------------------------------
00  00  00  000000  00  00  000000  000000    000000  000000    00      000000  0    0  000000  000000
00  00  00  00  00  00  00  00      00  00    00  00  00  00    00      00  00  0    0  00      00  00
00  00  00  00      00  00  00      00  00    00  00  00  00    00      00  00  0 00 0  00      00  00
000000  00  000000  000000  000000  000000    00  00  000000    00      00  00  0 00 0  000000  000000
00  00  00  00  00  00  00  00      00 00     00  00  00 00     00      00  00  0 00 0  00      00 00 
00  00  00  00  00  00  00  00      00  00    00  00  00  00    00      00  00  0 00 0  00      00  00
00  00  00  000000  00  00  000000  00  00    000000  00  00    000000  000000  000000  000000  00  00
------------------------------------------------------------------------------------------------------

                   Welcome to 'Higher or Lower'! A fun and simple game of chance

              If you are ready to play your first game, please enter your name below:
""")

player_1 = input(">>> ")
# User is prompted to type their name.
print("\nHi {}!  I'm going to deal you a card and all you have to do is guess whether the next card dealt will be 'Higher or Lower'".format(player_1.title()))
print("The highest value card is an ACE and the lowest value card is a TWO.")
print("Everytime you guess correctly your skill level score will increase by one point!")
print("However, an incorrect guess will deduct a point from your score!")
print("AND... if you draw a JOKER card your score will reset at ZERO!!!")
print("The game is won when you reach skill level 10, or lost when your skill level reaches zero.\n")
print("If you're ready to start press ENTER now!\n")
input(">>> ")

print("Game starts")