# Generated by Django 4.1.7 on 2023-02-15 13:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="is_employee",
            field=models.BooleanField(default=False, null=True),
        ),
    ]
