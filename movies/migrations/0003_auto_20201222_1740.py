# Generated by Django 3.1.4 on 2020-12-22 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20201214_0142'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'verbose_name': 'Жанр', 'verbose_name_plural': 'Жанры'},
        ),
        migrations.AlterModelOptions(
            name='movie',
            options={'verbose_name': 'Фильм', 'verbose_name_plural': 'Фильмы'},
        ),
        migrations.AlterModelOptions(
            name='persone',
            options={'verbose_name': 'Персоны', 'verbose_name_plural': 'Персоны'},
        ),
        migrations.AlterModelOptions(
            name='rating',
            options={'verbose_name': 'Рейтинг', 'verbose_name_plural': 'Рейтинги'},
        ),
        migrations.AlterModelOptions(
            name='reviews',
            options={'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
        migrations.AlterModelOptions(
            name='shots',
            options={'verbose_name': 'Кадр из фильма', 'verbose_name_plural': 'Кадры из фильма'},
        ),
        migrations.AlterModelOptions(
            name='star',
            options={'ordering': ['-value'], 'verbose_name': 'Звезда', 'verbose_name_plural': 'Звезды'},
        ),
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(related_name='film_actor', to='movies.Persone', verbose_name='актер'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='directors',
            field=models.ManyToManyField(related_name='film_director', to='movies.Persone', verbose_name='режиссер'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(to='movies.Genre', verbose_name='жанры'),
        ),
    ]
