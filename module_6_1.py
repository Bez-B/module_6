class Animal:
    """
    Класс животных (родительский класс)
    """

    alive = True  # (живой)
    fed = False  # (накормленный)

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        self.food = food                                    # food - это параметр, принимающий объекты классов растений
        if food.edible:                                     # Если съедобно (True)
            print(f'{self.name} съел {food.name}')
            Animal.fed = True                               # Становится накормленным
        else:                                               # Тогда не съедобно (False)
            print(f'{self.name} не стал есть {food.name}')
            Animal.alive = False                            # Становится неживым

class Mammal(Animal):
    """
    Класс млекопитающие (подкласс животных или дочерний класс)
    """
    pass

class Predator(Animal):
    """
    Класс хищники (подкласс животных или дочерний класс)
    """
    pass


class Plant:
    """
    Класс растений (родительский класс)
    """

    edible = False  # (съедобность)

    def __init__(self, name):
        self.name = name

class Flower(Plant):
    """
    Класс цветов (подкласс растений или дочерний класс)
    """
    pass

class Fruit(Plant):
    """
    Класс фруктов (подкласс растений или дочерний класс)
    """
    edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

# Что произошло: Хищник попытался съесть цветок и погиб, млекопитающее съело фрукт и насытилось.
