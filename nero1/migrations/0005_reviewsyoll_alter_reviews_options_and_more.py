# Generated by Django 4.0.2 on 2022-03-27 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nero1', '0004_reviewszoon_alter_reviews_options_alter_reviews_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewsYoll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name2', models.TextField(verbose_name='Имя')),
                ('review2', models.TextField(verbose_name='Отзыв')),
                ('date2', models.TextField(verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы Yoll',
            },
        ),
        migrations.AlterModelOptions(
            name='reviews',
            options={'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы Yandex'},
        ),
        migrations.AlterModelOptions(
            name='reviewszoon',
            options={'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы Zoon'},
        ),
    ]
