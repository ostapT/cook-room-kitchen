from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class AdminPageTests(TestCase):
    def setUp(self) -> None:
        self.admin_user = get_user_model().objects.create_superuser(
            username="user.admin",
            password="password123",
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            username="user1",
            password="passusertest",
            first_name="Test_first",
            last_name="Test_last",
            years_of_experience=3,
        )

    def test_show_years_of_experience_list(self):
        url = reverse("admin:kitchen_cook_changelist")
        response = self.client.get(url)

        self.assertContains(response, self.user.years_of_experience)

    def test_show_dish_list(self):
        url = reverse("admin:kitchen_dish_changelist")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
