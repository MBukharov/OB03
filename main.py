class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def make_sound(self,sound):
        print(f"{self.name} говорит - {sound}")
    def eat(self):
        print("Животное кушает")

class Bird(Animal):
    def __init__(self,name,age,sound,types):
        super().__init__(name,age)
        self.sound = sound
        self.types = types
    def make_sound(self):
        super().make_sound(self.sound)

class Mammal(Animal):
    def __init__(self,name,age,sound,predator):
        super().__init__(name,age)
        self.sound = sound
        self.predator = predator
    def make_sound(self):
        super().make_sound(self.sound)

class Reptile(Animal):
    def __init__(self, name, age, sound, toxic):
        super().__init__(name, age)
        self.sound = sound
        self.toxic = toxic
    def make_sound(self):
        super().make_sound(self.sound)

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

animals = [Bird("Утка","1","Кря-кря","Перелетная"),
           Mammal("Тигр","5","РРРРР","Хищник"),
           Reptile("Уж","1","Шшшшшшш","Не ядовит")]

animal_sound(animals)