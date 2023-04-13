from django.contrib.auth import get_user_model
from django.test import TestCase

from kitchen.models import Dish, DishType


class ModelTests(TestCase):
    def test_dish_type_str(self):
        dish_type = DishType.objects.create(name="Bread")
        self.assertEqual(str(dish_type), "Bread")

    def test_cook_str(self):
        cook = get_user_model().objects.create_user(
            username="usertest",
            password="Ban12345",
            first_name="John",
            last_name="Smith"
        )
        self.assertEqual(str(cook), "John Smith")

    def test_dish_str(self):
        dish_type = DishType.objects.create(name="Bread")
        dish = Dish.objects.create(name="Baguette", dish_type=dish_type, price=20.99)

        self.assertEqual(str(dish), "Baguette price: 20.99")
