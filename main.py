from classes import *

#ТЕСТ ЗАДАНИЙ 1-3
def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

print("ТЕСТ ЗАДАНИЙ 1-3")
animals = [Bird("Утка","1","Кря-кря","Перелетная"),
           Mammal("Тигр","5","РРРРР","Хищник"),
           Reptile("Уж","1","Шшшшшшш","Не ядовит")]

animal_sound(animals)


#ТЕСТ ЗАДАНИЙ 4-5
print("\nТЕСТ ЗАДАНИЙ 4-5")
zoo = Zoo("Москва")
zoo.add_animal("Bird","Воробей","2","Чирик-чирик","Не перелетный")
zoo.add_animal("Mammal","Лев","5","РРРРР","Хищник")
zoo.add_animal("Reptile","Кобра","2","Шшшшшш","Ядовита")

zoo.add_employee("ZooKeeper","Валера")
zoo.add_employee("Veterinarian","Анна")

zoo.zoo_info()
zoo.employees[0].feed_animal()
zoo.employees[1].heal_animal()
zoo.animal_sound()

zoo.write_data("data.txt")

