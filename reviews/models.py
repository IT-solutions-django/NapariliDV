from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Platform(models.Model): 
    name = models.CharField('Название платформы', max_length=100)

    def __str__(self) -> str: 
        return self.name
    
    class Meta:
        verbose_name = 'Платформа'
        verbose_name_plural = 'Платформы с отзывами'


class Review(models.Model): 
    rate = models.SmallIntegerField('Оценка', validators=[
        MinValueValidator(1), 
        MaxValueValidator(5)
    ])
    author = models.CharField('Имя автора', max_length=100)
    author_avatar = models.URLField('Аватар автора', null=True, blank=True)
    content = models.TextField('Содержание')
    created_at = models.DateTimeField('Дата и время публикации')
    platform = models.ForeignKey(verbose_name='Платформа', to=Platform, on_delete=models.CASCADE)

    class Meta: 
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-created_at']

    def __str__(self) -> str: 
        return f'{self.created_at}, {self.platform}, {self.author}'
    

class ReviewPhoto(models.Model): 
    url = models.URLField('Фото отзыва')
    review = models.ForeignKey(verbose_name='Отзыв', to=Review, on_delete=models.CASCADE)