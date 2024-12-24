from django.db import models
from django.core.validators import MinValueValidator
from home.services import convert_image_to_webp


class Slide(models.Model): 
    title = models.CharField('Заголовок', max_length=80)
    description = models.TextField('Описание') 
    photo = models.ImageField('Фото', upload_to='home/slides')
    square = models.FloatField('Площадь', validators=[MinValueValidator(0.0)])
    bedrooms_quantity = models.SmallIntegerField('Количество спален', default=1)
    bathrooms_quantity = models.SmallIntegerField('Количество санузлов', validators=[MinValueValidator(0.0)], default=1)
    price = models.DecimalField('Цена', decimal_places=2, max_digits=12)

    class Meta: 
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'

    def save(self, *args, **kwargs):
        # TODO
        # if self.pk:
        #     old_image = self.__class__.objects.filter(pk=self.pk).first().photo
        #     if old_image and self.photo and old_image.name == self.photo.name:
        #         super(self.__class__, self).save(*args, **kwargs)
        #         return
            
        webp_image = convert_image_to_webp(self.photo)
        if webp_image:
            self.photo.save(webp_image.name, webp_image, save=False)
        
        super(self.__class__, self).save(*args, **kwargs)


class CompanyInfo(models.Model): 
    subheader = models.TextField('Подзаголовок', default='', max_length=200)
    description = models.TextField('Описание', null=True, blank=True)
    history = models.TextField('История компании', null=True, blank=True)
    mission = models.TextField('Миссия компании', null=True, blank=True)
    address = models.CharField('Адрес', max_length=120, null=True, blank=True)
    working_mode = models.TextField('Режим работы', null=True, blank=True)
    phone = models.CharField('Номер телефона', max_length=20, null=True, blank=True)
    email = models.CharField('Email', max_length=50, null=True, blank=True)
    whatsapp = models.CharField('Ссылка на Whatsapp', max_length=200, null=True, blank=True)
    full_name = models.CharField('Полное название организации', max_length=120, null=True, blank=True)
    ogrn = models.CharField('ОГРН', max_length=13, null=True, blank=True)
    inn = models.CharField('ИНН', max_length=10, null=True, blank=True)
    two_gis_profile = models.URLField('Ссылка на профиль в 2GIS', max_length=200, default='https://2gis.ru/vladivostok/firm/70000001059056448/tab/reviews')

    admin_panel_title = models.CharField(
        'Название вкладки в админке', 
        max_length=40, 
        default='Информация о компании'
    )

    class Meta: 
        verbose_name = 'Информация о компании'
        verbose_name_plural = 'Информация о компании'

    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)

    @classmethod
    def get_instance(cls) -> "CompanyInfo":
        instance, created = cls.objects.get_or_create(id=1)
        return instance
    
    def __str__(self) -> str: 
        return 'Информация о компании'
    

class CooperationStage(models.Model): 
    number = models.CharField('Порядковый номер', max_length=2, blank=True, null=True)
    name = models.CharField('Название', max_length=80, blank=True, null=True)
    description = models.TextField('Описание', blank=True, null=True)
    image = models.ImageField('Картинка', null=True, blank=True, upload_to='home/cooperation_stages')

    class Meta: 
        verbose_name = 'Этап сотрудничества'
        verbose_name_plural = 'Этапы сотрудничества'

    def save(self, *args, **kwargs):
        # TODO
        # if self.pk:
        #     old_image = self.__class__.objects.filter(pk=self.pk).first().image
        #     if old_image and self.image and old_image.name == self.image.name:
        #         super(self.__class__, self).save(*args, **kwargs)
        #         return

        webp_image = convert_image_to_webp(self.image)
        if webp_image:
            self.image.save(webp_image.name, webp_image, save=False)
        
        super(self.__class__, self).save(*args, **kwargs)

    def __str__(self): 
        return f'{self.number}. {self.name}' if self.name else f'Картинка "{self.image.name}"'


class PopularQuestion(models.Model): 
    question = models.CharField('Вопрос', max_length=150)
    answer = models.TextField('Ответ')

    class Meta: 
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Часто задаваемые вопросы'