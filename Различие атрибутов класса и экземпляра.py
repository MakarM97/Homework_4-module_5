class Buiding:
    total_building = 0

    def __init__(self):
        Buiding.total_building += 1


for _ in range(1, 41):
    building = Buiding()
    print(f'Здание номер {building.total_building}')
