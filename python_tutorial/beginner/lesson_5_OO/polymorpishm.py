class Duck():
    def fly(self):
        print("The duck is flying")

    def soar(self):
        print("A duck cannot soar")

    def feed(self):
        print("The duck eats bread")


class Eagle():
    def fly(self):
        print("The eagle is flying.")

    def soar(self):
        print("The eagle soars to great heights")

    def feed(self):
        print("The eagle eats a lamb")


def fly_bright(bird):
    bird.soar()


def eat_something(bird):
    bird.feed()


donald = Duck()
USA = Eagle()
fly_bright(donald)
fly_bright(USA)
eat_something(donald)
eat_something(USA)