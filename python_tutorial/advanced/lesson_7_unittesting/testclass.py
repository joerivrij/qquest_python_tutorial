class Restaurant:

    def __init__(self, name, price_level="Unknown", stars=0):
        self.name = name
        self.price_level = price_level
        self.stars = stars
        self.staff = []

    def show_name(self):
        print(self.name)
        return self.name

    def show_price(self):
        print(self.price_level)

    def show_stars(self):
        print(self.stars)
        return self.stars

    def show_staff(self):
        if self.staff.__len__() < 1:
            print("No staff at the moment")
        for member in self.staff:
            print(member.name, member.function, member.salary)

    def new_stars_awarded(self, stars):
        if type(self) is CheapRestaurant:
            print("Cheap restaurants do not get stars")
            return
        if stars > 3:
            raise ValueError("Can only have a max of 3 stars")
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