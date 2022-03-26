from django.db import models

class Reviews(models.Model):
    name =  models.TextField(
        verbose_name='Имя1',
    )
    review =  models.TextField(
        verbose_name='Отзыв',
    )
    date =  models.TextField(
        verbose_name='Дата',
    )


    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
