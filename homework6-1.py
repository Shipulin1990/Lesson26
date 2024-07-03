class Animal:
    def __init__(self,name):
        self.alive = True
        self.fed = False
        self.name = name

    def eat(self, food):
        if food.edible :
            print('{} съел {}'.format(self.name, food.name))
            self.fed = True
        else:
            print('{} не стал есть {}'.format(self.name, food.name))
            self.alive = False

class Plant:
    def __init__(self, name):
        self.name = name
        self.edible = False

class Mammal(Animal):
    def __init__(self,name):
        super().__init__(name)

class Predator(Animal):
    def __init__(self,name):
        super().__init__(name)

class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True

class Flower(Plant):
    def __init__(self, name):
        super().__init__(name)


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name) # Волк с Уолл-Стрит
print(p1.name) # Цветик семицветик

print(a1.alive) # True
print(a2.fed) # False
a1.eat(p1) # Волк с Уолл-Стрит не стал есть Цветик семицветик
a2.eat(p2) # Хатико съел Заводной апельсин
print(a1.alive) # False
print(a2.fed) # True
