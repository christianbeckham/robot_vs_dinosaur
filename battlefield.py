from fleet import Fleet
from herd import Herd
from random import randint


class Battlefield:
    def __init__(self):
        self.fleet = []
        self.herd = []

    def run_game(self):
        self.display_welcome()
        self.create_fleet(3)
        self.create_herd(3)
        self.battle_phase()

    def display_welcome(self):
        print('\nWelcome to ROBOT vs. DINOSAUR!')
        print(f'The epic showdown to end all epic showdowns.')

    def battle_phase(self):
        rounds = len(self.fleet) if len(self.fleet) == len(self.herd) else 0

        for round in range(1, rounds + 1):
            print('\nBATTLE ROUND', round)

            attack_sequence = self.attack_sequence()

            first_opponent = attack_sequence[0]
            second_opponent = attack_sequence[1]
            self.battle(first_opponent, second_opponent)

    def display_winner(self, winner):
        print(f"\nWinner! {winner.name} is the last one standing.")

    def create_fleet(self, fleet_count):
        new_fleet = Fleet()
        self.fleet += new_fleet.create_fleet(fleet_count)

    def create_herd(self, herd_count):
        new_herd = Herd()
        self.herd += new_herd.create_herd(herd_count)

    def battle(self, opponent_one, opponent_two):
        print(f'{opponent_one.name} vs. {opponent_two.name}')
        continue_battle = True

        while continue_battle:
            if opponent_one.health > 0:
                print(
                    f'\n{opponent_one.name} (HP: {opponent_one.health}) is attacking...')

                attack_level = self.generate_attack_power()
                opponent_one.attack(opponent_two, attack_level)

            if opponent_two.health > 0:
                print(
                    f'\n{opponent_two.name} (HP: {opponent_two.health}) is attacking...')

                attack_level = self.generate_attack_power()
                opponent_two.attack(opponent_one, attack_level)

            if opponent_two.health <= 0:
                continue_battle = False
                winner = opponent_one
            elif opponent_one.health <= 0:
                continue_battle = False
                winner = opponent_two

        self.display_winner(winner)

    def attack_sequence(self):
        first_roll = self.roll_dice()
        second_roll = self.roll_dice()

        while first_roll == second_roll:
            first_roll = self.roll_dice()
            second_roll = self.roll_dice()

        if first_roll > second_roll:
            return [self.fleet.pop(0), self.herd.pop(0)]
        else:
            return [self.herd.pop(0), self.fleet.pop(0)]

    def roll_dice(self):
        return randint(1, 6)

    def generate_attack_power(self):
        damage_level = self.roll_dice()

        if damage_level == 6:
            multiplier = 0
        elif 5 >= damage_level >= 2:
            multiplier = 1/damage_level
        else:
            multiplier = 1

        return multiplier
