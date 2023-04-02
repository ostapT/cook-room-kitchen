# Generated by Django 4.1.7 on 2023-04-02 15:49

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("kitchen", "0002_alter_cook_years_of_experience"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="cook",
            options={"verbose_name": "cook", "verbose_name_plural": "cooks"},
        ),
        migrations.AlterModelOptions(
            name="dish",
            options={"ordering": ["dish_type"]},
        ),
        migrations.AlterModelOptions(
            name="dishtype",
            options={"ordering": ["name"]},
        ),
    ]
