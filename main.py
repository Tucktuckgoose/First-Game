# The card game Munchkin
# Author: Wilson Tucker
# Date: 7 October 2016
# Python 3.5

import random

class Player(object):

    def __init__(self):
        # All players start as level 1 humans
        self.level = 1
        self.race = "Human"

    def set_name(self, name):
        # Set player name
        self.name = name

    def set_gender(self, gender):
        # Set player gender
        self.gender = gender

    def switch_gender(self):
        # Switch player gender from male to female and vice versa
        if self.gender == "Male":
            self.gender = "Female"
        elif self.gender == "Female":
            self.gender = "Male"
        else:
            print ("What are you?")

# Determine the number of players in this game
numPlayers = int(input("How many players in this game? "))

# Initialize all of the Player objects
players = [Player() for i in range(numPlayers)]

counter = 1
# Set the player's names and genders
for player in players:
    name = input("What is the Player " + str(counter) +"'s name? ")
    Player.set_name(player, name)
    gender = input("What is " + name + "'s gender? ")
    Player.set_gender(player, gender)
    print("Player Number " + str(counter) + " is a " + player.gender + " whose name is " + player.name + " and is a Level " + str(player.level) + " " + player.race + ".")
    counter += 1

# Determine who goes first
for counter in range(numPlayers):
    if counter == 0:
        highRoll = random.randint(1,6)
        firstPlayer = counter
        print(players[counter].name + " rolled a " + str(highRoll) + ", that is the score to beat.")
    else:
        roll = random.randint(1,6)
        if roll > highRoll:
            highRoll = roll
            firstPlayer = counter
            print(players[counter].name + " rolled a " + str(roll) + ", that is the new score to beat.")
        else:
            print(players[counter].name + " rolled a " + str(roll) + ", that is not high enough.")

print("The first player to go is " + players[firstPlayer].name + " with a roll of " + str(highRoll) +".")





