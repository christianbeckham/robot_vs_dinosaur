class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 100

    def attack(self, rival, power_level):
        power_of_attack = self.attack_power * power_level

        if rival.health - power_of_attack > 0:
            rival.health = rival.health - power_of_attack
        else:
            rival.health = 0

        print(f'{self.name} attacked causing {power_of_attack} damage points.')
