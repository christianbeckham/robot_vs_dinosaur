class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 100

    def attack(self, robot):

        if robot.health - self.attack_power > 0:
            robot.health = robot.health - self.attack_power
        else:
            robot.health = 0

        print(
            f'\n{self.name} attacked {robot.name} with an attack power of {self.attack_power}.')
        print(f'\t{robot.name}\'s health is now at {robot.health}.')
