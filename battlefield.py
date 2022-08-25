from robot import Robot
from dinosaur import Dinosaur


class Battlefield:
    def __init__(self):
        self.robot = Robot('Optimus Prime')
        self.dinosaur = Dinosaur('Godzilla', 30)

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print('\nWelcome to ROBOT vs. DINOSAUR!')
        print(
            f'This epic showdown is between {self.robot.name} and {self.dinosaur.name}.')

    def battle_phase(self):
        continue_battle = True

        while continue_battle:
            if self.dinosaur.health > 0:
                self.dinosaur.attack(self.robot)

            if self.robot.health > 0:
                self.robot.attack(self.dinosaur)

            if self.robot.health <= 0 or self.dinosaur.health <= 0:
                continue_battle = False

    def display_winner(self):
        if self.robot.health == 0:
            winner = self.dinosaur.name
        elif self.dinosaur.health == 0:
            winner = self.robot.name

        print(f'\nWinner! {winner} is the last one standing.')
