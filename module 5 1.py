class House:
    def __init__(self, name, number_of_flours):
        self.name = name
        self.number_of_floors = number_of_flours
    def go_to(self, new_floor):
        if 0 < new_floor <= self.number_of_floors:
            for i in range(1, new_floor + 1):
                print(i)
        else:
            print('Такого этажа не существует')




h1 = House('ЖК Ботаника', 20)
h2 = House('Бирюзовая', 5)
h1.go_to(5)
h2.go_to(10)

