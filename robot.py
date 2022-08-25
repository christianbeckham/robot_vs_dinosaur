from weapon import Weapon


class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = None

    def attack(self, dinosaur):
        print(f'\n{self.name} is about to attack...')
        self.active_weapon = self.select_weapon()

        if dinosaur.health - self.active_weapon.attack_power > 0:
            dinosaur.health = dinosaur.health - self.active_weapon.attack_power
        else:
            dinosaur.health = 0

        print(
            f'\n{self.name} attacked {dinosaur.name} with an {self.active_weapon.name} having an attack power of {self.active_weapon.attack_power}.')
        print(f'\t{dinosaur.name}\'s health is now at {dinosaur.health}.')

    def select_weapon(self):
        available_weapons = [
            {'name': 'Knuckle-Spikes', 'attack_power': 10},
            {'name': 'Dual Energon Swords', 'attack_power': 20},
            {'name': 'Ion Blaster', 'attack_power': 45}
        ]

        self.display_available_weapons(available_weapons)
        selection = self.verify_weapon_selection(available_weapons)
        weapon_name = available_weapons[selection]['name']
        weapon_attack_power = available_weapons[selection]['attack_power']
        selected_weapon = Weapon(weapon_name, weapon_attack_power)
        return selected_weapon

    def display_available_weapons(self, available_weapons):
        print('Select from available weapons:')

        for index in range(len(available_weapons)):
            print(
                f"\tSelect [{index + 1}] for {available_weapons[index]['name']} (attack power: {available_weapons[index]['attack_power']})")

    def verify_weapon_selection(self, available_weapons):
        input_option = int(input('Enter option: '))
        valid_input = (1 <= input_option <= len(available_weapons))

        while valid_input != True:
            print('Invalid. Please enter a valid option.')
            return self.verify_weapon_selection(available_weapons)

        return (input_option - 1)
