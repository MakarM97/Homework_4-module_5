from random import randint


class Buiding:
    total_building = 0

    def __init__(self):
        Buiding.total_building += 1


buildings = []
buildings_count = randint(0, 40)
while len(buildings) < buildings_count:
    new_building = Buiding()
    buildings.append(new_building)
print(Buiding.total_building)



