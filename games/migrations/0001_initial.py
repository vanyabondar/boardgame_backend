# Generated by Django 3.2.9 on 2021-11-22 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor_name', models.CharField(max_length=100)),
                ('author_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='GameCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_category_name', models.CharField(max_length=100)),
                ('game_category_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_name', models.CharField(max_length=100)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=8)),
                ('quantity', models.IntegerField()),
                ('game_description', models.TextField()),
                ('released_year', models.IntegerField()),
                ('playing_time', models.IntegerField()),
                ('min_age', models.IntegerField()),
                ('authors', models.ManyToManyField(blank=True, to='games.Author')),
                ('game_category', models.ManyToManyField(blank=True, to='games.GameCategory')),
            ],
        ),
    ]