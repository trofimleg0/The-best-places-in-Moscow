# Generated by Django 4.2.5 on 2023-10-01 16:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("moscow_places", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="place",
            name="short_description",
            field=models.TextField(verbose_name="Short description"),
        ),
    ]
