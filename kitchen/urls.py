from django.urls import path

from kitchen.views import index, DishListView, DishDetailView, DishTypeListView, CookListView, CookDetailView, \
    DishTypeCreateView, DishTypeUpdateView, DishTypeDeleteView

urlpatterns = [
    path("", index, name="index"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("dish_types/", DishTypeListView.as_view(), name="dish-type-list"),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
    path("dish_types/create/", DishTypeCreateView.as_view(), name="dish-type-create"),
    path("dish_types/<int:pk>/update", DishTypeUpdateView.as_view(), name="dish-type-update"),
    path("dish_types/<int:pk>/delete", DishTypeDeleteView.as_view(), name="dish-type-delete"),

]

app_name = "kitchen"
