from dinosaur import Dinosaur


class Herd:
    def __init__(self):
        self.dinosaurs = []

    def create_herd(self, herd_count):
        for number in range(herd_count):
            new_dino = Dinosaur(f'Godzilla {number + 1}', 30)
            self.dinosaurs.append(new_dino)

        return self.dinosaurs
