import random


class Animal:
    """
    Класс описывающий животных
    """

    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed, _cords = None):
        if _cords is None:
            _cords = [0, 0, 0]
        self.speed = speed
        self._cords = _cords

    def move(self, dx, dy, dz):
        self._cords[0] = dx * self.speed
        self._cords[1] = dy * self.speed
        if dz * self.speed < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords[2] = dz * self.speed
        return self._cords

    def get_cords(self):
        print(f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        elif self._DEGREE_OF_DANGER >= 5:
            print("Be careful, i'm attacking you 0_0")


class Bird(Animal):
    """
    Класс, описывающий птиц. Наследуется от Animals.
    """

    beak = True  # наличие клюва

    def lay_eggs(self):
        number_of_eggs = random.randint(1, 4)
        if number_of_eggs == 1:
            print(f'Here is {number_of_eggs} egg for you')
        else:
            print(f'Here are {number_of_eggs} eggs for you')


class AquaticAnimal(Animal):
    """
    Класс, описывающий плавающего животного. Наследуется от Animals.
    """

    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        if self._cords[2] < abs(dz) * self.speed:
            # self._cords[2] -= int(abs(dz) * (self.speed / 2))  # Формула дающая ответ как в задании
            self._cords[2] = 0 - int((abs(dz) * self.speed - self._cords[2]) / 2)  # Мой вариант. Пояснение под методом.
        else:
            self._cords[2] -= abs(dz) * self.speed
    """
    Если при проверке начальная координата меньше пройденного пути, то есть self._cords[2] < abs(dz) * self.speed,
    то значит часть пути равная координате self._cords[2] пройдена до отметки "0" над водой со скоростью self.speed,
    а остальная часть пути равная (abs(dz) - elf._cords[2] / self.speed) * (self.speed / 2) уже пройдена с половинной 
    скоростью и ниже нулевой отметки. После преобразования выражение принимает вид: 
    self._cords[2] = 0 - int((abs(dz) * self.speed - self._cords[2]) / 2).
    Правда в задании есть противоречие. Метод move класса Animal гласит: "It's too deep, i can't dive :(". 
    Получается, что никакие животные не могут нырять, даже из дочернего класса AquaticAnimal.
    В таком случае правильно было бы так:
    if self._cords[2] < abs(dz) * self.speed:
        print("It's too deep, i can't dive :(")
    """

class PoisonousAnimal(Animal):
    """
    Класс, описывающий ядовитых животных. Наследуется от Animals.
    """

    _DEGREE_OF_DANGER = 8


class Duckbill(Bird, PoisonousAnimal,  AquaticAnimal):
    """
    Класс, описывающий утконоса. Наследуется от классов Bird, AquaticAnimal, PoisonousAnimal.
    """

    sound = "Click-click-click"

    def speak(self):
        print(self.sound)




db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()
