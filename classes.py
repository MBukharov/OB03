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
        print(f"Новое животное {name} добавлено")

    # Добавление сотрудника
    def add_employee(self,who,name):
        if who == "ZooKeeper":
            self.employees.append(ZooKeeper(name))
        elif who == "Veterinarian":
            self.employees.append(Veterinarian(name))
        print(f"Новый сотрудник {name} добавлен")

    def zoo_info(self):
        print(f"\nЗоопарк {self.city} имеет следующих зверей:")
        for animal in self.animals:
            match animal.__class__.__name__:
                case "Bird": print(f"{animal.name}, возраст: {animal.age}, {animal.types}")
                case "Mammal": print(f"{animal.name}, возраст: {animal.age}, {animal.predator}")
                case "Reptile": print(f"{animal.name}, возраст: {animal.age}, {animal.toxic}")
        print(f"Зоопарк в {self.city} имеет следующих сотрудников:")
        for person in self.employees:
            print(f"{person.name}, должность: {person.__class__.__name__}")

    def animal_sound(self):
        print("\nГолоса животных:")
        for animal in self.animals:
            animal.make_sound()

    def write_data(self,filename):
        with open(filename,'w',encoding="utf-16") as file:
            for animal in self.animals:
                if animal.__class__.__name__ == "Bird":
                    file.write(f"animal\tBird\t{animal.name}\t{animal.age}\t{animal.sound}\t{animal.types}\t\n")
                elif animal.__class__.__name__ == "Mammal":
                    file.write(f"animal\tMammal\t{animal.name}\t{animal.age}\t{animal.sound}\t{animal.predator}\t\n")
                elif animal.__class__.__name__ == "Reptile":
                    file.write(f"animal\tReptile\t{animal.name}\t{animal.age}\t{animal.sound}\t{animal.toxic}\t\n")
            for person in self.employees:
                file.write(f"employee\t{person.__class__.__name__}\t{person.name}\t\n")
        print("Файл с данными записан")

    def read_data(self,filename):
        try:
            with open(filename, 'r',encoding="utf-16") as file:
                for line in file:
                    data = line.split("\t")
                    if data[0] == "animal":
                        self.animals.append(Bird(data[2],data[3],data[4],data[5]))
                    elif data[0] == "employee":
                        match data[1]:
                            case "ZooKeeper": self.employees.append(ZooKeeper(data[2]))
                            case "Veterinarian": self.employees.append(Veterinarian(data[2]))
            print("Файл с данными прочитан")
        except FileNotFoundError:
            print(f"Ошибка чтения файла. Файла {filename} не существует")