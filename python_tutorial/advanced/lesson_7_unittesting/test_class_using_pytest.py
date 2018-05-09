from python_tutorial.advanced.lesson_7_unittesting.testclass import *
import pytest


class TestClassStars(object):
    def test_stars(self):
        Librije = MichelinStarRestaurant("De Librije", 3)
        assert Librije.stars == 3

    def test_set_stars_down(self):
        Librije = MichelinStarRestaurant("De Librije", 3)
        Librije.new_stars_awarded(2)
        assert Librije.stars == 2

    def test_set_stars_up(self):
        Bolenius = MichelinStarRestaurant("Bolenius", 1)
        Bolenius.new_stars_awarded(2)
        assert Bolenius.stars == 2

    def test_cannot_set_stars_for_cheaprestaurant(self):
        PaarseDoos = CheapRestaurant("De Paarse Doos", "Low")
        PaarseDoos.new_stars_awarded(3)
        assert PaarseDoos.stars == 0

    def test_stars_cannot_exceed_three(self):
        Librije = MichelinStarRestaurant("De Librije", 3)
        with pytest.raises(ValueError):
            Librije.new_stars_awarded(4)


class TestClassShowNames(object):
    def test_stars(self):
        Librije = MichelinStarRestaurant("De Librije", 3)
        name = Librije.show_name()
        assert name == "De Librije"
