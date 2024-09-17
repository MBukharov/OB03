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


#ЗАДАНИЕ 4-5
class ZooKeeper():
    def __init__(self,name):
        self.name = name
    def feed_animal(self):
        print(f"Сотрудник {self.name} кормит животных")

class Veterinarian():
    def __init__(self,name):
        self.name = name
    def heal_animal(self):
        print(f"Сотрудник {self.name} лечит животных")

class Zoo():
    def __init__(self,city):
        self.city = city
        self.animals = []
        self.employees = []

    #Добавление животного
    def add_animal(self,what,name,age,sound,feature):
        if what == "Bird":
            self.animals.append(Bird(name,age,sound,feature))
        elif what == "Mammal":
            self.animals.append(Mammal(name, age, sound, feature))
        elif what == "Reptile":
            self.animals.append(Reptile(name, age, sound, feature))

    # Добавление сотрудника
    def add_employee(self,name,who):
        if who == "Zookeeper":
            self.employees.append(ZooKeeper(name))
        elif who == "Veterinarian":
            self.employees.append(Veterinarian(name))

    def zoo_info(self):
        print(f"Зоопарк в {self.city} имеет следующих зверей:")
        for animal in self.animals:
            print(f"{animal.name}, возраст: {animal.age}")
        print(f"Зоопарк в {self.city} имеет следующих сотрудников:")
        for person in self.employees:
            print(f"{person.name}, должность: {person.__class__.__name__}")

    def animal_sound(self):
        print("Голоса животных:")
        for animal in self.animals:
            animal.make_sound()