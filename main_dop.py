# -*- coding: utf-8 -*-
from classes import *

zoo = Zoo("Москва")
zoo.read_data('data.txt')

zoo.zoo_info()

zoo.add_animal("Mammal","Слон","30","Туууу","Травоядный")
zoo.add_employee("ZooKeeper","Катя")

zoo.write_data()