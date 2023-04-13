from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from kitchen.models import DishType, Dish


class PublicTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_dish_type_list_login_required(self):
        response = self.client.get(reverse("kitchen:dish-type-list"))

        self.assertNotEqual(response.status_code, 200)

    def test_dish_list_login_required(self):
        response = self.client.get(reverse("kitchen:dish-list"))

        self.assertNotEqual(response.status_code, 200)

    def test_cook_list_login_required(self):
        response = self.client.get(reverse("kitchen:cook-list"))

        self.assertNotEqual(response.status_code, 200)


class PrivateDishTypeTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="usertest", password="ban12345"
        )
        DishType.objects.create(name="Bread")
        DishType.objects.create(name="Soup")

        self.client.force_login(self.user)

    def test_dish_type_list(self):
        response = self.client.get(reverse("kitchen:dish-type-list"))
        dish_type_list = DishType.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["dish_type_list"]),
            list(dish_type_list),
        )
        self.assertTemplateUsed(response, "kitchen/dish_type_list.html")

    def test_dish_type_search(self):
        dish_type_filtered = DishType.objects.filter(
            name__icontains="Ces"
        )
        response = self.client.get(
            reverse("kitchen:dish-type-list"), {"name": "Ces"}
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["dish_type_list"]),
            list(dish_type_filtered),
        )


class PrivateDishTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="usertest", password="ban12345"
        )
        self.dish_type_1 = DishType.objects.create(
            name="Soup"
        )
        self.dish_type_2 = DishType.objects.create(
            name="Bread"
        )
        self.dish_1 = Dish.objects.create(
            name="Borshch", dish_type=self.dish_type_1
        )
        self.dish_2 = Dish.objects.create(
            name="Baguette", dish_type=self.dish_type_2
        )
        self.client.force_login(self.user)

    def test_dish_list(self):
        response = self.client.get(reverse("kitchen:dish-list"))
        dish_list = Dish.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["dish_list"]), list(dish_list))
        self.assertTemplateUsed(response, "kitchen/dish_list.html")

    def test_dish_detail_view(self):
        response = self.client.get(
            reverse("kitchen:dish-detail", args=[self.dish_1.id])
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "kitchen/dish_detail.html")

    def test_dish_search(self):
        dish_filtered = Dish.objects.filter(name__icontains="Bague")
        response = self.client.get(
            reverse("kitchen:dish-list"), {"name": "Bague"}
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["dish_list"]), list(dish_filtered)
        )

    def test_dish_was_assigned(self):
        url = reverse("kitchen:toggle-dish-assign", args=[self.dish_1.id])
        self.client.get(url)
        self.assertTrue(self.dish_1 in self.user.dishes.all())


class PrivateCookTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="usertest", password="ban12345"
        )
        self.dish_type_1 = DishType.objects.create(
            name="Soup"
        )
        self.dish_type_2 = DishType.objects.create(
            name="Bread"
        )
        self.dish_1 = Dish.objects.create(
            name="Borshch", dish_type=self.dish_type_1
        )
        self.dish_2 = Dish.objects.create(
            name="Baguette", dish_type=self.dish_type_2
        )
        self.client.force_login(self.user)

    def test_cook_list(self):
        response = self.client.get(reverse("kitchen:cook-list"))
        cook_list = get_user_model().objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["cook_list"]), list(cook_list)
        )
        self.assertTemplateUsed(response, "kitchen/cook_list.html")

    def test_cook_detail_view(self):
        response = self.client.get(
            reverse("kitchen:cook-detail", args=[self.user.id])
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "kitchen/cook_detail.html")
