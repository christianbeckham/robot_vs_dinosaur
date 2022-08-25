from weapon import Weapon


class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon('Ion Blaster', 25)

    def attack(self, dinosaur):

        if dinosaur.health - self.active_weapon.attack_power > 0:
            dinosaur.health = dinosaur.health - self.active_weapon.attack_power
        else:
            dinosaur.health = 0

        print(
            f'\n{self.name} attacked {dinosaur.name} with an {self.active_weapon.name} having an attack power of {self.active_weapon.attack_power}.')
        print(f'\t{dinosaur.name}\'s health is now at {dinosaur.health}.')
