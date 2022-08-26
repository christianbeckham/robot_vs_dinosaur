from robot import Robot


class Fleet:
    def __init__(self):
        self.robots = []

    def create_fleet(self, fleet_count):
        for number in range(fleet_count):
            new_robot = Robot(f'Optimus Prime {number + 1}')
            self.robots.append(new_robot)

        return self.robots
