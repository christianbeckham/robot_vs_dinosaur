from weapon import Weapon


class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = None

    def attack(self, rival, power_level):
        self.select_weapon()
        power_of_attack = self.active_weapon.attack_power * power_level

        if rival.health - power_of_attack > 0:
            rival.health = rival.health - power_of_attack
        else:
            rival.health = 0

        print(f'{self.name} attacked with {self.active_weapon.name} causing {power_of_attack} damage points.')

    def select_weapon(self):
        available_weapons = [
            {'name': 'Knuckle-Spikes', 'attack_power': 10},
            {'name': 'Dual Energon Swords', 'attack_power': 20},
            {'name': 'Ion Blasters', 'attack_power': 45}
        ]

        self.display_available_weapons(available_weapons)
        selection = self.verify_weapon_selection(available_weapons)
        weapon_name = available_weapons[selection]['name']
        weapon_attack_power = available_weapons[selection]['attack_power']
        self.active_weapon = Weapon(weapon_name, weapon_attack_power)

    def display_available_weapons(self, available_weapons):
        print('Select from available weapons:')

        for index in range(len(available_weapons)):
            print(
                f"\tSelect [{index + 1}] for {available_weapons[index]['name']}")

    def verify_weapon_selection(self, available_weapons):
        input_option = int(input('Enter option: '))
        valid_input = (1 <= input_option <= len(available_weapons))

        while valid_input != True:
            print('Invalid. Please enter a valid option.')
            return self.verify_weapon_selection(available_weapons)

        return (input_option - 1)
