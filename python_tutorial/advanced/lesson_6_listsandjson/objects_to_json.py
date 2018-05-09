from datetime import date
import json

class Animal:

    def __init__(self, name, ):
        self.name = name


class Dog(Animal):

    def __init__(self, name, legs, size, species, date_of_birth, owner_name, owner_city, kind="Mammal", frat_dog=False):
        super().__init__(name)
        self.legs = legs
        self.size = size
        self.species = species
        self.date_of_birth = date_of_birth
        self.owner_name = owner_name
        self.owner_city = owner_city
        self.kind = kind
        self.frat_dog = frat_dog


def create_a_json_file(file_name, json_data):
    with open(file_name, 'w') as outfile:
        json.dump(json_data, outfile, indent=4)



d = date(2015, 5, 23).strftime("%d/%m/%Y")


Bully = Dog("Bully", 4, "Medium", "Bulldog", d, "Alpha Beta Phi", "Miami", "Mammal", True)
json_bully = Bully.__dict__
print(json_bully)
create_a_json_file(f'{Bully.name}.json', json_bully)


d = date(1954, 5, 23).strftime("%d/%m/%Y")
Laika = Dog("Laika", 4, "Small", "Jack-Russel", d, "USSR", "Space")
json_laika = Laika.__dict__
print(json_laika)
create_a_json_file(f'{Laika.name}.json', json_laika)

