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
new_deck_of_cards = (
    "2 of Hearts", "3 of Hearts", "4 of Hearts", "5 of Hearts", "6 of Hearts", "7 of Hearts", "8 of Hearts", "9 of Hearts", "10 of Hearts", "Jack of Hearts", "Queen of Hearts", "King of Hearts", "Ace of Hearts",
    "2 of Clubs", "3 of Clubs", "4 of Clubs", "5 of Clubs", "6 of Clubs", "7 of Clubs", "8 of Clubs", "9 of Clubs", "10 of Clubs", "Jack of Clubs", "Queen of Clubs", "King of Clubs", "Ace of Clubs",
    "2 of Diamonds", "3 of Diamonds", "4 of Diamonds", "5 of Diamonds", "6 of Diamonds", "7 of Diamonds", "8 of Diamonds", "9 of Diamonds", "10 of Diamonds", "Jack of Diamonds", "Queen of Diamonds", "King of Diamonds", "Ace of Diamonds",
    "2 of Spades", "3 of Spades", "4 of Spades", "5 of Spades", "6 of Spades", "7 of Spades", "8 of Spades", "9 of Spades", "10 of Spades", "Jack of Spades", "Queen of Spades", "King of Spades", "Ace of Spades",
    "JOKER"
)

# This is the deck which will be dealt from. Each time a card is dealt it is removed (pop) from the deck.
working_deck = list(new_deck_of_cards)

# This function (deal) returns one randomly chosen card from working_deck. The chosen card is then removed from working_deck (so it cannot be chosen again).
def deal():
    return working_deck.pop(random.randint(0, len(working_deck)-1))

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

player_1.name = input(">>> ")
if player_1.name == "":
    player_1.name = "Player 1"
# User is prompted to type their name.
print("\nHi {}!  I'm going to deal you a card and all you have to do is guess whether the next card dealt will be 'Higher or Lower'.".format(player_1.name.title()))
print("The highest value card is an ACE and the lowest value card is a TWO.")
print("Everytime you guess correctly your skill level score will increase by one point!")
print("However, an incorrect guess will deduct a point from your score!")
print("You can choose whether to play with a JOKER in the deck or not...")
print("If you choose to AND you draw a JOKER card your score will reset at ZERO and the game is over!!!")
print("The game is won when you reach skill level 10, or lost when your skill level reaches zero - OR you run out of cards!\n")
print("If you're ready to start press ENTER now!")
input(">>> ")
print("\nWould you like to play with a JOKER card?")
print("Type 'Y' or 'N' and press ENTER")
joker_present = input(">>> ")
joker_present = joker_present.upper()
while joker_present != "YES" and joker_present != "NO":
    if "Y" in joker_present:
        joker_present = "YES"
    elif "N" in joker_present:
        joker_present = "NO"
    else:
        print("Oops! Input not recognised. Try typing either 'Y' or 'N'")
        joker_present = input(">>> ")
        joker_present = joker_present.upper()
if joker_present == "NO":
    working_deck.remove("JOKER")
    print("You have chosen to play with the JOKER card removed...")
    print("CHICKEN!")
else:
    print("You have chosen to play with the JOKER card included...")
    print("You are very brave!")

# This is the main gameplay loop. The game continues until the player wins or loses.
continue_game = True
first_card = deal()
while continue_game == True:
    first_card_value = get_value(first_card)
    print("")
    print("Your current skill level score is {}.".format(player_1.skill_level))
    if len(working_deck) == 1:
        print("There is only one card left in the deck!")
    else:
        print("There are {} cards remaining in the deck.".format(len(working_deck) + 1))
    print("\nThe current card is {}".format(first_card))
    print("Will the next card be 'higher or lower'?")
    print("Type 'H' or 'L' and press ENTER")
    guess = input(">>> ")
    guess = guess.upper()
    while guess != "HIGHER" and guess != "LOWER":
        if "H" in guess:
            guess = "HIGHER"
        elif "L" in guess:
            guess = "LOWER"
        else:
            print("Oops! Input not recognised. Try typing either 'H' or 'L'")
            guess = input(">>> ")
            guess = guess.upper()
    print("\nYou guessed {}...".format(guess))
    second_card = deal()
    second_card_value = get_value(second_card)
    result = ""
    if second_card == "JOKER":
        print("Oh no! You've been dealt a JOKER! - Score reset to zero!")
        print("GAME OVER! Better luck next time")
        player_1.skill_level = 0
        player_1.has_played += 1
        player_1.has_lost += 1
        print("\nWould you like to play again?")
        print("Type 'Y' or 'N' and press ENTER")
        y_or_n = input(">>> ")
        y_or_n = y_or_n.upper()
        while y_or_n != "YES" and y_or_n != "NO":
            if "Y" in y_or_n:
                y_or_n = "YES"
            elif "N" in y_or_n:
                y_or_n = "NO"
            else:
                print("Oops! Input not recognised. Try typing either 'Y' or 'N'")
                y_or_n = input(">>> ")
                y_or_n = y_or_n.upper()
        if y_or_n == "YES":
            player_1.skill_level = 1
            player_1.has_played = 0
            working_deck = list(new_deck_of_cards)
            print("\nWould you like to play with a JOKER card?")
            print("Type 'Y' or 'N' and press ENTER")
            joker_present = input(">>> ")
            joker_present = joker_present.upper()
            while joker_present != "Yes" and joker_present != "NO":
                if "Y" in joker_present:
                    joker_present = "YES"
                elif "N" in joker_present:
                    joker_present = "NO"
                else:
                    print("Oops! Input not recognised. Try typing either 'Y' or 'N'")
                    joker_present = input(">>> ")
                    joker_present = joker_present.upper()
            if joker_present == "NO":
                working_deck.remove("JOKER")
                print("You have chosen to play with the JOKER card removed...")
                print("CHICKEN!")
            else:
                print("You have chosen to play with the JOKER card included...")
                print("You are very brave!")
        elif y_or_n == "NO":
            continue_game = False
    elif second_card != "JOKER":
        if first_card_value == second_card_value:
            result = "SAME VALUE"
        elif first_card_value > second_card_value:
            result = "LOWER"
        elif first_card_value < second_card_value:
            result = "HIGHER"
        print("The card dealt is {}...".format(second_card))
        if result == "SAME VALUE":
            print("Both cards are of same value - No score!")
        elif result == guess:
            print("You guessed correctly - One point scored!")
            player_1.skill_level += 1
            player_1.has_won += 1
        else:
            print("Bad luck, you guessed incorrectly - One point deducted!")
            player_1.skill_level -= 1
            player_1.has_lost += 1
        player_1.has_played += 1
        if player_1.skill_level > 0 and player_1.skill_level < 10:
            if len(working_deck) == 0:
                print("Uh oh! You've run out of cards!")
                print("GAME OVER! Better luck next time")
                print("\nWould you like to play again?")
                print("Type 'Y' or 'N' and press ENTER")
                y_or_n = input(">>> ")
                y_or_n = y_or_n.upper()
                while y_or_n != "YES" and y_or_n != "NO":
                    if "Y" in y_or_n:
                        y_or_n = "YES"
                    elif "N" in y_or_n:
                        y_or_n = "NO"
                    else:
                        print("Oops! Input not recognised. Try typing either 'Y' or 'N'")
                        y_or_n = input(">>> ")
                        y_or_n = y_or_n.upper()
                if y_or_n == "YES":
                    player_1.skill_level = 1
                    player_1.has_played = 0
                    working_deck = list(new_deck_of_cards)
                    print("\nWould you like to play with a JOKER card?")
                    print("Type 'Y' or 'N' and press ENTER")
                    joker_present = input(">>> ")
                    joker_present = joker_present.upper()
                    while joker_present != "Yes" and joker_present != "NO":
                        if "Y" in joker_present:
                            joker_present = "YES"
                        elif "N" in joker_present:
                            joker_present = "NO"
                        else:
                            print("Oops! Input not recognised. Try typing either 'Y' or 'N'")
                            joker_present = input(">>> ")
                            joker_present = joker_present.upper()
                    if joker_present == "NO":
                        working_deck.remove("JOKER")
                        print("You have chosen to play with the JOKER card removed...")
                        print("CHICKEN!")
                    else:
                        print("You have chosen to play with the JOKER card included...")
                        print("You are very brave!")
                elif y_or_n == "NO":
                    continue_game = False
            first_card = second_card
            print("\nReady to play round {}? Press ENTER".format(player_1.has_played + 1))
            input(">>> ")
        elif player_1.skill_level == 0:
            print("\nGAME OVER! Better luck next time")
            print("\nWould you like to play again?")
            print("Type 'Y' or 'N' and press ENTER")
            y_or_n = input(">>> ")
            y_or_n = y_or_n.upper()
            while y_or_n != "YES" and y_or_n != "NO":
                if "Y" in y_or_n:
                    y_or_n = "YES"
                elif "N" in y_or_n:
                    y_or_n = "NO"
                else:
                    print("Oops! Input not recognised. Try typing either 'Y' or 'N'")
                    y_or_n = input(">>> ")
                    y_or_n = y_or_n.upper()
            if y_or_n == "YES":
                player_1.skill_level = 1
                player_1.has_played = 0
                working_deck = list(new_deck_of_cards)
                print("\nWould you like to play with a JOKER card?")
                print("Type 'Y' or 'N' and press ENTER")
                joker_present = input(">>> ")
                joker_present = joker_present.upper()
                while joker_present != "YES" and joker_present != "NO":
                    if "Y" in joker_present:
                        joker_present = "YES"
                    elif "N" in joker_present:
                        joker_present = "NO"
                    else:
                        print("Oops! Input not recognised. Try typing either 'Y' or 'N'")
                        joker_present = input(">>> ")
                        joker_present = joker_present.upper()
                if joker_present == "NO":
                    working_deck.remove("JOKER")
                    print("You have chosen to play with the JOKER card removed...")
                    print("CHICKEN!")
                    first_card = deal()
                else:
                    print("You have chosen to play with the JOKER card included...")
                    print("You are very brave!")
                    first_card = deal()
            elif y_or_n == "NO":
                continue_game = False
        elif player_1.skill_level == 10:
            print("\nCONGRATULATIONS! You have scored 10 points! You win!")
            print("\nWould you like to play again?")
            print("Type 'Y' or 'N' and press ENTER")
            y_or_n = input(">>> ")
            y_or_n = y_or_n.upper()
            while y_or_n != "YES" and y_or_n != "NO":
                if "Y" in y_or_n:
                    y_or_n = "YES"
                elif "N" in y_or_n:
                    y_or_n = "NO"
                else:
                    print("Oops! Input not recognised. Try typing either 'Y' or 'N'")
                    y_or_n = input(">>> ")
                    y_or_n = y_or_n.upper()
            if y_or_n == "YES":
                player_1.skill_level = 1
                player_1.has_played = 0
                working_deck = list(new_deck_of_cards)
                print("\nWould you like to play with a JOKER card?")
                print("Type 'Y' or 'N' and press ENTER")
                joker_present = input(">>> ")
                joker_present = joker_present.upper()
                while joker_present != "Yes" and joker_present != "NO":
                    if "Y" in joker_present:
                        joker_present = "YES"
                    elif "N" in joker_present:
                        joker_present = "NO"
                    else:
                        print("Oops! Input not recognised. Try typing either 'Y' or 'N'")
                        joker_present = input(">>> ")
                        joker_present = joker_present.upper()
                if joker_present == "NO":
                    working_deck.remove("JOKER")
                    print("You have chosen to play with the JOKER card removed...")
                    print("CHICKEN!")
                    first_card = deal()
                else:
                    print("You have chosen to play with the JOKER card included...")
                    print("You are very brave!")
                    first_card = deal()
            elif y_or_n == "NO":
                continue_game = False

print("\nThank you for playing {}.".format(player_1.name.title()))
print("See you again soon!\n")

# END OF CODE
