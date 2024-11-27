from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class TwoGISReview(models.Model): 
    rate = models.SmallIntegerField('Оценка', validators=[
        MinValueValidator(1), 
        MaxValueValidator(5)
    ])
    username = models.CharField('Имя пользователя', max_length=100)
    content = models.TextField('Содержание')
    created_at = models.DateTimeField('Дата и время публикации')

    class Meta: 
        verbose_name = 'Отзыв с 2GIS'
        verbose_name_plural = 'Отзывы с 2GIS'
        ordering = ['-created_at']

    def __str__(self) -> str: 
        return self.content[:20]