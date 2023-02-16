# Generated by Django 4.1.7 on 2023-02-15 21:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("movies", "0003_movieorder_movie_orders"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="orders",
            field=models.ManyToManyField(
                related_name="ordered_movies",
                through="movies.MovieOrder",
                to="movies.movie",
            ),
        ),
    ]
