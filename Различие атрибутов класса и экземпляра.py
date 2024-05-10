class Buiding:
    total_building = 0

    def __init__(self):
        Buiding.total_building += 1

    def buildings_count(self):
        for self.total_building in range(1, 41):
            print(f'Здание номер {self.total_building}')


building = Buiding()
building.buildings_count()





