# HW1
# Name: Omar Alaa
# ID: 120180022

from typing import List
import Singleton as sg  # Implement a design pattern in the game
import random as rn  # essential to randomize choices, I could use linear congruential function but random module is very convenient
from prettytable import PrettyTable as pt  # To print the final outcome in a neat way
import numpy as np  # To use ceil function to find a winner where a player outperform another where the other could not compensate that loss in the remaining rounds
class Rock_paper_scissors(sg.Singleton):  # Inherits from a singleton class
    def __init__(self, rounds):
        x, com_rounds, human_rounds, ties, flag = pt(), 0, 0, 0, False  # My field variables
        x.field_names = ["Round number", "You played", "COM played", "Wins", "COM wins", "Ties"]  # Yhe header for my table
        self.flag, self.x, self.rounds, self.com_rounds, self.human_rounds, self.ties = flag, x, rounds, com_rounds, human_rounds, ties

    def Play(self):
        l: List[str] = ["Rock", "Paper", "Scissor"]  # All possible options
        for i in range(self.rounds):
            if self.flag: break  # Some flag to exit the game when it is already decided
            com_choice = rn.choice(l)  # a random choice of list l
            x = int(input('Type 1 for Rock, 2 for Paper, 3 for Scissor:\n'))
            assert 3>=x>=1,'Wrong Input' and self.Play()
            if l[x - 1] == l[0] and com_choice == l[1] or l[x - 1] == l[1] and com_choice == l[2] or l[x - 1] == l[2] and com_choice == l[0]:
                # All possible cases where the computer can win in order: (Paper,Rock)(Scissor,Paper)(Rock,Scissor)
                self.com_rounds += 1  # How many did the computer win out of total rounds?
                print("You played {} and COM played {}".format(l[x - 1], com_choice))  # Some feed in the game to inform the player where he stands
            elif l[x - 1] == l[0] and com_choice == l[2] or l[x - 1] == l[1] and com_choice == l[0] or l[x - 1] == l[2] and com_choice == l[1]:
                # All possible cases where the player can win in order: (Rock,Scissor)(Paper,Rock)(Scissor,Paper)
                self.human_rounds += 1
                print("You played {} and COM played {}".format(l[x - 1], com_choice))
            elif l[x - 1] == com_choice:
                # Identical choices indicate a tie
                self.ties += 1
                print("Tie")
            print(self.Result(i))
            self.Report(l[x - 1], com_choice, i + 1) #

    def COM_wins(self):  # Return number of COM wins
        return self.com_rounds

    def My_wins(self):  # Return number of my wins
        return self.human_rounds

    def Rounds(self):  # Return number of rounds
        return self.rounds

    def Choices(self, round_no):  # Return choices in a specific round
        return self.x[round_no - 1]

    def Final_Report(self):  # Return final report
        return self.x

    def Result(self, i):  # What lies below is an algorithm to quit the game as early as it has been decided
        if self.com_rounds > np.ceil((self.rounds - self.ties) // 2) or self.human_rounds > np.ceil((self.rounds - self.ties) // 2):  self.flag = True
        return "for {} rounds, you won {} and the computer won {}, with {} ties".format(i + 1, self.human_rounds,self.com_rounds, self.ties)

    def Report(self, x=str, y=str, i=int):  # Adds to the table of outcomes
        self.x.add_row(["{}".format(i), "{}".format(x), "{}".format(y), "{}".format(self.human_rounds),"{}".format(self.com_rounds), "{}".format(self.ties)])

    def Winner(self):  # Return the winner out of all rounds
        if self.com_rounds == 0 and self.human_rounds == 0 and self.ties == 0:
            return "You have not played yet to declare a winner"
        elif self.com_rounds > self.human_rounds:
            return "COM wins, good luck next time!"
        elif self.com_rounds < self.human_rounds:
            return "You win!!!"
        else:
            return "Tie, what a coincidence!"
a = Rock_paper_scissors(int(input('How many rounds?\n')))  # create the instance
a.Play()  # begin the game
print(a.Winner())  # return the winner
print(a.Final_Report())  # return a table documenting the progress of the game
print(a.Choices(2))  # return the choices in round number 2
# b=Rock_paper_scissors(int(input('How many rounds?\n')))
