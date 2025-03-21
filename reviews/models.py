from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid
from home.models import convert_image_to_webp


class Platform(models.Model): 
    name = models.CharField('Название платформы', max_length=100)
    icon = models.ImageField('Иконка', upload_to='reviews/platforms', null=True)
    average_rating = models.FloatField('Средний рейтинг компании на платформе', default=4.9)
    reviews_count = models.IntegerField('Количество отзывов', default=0)
    url = models.URLField('Ссылка на профиль компании')

    def __str__(self) -> str: 
        return self.name
    
    class Meta:
        verbose_name = 'Платформа'
        verbose_name_plural = 'Платформы с отзывами'

    def save(self, *args, **kwargs):
        if self.pk:
            old_image = self.__class__.objects.filter(pk=self.pk).first().icon
            if old_image and self.icon and old_image.name == self.icon.name:
                super(self.__class__, self).save(*args, **kwargs)
                return

        webp_image = convert_image_to_webp(self.icon)
        if webp_image:
            self.icon.save(webp_image.name, webp_image, save=False)
        
        super(self.__class__, self).save(*args, **kwargs)


class Review(models.Model): 
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
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
    review = models.ForeignKey(verbose_name='Отзыв', to=Review, on_delete=models.CASCADE, related_name='photos')
