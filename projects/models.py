from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse


class Category(models.Model): 
    name = models.CharField('Название', max_length=100)

    class Meta: 
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self) -> str: 
        return f'{self.name}'


class Material(models.Model): 
    name = models.CharField('Название', max_length=100)

    class Meta: 
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'

    def __str__(self) -> str: 
        return f'{self.name}'


class RoofType(models.Model): 
    name = models.CharField('Название', max_length=100)

    class Meta: 
        verbose_name = 'Тип кровли'
        verbose_name_plural = 'Типы кровли'

    def __str__(self) -> str: 
        return f'{self.name}'


class Project(models.Model): 
    name = models.CharField('Название', max_length=100)
    description = models.TextField('Описание')
    square = models.FloatField('Площадь', validators=[MinValueValidator(0.0)])
    price = models.DecimalField('Цена', decimal_places=2, max_digits=12)
    bedrooms_quantity = models.SmallIntegerField('Количество спален', default=1)
    rooms_quantity = models.SmallIntegerField('Количество комнат', validators=[MinValueValidator(0.0)], default=1)
    floors_quantity = models.SmallIntegerField('Количество этажей', validators=[MinValueValidator(0.0)], default=1)
    bathrooms_quantity = models.SmallIntegerField('Количество санузлов', validators=[MinValueValidator(0.0)], default=1)
    estimates = models.FileField('Смета', upload_to='projects/estimates', null=True, blank=True)
    is_the_best = models.BooleanField('Входит в топ', default=False)
    is_in_gallery = models.BooleanField('Отображается в галерее', default=False)
    gallery_photo = models.ImageField('Фото в галерее', upload_to='gallery', blank=True, null=True)
    category = models.ForeignKey(
        verbose_name='Категория', 
        to=Category, 
        on_delete=models.CASCADE, 
        related_name='category_projects'
    )
    material = models.ForeignKey(
        verbose_name='Материал', 
        to=Material, 
        on_delete=models.CASCADE, 
        related_name='material_projects'
    )
    roof_type = models.ForeignKey(
        verbose_name='Тип кровли', 
        to=RoofType, 
        on_delete=models.CASCADE, 
        related_name='roof_type_projects'
    )

    class Meta: 
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self) -> str: 
        return f'{self.name} | {self.price} р'
    
    def get_absolute_url(self): 
        return reverse('projects:project', args=[self.id])


class ProjectPhoto(models.Model): 
    image = models.ImageField('Изображение', upload_to='projects', null=True, blank=True)
    project = models.ForeignKey(verbose_name='Проект', to=Project, on_delete=models.CASCADE, related_name='photos', null=True)

    class Meta: 
        verbose_name = 'Фото проекта'
        verbose_name_plural = 'Фото проекта'

    def __str__(self) -> str: 
        return f'{self.image}'