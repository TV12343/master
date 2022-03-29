from django.db import models

class Reviews(models.Model):
    name =  models.TextField(
        verbose_name='Имя',
    )
    review =  models.TextField(
        verbose_name='Отзыв',
    )
    date =  models.TextField(
        verbose_name='Дата',
    )
    class Meta:
            verbose_name = 'Отзывы Yandex'
            verbose_name_plural = 'Отзывы Yandex'

class ReviewsZoon(models.Model):
    name1 =  models.TextField(
        verbose_name='Имя',
    )
    review1 =  models.TextField(
        verbose_name='Отзыв',
    )
    date1 =  models.TextField(
        verbose_name='Дата',
    )
    class Meta:
            verbose_name = 'Отзывы Zoon'
            verbose_name_plural = 'Отзывы Zoon'

class ReviewsYoll(models.Model):
    name2 =  models.TextField(
        verbose_name='Имя',
    )
    review2 =  models.TextField(
        verbose_name='Отзыв',
    )
    date2 =  models.TextField(
        verbose_name='Дата',
    )
    rating2 =  models.TextField(
        verbose_name='Рейтинг',
    )
    class Meta:
        verbose_name = 'Отзывы Yoll'
        verbose_name_plural = 'Отзывы Yoll'


