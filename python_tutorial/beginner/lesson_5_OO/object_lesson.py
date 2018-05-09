class Restaurant:

    def __init__(self, name, price_level="Unknown", stars=0):
        self.name = name
        self.price_level = price_level
        self.stars = stars
        self.staff = []

    def show_name(self):
        print(self.name)

    def show_price(self):
        print(self.price_level)

    def show_stars(self):
        print(self.stars)

    def show_staff(self):
        if self.staff.__len__() < 1:
            print("No staff at the moment")
        for member in self.staff:
            print(member.name, member.function, member.salary)

    def new_stars_awarded(self, stars):
        if type(self) is CheapRestaurant:
            print("Cheap restaurants do not get stars")
        else:
            self.stars = stars

    def add_staff_object(self, staff):
        self.staff.append(staff)

    def print_object_data(self):
        print(self)


class LuxuryRestaurant(Restaurant):

    def __init__(self, name, price_level):
        super().__init__(name, price_level)


class MichelinStarRestaurant(Restaurant):
    def __init__(self, name, stars):
        super().__init__(name, "Extreme", stars)


class CheapRestaurant(Restaurant):

    def __init__(self, name, price_level):
        super().__init__(name, price_level)


class Staff:

    def __init__(self, name, function, salary):
        self.name = name
        self.function = function
        self.salary = salary

    def give_raise(self, perc_raise):
        self.salary = self.salary + self.salary * perc_raise

    def work_work(self):
        print("Your wish is my command")

class Chef(Staff):

    def __init__(self, name, salary=2500.00):
        super().__init__(name, "Chef", salary)

    def work_work(self):
        print("More Work?")

class Waiter(Staff):

    def __init__(self, name, salary=2000.00):
        super().__init__(name, "Waiter", salary)

    def work_work(self):
        print("Something to doing?")


def work_even_more(worker):
    worker.work_work()

Librije = MichelinStarRestaurant("De Librije", 3)
Bolenius = MichelinStarRestaurant("Bolenius", 1)
PaarseDoos = CheapRestaurant("De Paarse Doos", "Low")
BijOns = LuxuryRestaurant("Bij ons", "Average")


Librije.show_name()
Librije.show_price()
Librije.show_stars()
print('---------------------')
Bolenius.show_name()
Bolenius.show_price()
Bolenius.show_stars()
print('---------------------')
PaarseDoos.show_name()
PaarseDoos.show_price()
PaarseDoos.show_stars()
print('---------------------')
BijOns.show_name()
BijOns.show_price()
BijOns.show_stars()
print('---------------------')
PaarseDoos.new_stars_awarded(3)
PaarseDoos.show_stars()
Bolenius.new_stars_awarded(2)
Bolenius.show_stars()
print('---------------------')

Librije.print_object_data()
Bolenius.print_object_data()
PaarseDoos.print_object_data()
BijOns.print_object_data()
print('---------------------')
Librije.show_staff()
print('---------------------')

Johhny = Staff("Johnny", "Owner", 5000.00)
Librije.add_staff_object(Johhny)
Librije.add_staff_object(Chef("Sergio", 4000.00))
Librije.show_staff()
print('---------------------')

Gordon = Chef("Gordon")
Librije.add_staff_object(Gordon)
Librije.show_staff()
print('---------------------')

JeanLuc= Waiter("Jean-Luc")
Librije.add_staff_object(JeanLuc)
Librije.show_staff()
print('---------------------')

JeanLuc.give_raise(10)
Librije.show_staff()
Bolenius.show_staff()
PaarseDoos.show_staff()
BijOns.show_staff()

print('---------------------')
PaarseDoos.add_staff_object(Chef("Beunhaas", 1750))
PaarseDoos.show_staff()

print('---------------------')
work_even_more(Gordon)
work_even_more(JeanLuc)
work_even_more(Johhny)