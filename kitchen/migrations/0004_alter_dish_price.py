# Generated by Django 4.1.7 on 2023-04-13 13:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("kitchen", "0003_alter_cook_options_alter_dish_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dish",
            name="price",
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5),
        ),
    ]
