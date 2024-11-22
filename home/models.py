from django.db import models


class Slide(models.Model): 
    title = models.CharField('Заголовок', max_length=80)
    description = models.TextField('Описание') 
    photo = models.ImageField('Фото', upload_to='home/slides')
    button_text = models.CharField('Надпись на кнопке', max_length=50)

    class Meta: 
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'


class CompanyAdvantage(models.Model): 
    name = models.CharField('Название', max_length=100), 
    photo = models.ImageField('Фото', upload_to='home/company_advantages')
    description = models.TextField('Описание')

    class Meta: 
        verbose_name = 'Преимущество'
        verbose_name_plural = 'Преимущества компании'


class CompanyFact(models.Model): 
    name = models.CharField('Название', max_length=100)

    class Meta: 
        verbose_name = 'Факт'
        verbose_name_plural = 'Факты о компании'


class CompanyService(models.Model): 
    name = models.CharField('Название', max_length=50)

    class Meta: 
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги компании'


class CompanyInfo(models.Model): 
    description = models.TextField('Описание')
    history = models.TextField('История компании')
    mission = models.TextField('Миссия компании')
    address = models.CharField('Адрес', max_length=120)
    working_mode = models.TextField('Режим работы')
    phone = models.CharField('Номер телефона', max_length=20)
    email = models.CharField('Email', max_length=50)
    whatsapp = models.CharField('Ссылка на Whatsapp', max_length=200)

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
    name = models.CharField('Название', max_length=80)
    icon = models.FileField('Иконка')

    class Meta: 
        verbose_name = 'Этап сотрудничества'
        verbose_name_plural = 'Этапы сотрудничества'


class PopularQuestion(models.Model): 
    question = models.CharField('Вопрос', max_length=150)
    answer = models.CharField('Ответ', max_length=150)

    class Meta: 
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Часто задаваемые вопросы'