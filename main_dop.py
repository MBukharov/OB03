# -*- coding: utf-8 -*-
from classes import *

zoo = Zoo("Москва")
zoo.read_data('data.txt')   #читаем данные из файла

zoo.zoo_info()  #выводим информацию о зоопарке

#Добавляем новое животное и нового сотрудника
zoo.add_animal("Mammal","Слон","30","Туууу","Травоядный")
zoo.add_employee("ZooKeeper","Катя")

#Записываем данные в файл
zoo.write_data('data.txt')

zoo.zoo_info()  #выводим информацию о зоопарке
zoo.employees[0].feed_animal()  #действия работников
zoo.employees[1].heal_animal()
zoo.animal_sound() #выводим голоса зверей