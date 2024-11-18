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
        pass









